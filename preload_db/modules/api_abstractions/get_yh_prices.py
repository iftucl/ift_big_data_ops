import requests
import json
from datetime import datetime

from modules.data_models.equity_prices_yh import YahooStockPrices

class CompanyPricesYahoo:
    def __init__(self, symbol_id: str, api_url: str, api_key: str, api_host: str):
        self.symbol_id = symbol_id
        self.api_url = api_url
        self.api_key = api_key
        self.api_host = api_host
        self.request = self._request()
        self.meta_data, self.stock_prices = self._parse_data()
        self.stock_prices = None
    
    def _build_query_string(self):
        return {"symbol": self.symbol_id, "interval": "1d", "diffandsplits": "false"}
    def _build_headers(self):
        built_headers = {
            "x-rapidapi-key": self.api_key,
            "x-rapidapi-host": self.api_host,
            }
        return built_headers
    def _request(self):
        try:
            return requests.get(self.api_url, headers=self._build_headers, params=self._build_query_string())
        except Exception as exc:
            print(f"error in retrieving prices for stock {self.company_id}")
            raise
    def _parse_data(self):
        response_data = self.request.json()
        return response_data.get("meta"), response_data.get("body")    
    def _prices(self):
        currency = self.meta_data.get("currency")
        symbol = self.meta_data.get("symbol")
        prices_dicts = self.stock_prices.get("body")
        output_list = list()
        for _, prices_dict in prices_dicts.items():
            daily_price = YahooStockPrices(**{**prices_dict, "symbol_id": symbol, "currency": currency})
            output_list.append(daily_price)
        return output_list
    @property
    def prices(self):
        return self.prices()


