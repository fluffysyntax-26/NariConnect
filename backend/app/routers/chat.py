from fastapi import APIRouter, Depends
from app.auth.clerk import get_current_user
from app.models.schemas import UserInput, ChatResponse, ExtractedInfo, SchemeResult
from app.services.ollama_service import extract_user_info, chat_with_context
from app.services.vector_service import search_schemes
from app.db.mongo import get_database

router = APIRouter()


async def fetch_deep_details(scheme_ids: list[str]) -> dict:
    """Fetch full scheme details from MongoDB for given scheme slugs."""
    if not scheme_ids:
        return {}

    db = await get_database()
    deep_details = {}

    cursor = db.detailed_schemes.find({"slug": {"$in": scheme_ids}})
    async for doc in cursor:
        # Remove MongoDB's internal _id field for JSON serialization
        doc.pop("_id", None)
        deep_details[doc["slug"]] = doc

    return deep_details


@router.post("/chat", response_model=ChatResponse)
async def chat(
    data: UserInput,
    user_id: str = Depends(get_current_user),
):
    user_profile = extract_user_info(data.message)

    # Use the profile from request if available and not empty, otherwise use extracted
    final_user_profile = (
        data.user_profile
        if data.user_profile and any(data.user_profile.values())
        else user_profile
    )

    search_query = f"""
    Age: {final_user_profile.get("age")}
    Gender: {final_user_profile.get("gender")}
    Occupation: {final_user_profile.get("occupation")}
    State: {final_user_profile.get("state")}
    Income: {final_user_profile.get("income")}
    Query: {data.message}
    """

    schemes = search_schemes(search_query, n_results=5)

    # Fetch deep details from MongoDB for the returned schemes
    scheme_ids = [s["id"] for s in schemes]
    deep_details = await fetch_deep_details(scheme_ids)

    # Add deep details to each scheme result
    for scheme in schemes:
        slug = scheme["id"]
        if slug in deep_details:
            scheme["deep_details"] = deep_details[slug]

    context = "\n\n".join([s["text"] for s in schemes])

    response_text, should_show_schemes = chat_with_context(
        prompt=data.message,
        context=context,
        user_profile=final_user_profile,
        chat_history=data.chat_history,
    )

    return ChatResponse(
        status="success",
        user_profile=ExtractedInfo(**final_user_profile),
        schemes=[SchemeResult(**s) for s in schemes] if should_show_schemes else [],
        response=response_text,
    )
