import pandas as pd
import numpy as np
from same_day import rsi_same_day


def rsi_same_day_df(tickers: list[str],
                 buy_bellow: float,
                 sell_above: float,
                 rsi_period: 14,
                 start: str = '2026-01-01',
                 auto_adjust: bool = True) -> pd.DataFrame:
    dfs = []
    for ticker in tickers:
        try:
            df = rsi_same_day(ticker = ticker, buy_bellow = buy_bellow, sell_above = sell_above, rsi_period = rsi_period, start = start, auto_adjust = auto_adjust)
            dfs.append(df)
        except:
            df = pd.DataFrame({
                'ticker': [ticker],
                'date': [None],
                'price': [np.nan],
                'rsi': [np.nan],
                'signal': [np.nan]
            })
            dfs.append(df)
    dfs = pd.concat(dfs, ignore_index=True)
    dfs = dfs.sort_values(['rsi'])
    return dfs