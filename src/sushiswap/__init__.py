import requests
from typing import Optional
import contextlib
from . import tickers
from .models import PairResponse, TickerModel


BASE_URL = "https://api2.sushipro.io?action=get_pair"


def get_pair(ticker: TickerModel) -> Optional[PairResponse]:
    """
    Get pair information from the Sushiswap API
    :param ticker: Model containing the required query data
    :return:
        Return the API response as a model
    """
    url = f"{BASE_URL}&chainID={ticker.chain_id}&pair={ticker.address}"

    r = requests.get(url)

    return _get_request_response(r)


def _get_request_response(r: requests.Response) -> Optional[PairResponse]:

    if r.status_code == 200:
        with contextlib.suppress(Exception):
            data: dict = r.json()[0]

            return PairResponse.parse_obj(data)
