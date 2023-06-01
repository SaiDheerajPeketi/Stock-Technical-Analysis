#https://www.youtube.com/watch?v=N9NqTp_D_bw
import datetime as dt
import talib as ta
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as web
import yfinance as yf

#data = web.DataReader("TSLA","yahoo")
#data = yf.download(STOCK TICKER,START,END)
#START/END = 'YYYY-MM-DD'
data = yf.download('TSLA')
data['SMA_100'] = ta.SMA(data['Close'],100)
data['EMA_100'] = ta.EMA(data['Close'],100)

plt.plot(data['Close'])
plt.plot(data['SMA_100'])
plt.plot(data['EMA_100'])

plt.show()

print(data)