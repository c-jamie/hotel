import datetime as dt
import os
from pathlib import Path

import pandas as pd


def build_dates():
    date_rng = pd.date_range(
        dt.date.today() + dt.timedelta(60), freq="W-SAT", periods=35
    )
    date_1 = date_rng[::1]
    date_2 = date_rng[1::1]
    return list(zip(date_1, date_2))


BASE = Path(os.path.dirname(os.path.abspath(__file__)))
