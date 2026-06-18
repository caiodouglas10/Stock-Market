import yfinance as yf
import pandas as pd

def download_h(ticker: str, start: str = '2026-01-01', end: str | None = None,
    auto_adjust: bool = True, multi_level_index: bool = False) -> pd.DataFrame:
    df = yf.download(ticker,
        start = start,
        end = end,
        auto_adjust = auto_adjust,
        progress = False, 
        threads = True,
        multi_level_index = multi_level_index)
    if df.empty:
        raise ValueError(f'No data price returned for {ticker}')
    return df

   # progress: bool = False, threads: bool = True, | ticker=tricker