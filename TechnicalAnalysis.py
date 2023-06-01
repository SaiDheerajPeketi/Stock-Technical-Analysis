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
start = dt.date(2021,1,1)
end = dt.datetime.now
data = yf.download('TSLA')
data['SMA_100'] = ta.SMA(data['Close'],100)
data['EMA_100'] = ta.EMA(data['Close'],100)

# plt.plot(data['Close'])
# plt.plot(data['SMA_100'])
# plt.plot(data['EMA_100'])

#Relative Strength Indicator(RSI)
data['RSI'] = ta.RSI(data['Close'])
fig, axs = plt.subplots(2,1,gridspec_kw={"height_ratios" : [3,1]}, figsize=(10,6))
axs[0].plot(data['Close'])
axs[0].plot(data['SMA_100'])
axs[0].plot(data['EMA_100'])
axs[1].axhline(y=70,color='r',linestyle = '--')
axs[1].axhline(y=30,color='g',linestyle = '--')
axs[1].plot(data['RSI'])



plt.show()

print(data)