import requests
from typing import Optional, Dict


from modules.data_models import GenericRapidApiRequest, CompanyStatsResponse

def base_api_calls(rapidapi_conf: GenericRapidApiRequest, querystring: Optional[Dict]) -> dict:
    """
    Generic abstraction for rapid api calls.

    :param: rapidapi_conf: a ``GenericRapidApiRequest`` configuration for the company statistics endpoint (url, host and key)
    """
    headers = {
        "x-rapidapi-key": rapidapi_conf.key,
	    "x-rapidapi-host": rapidapi_conf.host
    }
    try:
        response = requests.get(rapidapi_conf.url, headers=headers, params=querystring)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise SystemExit(e)
    if response.status_code == 429:
        # 429 error code refers to when rapid api free call are exhausted
        raise requests.exceptions.RequestsWarning("Request was processed. Free tier calls are exhausted.")
    if response.status_code != 200:
        print(f"Generic error while requesting {headers} with {querystring}")
        raise    
    return response.json()



def get_key_statistics(symbol: str, rapidapi_conf: GenericRapidApiRequest) -> CompanyStatsResponse:
    """
    Get key statistics from RapidApi.

    :param: symbol: company symbol id as 'AAPL'
    :param: rapidapi_conf: a ``GenericRapidApiRequest`` configuration for the company statistics endpoint (url, host and key)

    :example:
        >>> from modules.api_abstractions import get_key_statistics
        >>> company_stats = get_key_statistics(symbol='AAPL', rapidapi_conf=ra_config)
    """
    
    api_resp = base_api_calls(rapidapi_conf=rapidapi_conf, querystring={"symbol": symbol})
    key_stats = api_resp["quoteSummary"]["result"][0]["defaultKeyStatistics"]
    validate_response = CompanyStatsResponse(
        symbol=symbol,
        float_shares=key_stats["floatShares"].get("raw", None),
        outstanding_shares=key_stats["sharesOutstanding"].get("raw", None),
        book_value =key_stats["bookValue"].get("raw", None),
        enterprise_revenue=key_stats["enterpriseToRevenue"].get("raw", None),
        enterprise_ebitda=key_stats["enterpriseToEbitda"].get("raw", None),
        start_date = "2025-02-15",
        end_date = "2199-12-31",
        entry_id=symbol+"20250215"
        )
    return key_stats
