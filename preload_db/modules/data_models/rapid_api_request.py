from pydantic import BaseModel, HttpUrl, Field, AfterValidator
from pydantic.networks import UrlConstraints
from typing_extensions import Annotated, TypeAlias

def check_rapidapi_hosts(host: str) -> str:
    if host.endswith("p.rapidapi.com"):
        return host
    raise ValueError("It's not in the list of accepted hosts")

AcceptedUrl: TypeAlias = Annotated[str, AfterValidator(check_rapidapi_hosts)]

class GenericRapidApiRequest(BaseModel):
    """
    :example:
        >>> from modules.data_models.rapid_api_request import GenericRapidApiRequest
        >>> GenericRapidApiRequest(url="https://yahoo-finance166.p.rapidapi.com/api/stock/get-statistics", key="jafsdlkhfn;fas", host="my.host.p.rapidapi.com")
    """
    url: HttpUrl = Field(..., description="extensive url with api endpoint")
    key: str = Field(..., description="RapidAPI Key for requests")
    host: AcceptedUrl = Field(..., description="rapid api host name. must end with p.rapidapi.com")

