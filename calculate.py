import pandas as pd
import numpy as np
from download_history import download_h
    
def compute_rsi(close: pd.Series, period: int = 14) -> pd.Series:
    gain = close.diff().clip(lower = 0.0)
    loss = close.diff().clip(upper = 0.0)

    avg_gain = gain.ewm(alpha = 1/period, adjust = False, min_periods = period).mean()
    avg_loss = loss.ewm(alpha = 1/period, adjust = False, min_periods = period).mean()
    rs = avg_gain / avg_loss.replace(0, np.nan)
    rsi = 100 - (100/(1+rs))

    return rsi.fillna(50.0)


def calculate_rsi(ticker: str,
                  buy_below: float = 30,
                  sell_above: float = 70,
                  rsi_period: int = 14,
                  start: str = '2026-01-01',
                  auto_adjust: bool = True,
                  multi_level_index = False):
    df = download_h(
        ticker = ticker,
        start = start,
        auto_adjust = auto_adjust,
        multi_level_index = multi_level_index 
    )

    df['RSI'] = compute_rsi(
        df['Close'],
        period = rsi_period
    )

    return df