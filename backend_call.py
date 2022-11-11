import json

import pandas as pd
import requests
from requests import Response

host = "http://localhost:5000"


def get_check_for_calls() -> pd.DataFrame:
    r: Response = requests.get(f'{host}/table/check_for_calls?send_mail=false')
    dikt: dict = json.loads(r.content)
    df: pd.DataFrame = pd.DataFrame(dikt).sort_values("factor", ascending=False)
    return df


def get_update_after_call(name: str) -> None:
    r: Response = requests.get(f'{host}/update_after_call?name={name}&days_since_last=0')
