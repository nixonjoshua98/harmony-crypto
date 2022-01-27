from .basemodel import BaseModel
from pydantic import Field


class ContractDataFile(BaseModel):
    name: str = Field(..., alias="contractName")
    address: str = Field(..., alias="address")
    abi: list[dict] = Field(..., alias="abi")
