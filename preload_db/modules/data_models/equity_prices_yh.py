from pydantic import BaseModel, Field
from pydantic.functional_validators import field_validator, model_validator
from typing import Optional, Any
from datetime import datetime, timezone

class YahooStockPrices(BaseModel):
    price_id: Optional[str] = None
    open_price: float = Field(alias="open")
    close_price: float = Field(alias="close")
    volume: float
    currency: str
    cob_date: str = Field(alias="date_utc")
    symbol_id: str
    @field_validator("cob_date", mode="before")
    @classmethod
    def serialise_date_string(cls, v: Any):
        try:
            dt_object = datetime.fromtimestamp(v, tz=timezone.utc)
            return dt_object.strftime("%Y-%m-%d")
        except ValueError:
            print("Could not convert to datetime object")
            raise
    @model_validator(mode="after")    
    def create_price_id(self):
        try:            
            self.price_id = self.cob_date.replace("-", "") + self.symbol_id
            return self
        except ValueError:
            print(f"Could not create unique id {self.symbol_id}")
            raise


