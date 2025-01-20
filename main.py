import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# get data for stock
def fetch_stock(ticker, period, interval):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period, interval=interval)
    return data

# calculate bollinger bands
def bollinger_bands(data, window):
    data['Moving Average'] = data['Close'].rolling(window=window).mean()
    data['Standard Deviation'] = data['Close'].rolling(window=window).std()
    data['Upper Band'] = data['Moving Average'] + (2 * data['Standard Deviation'])
    data['Lower Band'] = data['Moving Average'] - (2 * data['Standard Deviation'])
    return data

# calculate rsi
def rsi(data, window):
    delta = data['Close'].diff()

    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    data['RSI'] = rsi
    return data

# plot graph with bollinger bands and rsi values
def analysis(ticker):
    data = fetch_stock(ticker, period, interval)
    data = bollinger_bands(data, window)
    data = rsi(data, window)

    plt.figure(figsize=(14, 5))
    plt.plot(data['Close'], label='Close Price', color='blue', alpha=1)
