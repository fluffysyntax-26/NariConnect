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
    state: Optional[Any] = None
    nodalMinistryName: Optional[Any] = None
    nodalDepartmentName: Optional[Any] = None
    otherMinistryName: Optional[Any] = None
    otherDepartmentNames: Optional[Any] = None
    targetBeneficiaries: Optional[List[Any]] = None
    schemeSubCategory: Optional[List[Any]] = None
    dbtScheme: Optional[bool] = None
    implementingAgency: Optional[str] = None
    tags: Optional[List[str]] = None
    schemeName: Optional[str] = None
    schemeShortTitle: Optional[str] = None
    level: Optional[Any] = None
    schemeCategory: Optional[List[Any]] = None
    schemeFor: Optional[str] = None


class SchemeContent(BaseModel):
    references: Optional[List[Any]] = None
    schemeImageUrl: Optional[str] = None
    briefDescription: Optional[str] = None
    detailedDescription: Optional[List[Any]] = None
    benefitTypes: Optional[Any] = None
    benefits: Optional[List[Any]] = None
    exclusions: Optional[List[Any]] = None
    detailedDescription_md: Optional[str] = None


class ApplicationProcess(BaseModel):
    mode: Optional[str] = None
    url: Optional[str] = None
    process: Optional[List[Any]] = None


class SchemeDefinition(BaseModel):
    name: Optional[str] = None
    definition: Optional[List[Any]] = None
    source: Optional[str] = None


class EligibilityCriteria(BaseModel):
    eligibilityDescription_md: Optional[str] = None
    eligibilityDescription: Optional[List[Any]] = None


class Scheme(BaseModel):
    slug: str
    basicDetails: Optional[BasicDetails] = None
    schemeContent: Optional[SchemeContent] = None
    applicationProcess: Optional[List[ApplicationProcess]] = None
    schemeDefinitions: Optional[List[SchemeDefinition]] = None
    eligibilityCriteria: Optional[EligibilityCriteria] = None
