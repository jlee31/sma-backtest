# Libraries

import pandas_datareader as pdr
import numpy as np
import datetime
import matplotlib.pyplot as plt
import yfinance as yf

# Variables

PERIOD = 200
STARTING_BAL = 10000

# Time Period

START_DATE = datetime.datetime(2005, 1,1)
END_DATE = datetime.datetime(2015, 1, 1)
YEARS = (END_DATE - START_DATE).days / 365.25

# Adding data to pandas dataframe 

# price = pdr.get_data_yahoo('^GSPC', START_DATE, END_DATE)
price = yf.download('^GSPC', start=START_DATE, end=END_DATE, multi_level_index=False)

# print(price.head())

# Drop the unnecessary
price = price.drop(columns=['High', 'Low', 'Volume']) 

# print(price.head())

# Plot the chart

plt.plot(price.Close)
# plt.show()

# Daily Return of SMP500
price['Return'] = price.Close / price.Open
price['Bench_Bal'] = STARTING_BAL * price.Return.cumprod()
print(price.tail())

plt.plot(price.Bench_Bal)
plt.show()

# Calculate metrics
bench_return = price.Bench_Bal[-1] / price.Bench_Bal[0] * 100

# Full Return Value
print(bench_return)

# CAGR Calculate Annual Growth Rate
rate = 1/YEARS
bench_cagr = round((((price.Bench_Bal[-1] / price.Bench_Bal[0]) ** rate) - 1) * 100, 2)
print(bench_cagr)

# Peak to Low (Drawdown) | Maximum Drop
price['Bench_Peak'] = price.Bench_Bal.cummax()

price['Bench_DD'] = price.Bench_Bal - price.Bench_Peak

print(price.tail())

bench_dd = round((price.Bench_DD / price.Bench_Peak).min(), 2)

print(bench_dd)


# Moving Average

price['SMA'] = price.Close.rolling(window = PERIOD).mean()

# Plotting Chart with Moving Average
plt.plot(price.Close)
plt.plot(price.SMA)
plt.show()

# creating entry signals
# long means whenever you are in the market - above the moving average

print(price.columns)
price['Long'] = price.Close > price.SMA

print(price.tail())

# Calculate Daily System Return
price['Sys_Ret'] = np.where(price.Long.shift(1) == True, price.Return, 1.0)
print(price.tail())

# Calculate System Balance
price['Sys_Bal'] = STARTING_BAL * price.Sys_Ret.cumprod()


plt.plot(price.Bench_Bal)
plt.plot(price.Sys_Bal)
plt.show()

# calculate  more metrics
sys_return = price.Sys_Bal[-1] / price.Sys_Bal[0] * 100
sys_cagr = round((((price.Sys_Bal[-1] / price.Sys_Bal[0]) ** rate) - 1) * 100, 2)

print(sys_return)
print(sys_cagr)

# drawdown

price['Sys_Peak'] = price.Sys_Bal.cummax()
price['Sys_DD'] = price.Sys_Bal - price.Sys_Peak

sys_dd = round((((price.Sys_DD / price.Sys_Peak).min()) * 100), 2)

print(sys_dd)

# Final Metrics and Data Analysis

print(f'Benchmark Total return: {bench_return}%')
print(f'Benchmark CAGR: {bench_cagr}')
print(f'Benchmark DD: {bench_dd}%')
print('')
print(f'System Total return: {sys_return}%')
print(f'System CAGR: {sys_cagr}')
print(f'System DD: {sys_dd}%')