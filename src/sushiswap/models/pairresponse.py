from src.models.basemodel import BaseModel

from pydantic import Field


class PairResponse(BaseModel):
    t1_reserve: float = Field(..., alias="Token_1_reserve")
    t2_reserve: float = Field(..., alias="Token_2_reserve")

    @property
    def price(self) -> float:
        return round(self.t2_reserve / self.t1_reserve, 3)
