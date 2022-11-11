import json

import pandas as pd
import requests
from requests import Response


def get_check_for_calls() -> pd.DataFrame:
    r: Response = requests.get('http://localhost:5000/table/check_for_calls?send_mail=false')
    dikt: dict = json.loads(r.content)
    df: pd.DataFrame = pd.DataFrame(dikt).sort_values("factor", ascending=False)
    return df
