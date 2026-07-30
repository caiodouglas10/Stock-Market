import streamlit as st
from same_day_df import rsi_same_day_df
from backtesting import ma_strategy

tab1, tab2 = st.tabs(["RSI", "MA_STRATEGY"])

ticker = st.sidebar.text_input('Ticker', value='BRAP4.SA')
ma_short_button = st.sidebar.number_input('MA SHORT', min_value=1, max_value=100, value=9, step=1)
ma_long_button = st.sidebar.number_input('MA LONG', min_value=50, max_value=300, value=72, step=1)

with tab1:
    st.title('Acompanhamento Financeiro - Tabela RSI')
    st.write('Indicadores técnicos de valores de mercado')
    tk = ['CMIG4.SA', 'SAPR11.SA', 'AAPL', 'ITUB4.SA', 'PETR4.SA']

    df = rsi_same_day_df(tickers = tk,
                    buy_bellow= 30,
                    sell_above= 70,
                    rsi_period= 14,
                    start = '2026-01-01',
                    auto_adjust= True)

    st.dataframe(df, width="stretch")

with tab2:
    st.title(f'MA Strategy para {ticker}')
    st.write('Acompanhamento de médias móveis para valores de mercado')

    df = ma_strategy(ticker=ticker, sh_window=ma_short_button, lo_window=ma_long_button)

    st.dataframe(df, width="stretch")
