from modules.data_models import CompanyStatsResponse, GenericRapidApiRequest
from modules.api_abstractions.send_api_request import base_api_calls

def get_key_statisticts(symbol: str, rapidapi_conf: GenericRapidApiRequest) -> CompanyStatsResponse:
    """
    Get key statistics from RapidApi.

    :param: symbol: company symbol id as 'AAPL'
    :param: rapidapi_conf: a ``GenericRapidApiRequest`` configuration for the company statistics endpoint (url, host and key)
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
