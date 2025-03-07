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

# recommendation based on current price
def action(data):
    latest = data.iloc[-1]
    if latest['Close'] <= latest['Lower Band']:
        if latest['RSI'] <= 30:
            return 'Strong Buy'
        return 'Buy'
    elif latest['Close'] >= latest['Upper Band']:
        if latest['RSI'] >= 70:
            return 'Strong Sell'
        return 'Sell'
    else:
        return 'Hold'

# plot graph with bollinger bands and rsi values
def analysis(ticker):
    data = fetch_stock(ticker, period, interval)
    data = bollinger_bands(data, window)
    data = rsi(data, window)

    # graph for closing price and bollinger bands
    plt.figure(figsize=(14, 5))
    plt.plot(data['Close'], label='Close Price', color='blue', alpha=1)
    plt.plot(data['Moving Average'], label='Moving Average', color='orange', alpha=0.6, linestyle='--')
    plt.plot(data['Upper Band'], label='Upper Band', color='red', alpha=0.8)
    plt.plot(data['Lower Band'], label='Lower Band', color='green', alpha=0.8)
    plt.fill_between(data.index, data['Upper Band'], data['Lower Band'], color='gray', alpha=0.2)

    plt.title(f'Stock Analysis - {ticker}\n', fontweight='bold')
    plt.text(0.512, 0.9, f'Recommendation: {action(data)}', fontsize=10, ha='center', transform=plt.gcf().transFigure)
    plt.xlim(data.index.min() - pd.Timedelta(days=10), data.index.max() + pd.Timedelta(days=10))
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid()
    plt.show()

    print('')

    # graph for rsi values
    plt.figure(figsize=(14, 2))
    plt.plot(data['RSI'], label='RSI', color='dimgray', alpha=1)
    plt.axhline(y=70, label='70', color='red', alpha=0.8)
    plt.axhline(y=30, label='30', color='green', alpha=0.8)

    plt.title(f'RSI')
    plt.xlabel('Date')
    plt.ylabel('RSI')
    plt.legend()
    plt.grid()
    plt.show()

ticker = input('Enter stock ticker (e.g. AAPL): ').upper()
period = input('Enter time period (3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max): ')
interval = '1d'
window = 20
analysis(ticker)
