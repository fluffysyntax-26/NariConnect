from typing import List, Optional, Any, Dict
from pydantic import BaseModel

class ValueLabel(BaseModel):
    value: Any
    label: Optional[str] = None

class SchemeCategory(ValueLabel):
    subcategories: Optional[List[str]] = None

class Reference(BaseModel):
    title: Optional[str] = None
    url: Optional[str] = None

class BasicDetails(BaseModel):
    schemeOpenDate: Optional[Any] = None
    schemeCloseDate: Optional[Any] = None
    state: Optional[str] = None
    nodalMinistryName: Optional[ValueLabel] = None
    nodalDepartmentName: Optional[ValueLabel] = None
    otherMinistryName: Optional[str] = None
    otherDepartmentNames: Optional[str] = None
    targetBeneficiaries: Optional[List[ValueLabel]] = None
    schemeSubCategory: Optional[List[ValueLabel]] = None
    dbtScheme: Optional[bool] = None
    implementingAgency: Optional[str] = None
    tags: Optional[List[str]] = None
    schemeName: Optional[str] = None
    schemeShortTitle: Optional[str] = None
    level: Optional[ValueLabel] = None
    schemeCategory: Optional[List[SchemeCategory]] = None
    schemeFor: Optional[str] = None

class SchemeContent(BaseModel):
    references: Optional[List[Reference]] = None
    schemeImageUrl: Optional[str] = None
    briefDescription: Optional[str] = None
    detailedDescription: Optional[List[Dict[str, Any]]] = None
    benefitTypes: Optional[ValueLabel] = None
    benefits: Optional[List[Dict[str, Any]]] = None
    exclusions: Optional[List[Dict[str, Any]]] = None
    detailedDescription_md: Optional[str] = None

class ApplicationProcess(BaseModel):
    mode: Optional[str] = None
    url: Optional[str] = None
    process: Optional[List[Dict[str, Any]]] = None

class SchemeDefinition(BaseModel):
    name: Optional[str] = None
    definition: Optional[List[Dict[str, Any]]] = None
    source: Optional[str] = None

class EligibilityCriteria(BaseModel):
    eligibilityDescription_md: Optional[str] = None
    eligibilityDescription: Optional[List[Dict[str, Any]]] = None

class Scheme(BaseModel):
    slug: str
    basicDetails: Optional[BasicDetails] = None
    schemeContent: Optional[SchemeContent] = None
    applicationProcess: Optional[List[ApplicationProcess]] = None
    schemeDefinitions: Optional[List[SchemeDefinition]] = None
    eligibilityCriteria: Optional[EligibilityCriteria] = None
