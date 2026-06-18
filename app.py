import streamlit as st
from same_df import rsi_same_day_df

st.title('Acompanhamento Financeiro - Bolsas')

tk = ['CMIG4.SA', 'SAPR11.SA', 'AAPL', 'ITUB4.SA', 'PETR4.SA']

df = rsi_same_day_df(tickers = tk,
                 buy_bellow= 30,
                 sell_above= 70,
                 rsi_period= 14,
                 start = '2026-01-01',
                 auto_adjust= True)

st.dataframe(df, width="stretch")
    
