import pandas as pd
import vectorbt as vbt

def ma_strategy(ticker: str, 
                sh_window: int = 9, 
                lo_window: int = 72, start_date: str ='2021-01-01') -> pd.DataFrame:
    price = (vbt.YFData
            .download(ticker)
            .get('Close').loc[start_date:])

    mas = vbt.MA.run(price, window=sh_window)
    mal = vbt.MA.run(price, window=lo_window)

    entries = mas.ma_crossed_above(mal)
    exits = mas.ma_crossed_below(mal)

    portifolio = vbt.Portfolio.from_signals(close=price, 
                                            entries=entries, 
                                            exits=exits, 
                                            init_cash=10_000, 
                                            fees=0.001,
                                            slippage=0.001)
    df = portifolio.stats().to_frame("Value")
    return df
