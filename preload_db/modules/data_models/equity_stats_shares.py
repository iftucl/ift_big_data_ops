from pydantic import BaseModel, Field
from pydantic.functional_validators import field_validator, model_validator
from datetime import datetime
from typing import Any, Optional
from datetime import datetime, timezone

class CompanyStatsResponse(BaseModel):
    """
    Pydantic representation of the company_statistics response from rapid api.
    """
    symbol: str = Field(..., description="The ticker symbol of the company.")
    float_shares: Optional[int] = Field(description="The number of free-floating shares available for trading.")
    outstanding_shares: Optional[int] = Field(description="The total number of outstanding shares issued by the company.")
    book_value: Optional[float] = Field(description="The book value per share of the company.")
    enterprise_revenue: Optional[float] = Field(description="The enterprise value divided by revenue.")
    enterprise_ebitda: Optional[float] = Field(description="The enterprise value divided by EBITDA.")
    start_date: str = Field(description="The start date for financial data retrieval (stored as ISO 8601 string).")
    end_date: str = Field(description="The end date for financial data retrieval (stored as ISO 8601 string).")
    entry_id: str = Field(description=("Concatenates symbol and date to form primary key"))

    @field_validator("start_date", mode="before")
    @classmethod
    def set_start_date(cls, v: Any):
        if not v:
            dt_object = datetime.now(timezone.utc)
            return dt_object.strftime("%Y-%m-%d")
        try:
            date_format_check = datetime.strptime(v, "%Y-%m-%d")
            return date_format_check.strftime(date_format_check, "%Y-%m-%d")
        except ValueError:
            print("Could not convert to datetime object")
            raise
    @field_validator("end_date", mode="before")
    @classmethod
    def set_end_date(cls, v: Any):
        if not v:
            dt_object = datetime.now(timezone.utc)
            return dt_object.strftime("%Y-%m-%d")
        try:
            date_format_check = datetime.strptime(v, "%Y-%m-%d")
            return date_format_check.strftime(date_format_check, "%Y-%m-%d")
        except ValueError:
            print("Could not convert to datetime object")
            raise
    @model_validator(mode="after")    
    def create_id(self):
        try:            
            self.entry_id = self.start_date.replace("-", "") + self.symbol
            return self
        except ValueError:
            print(f"Could not create unique id {self.symbol}")
            raise
