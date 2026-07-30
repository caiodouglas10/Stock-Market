from download_history import download_h
download_h('1TUB4-SA')
from calculate_rsi import calculate_rsi
rsi = calculate_rsi('1TUB4.SA',)

from same import rsi_same_day
rsi_same_day(ticker = 'CMIG4.SA', buy_bellow = 35, sell_above = 70, rsi_period = 14, start = '2026-01-01', auto_adjust = True)