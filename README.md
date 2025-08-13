# Stock Analyzer
This program uses technical indicators including Bollinger Bands and Relative Strength Index (RSI) to predict short-term price movements for a given stock.
By analyzing historical and real-time market data, it identifies potential buying or selling opportunities that can guide manual or automated trading decisions.

---
## Features
![Analysis](https://github.com/Qijie-Sun/Stock-Analyzer/blob/main/public/analysisS.png)
- Historical price chart: Shows price movements for a user selected stock throughout a user selected timeframe
- Bollinger Bands: Plotted alongside historical price for clear visuals
- RSI: Plotted in a separate chart to show past and current RSI value
- Trading Signals: Generated based on bollinger bands and plotted on historical price chart
- Stock Info: Includes metrics such as the EPS, PE Ratio, Revenue, Income, etc

## Technical Details
### Bollinger Bands
- Measure volatility based on the moving average and a multiple of a stock's standard deviation
- Middle band calculated based on a 20 day moving average
- Upper band calculated based on the moving average + 2 standard deviations
- Lower band calculated based on the moving average - 2 standard deviations
- Prices near upper band indicates overbought conditions while prices near lower band indicates oversold conditions

### RSI
- Measures the speed and change of price movements based on a stock's recent gains and losses
- Calculated based on the average gain and average loss over 20 days (100 - $\frac{100}{1 + RS}$ where RS = $\frac{\text{Average Gain}}{\text{Average Loss}}$)
- RSI above 70 indicates overbought conditions while RSI below 30 indicates oversold conditions

### Strategies/Drawbacks
- Bollinger Bands can be combined with RSI to identify strong oversold/overbought conditions for opportunities to enter or exit the market
- Using this program on index funds may be more effective than individual stocks as they reduce risk by reflecting the overall market
- Bollinger Bands and RSI can generate false signals and lead to premature trades
- Bollinger Bands and RSI do not consider other important factors like external conditions and statistics like the EPS

## Requirements
- Python 3.10+
- Libraries:
  - yfinance
  - pandas
  - numpy
  - matplotlib

## Potential Updates
- Additional stock metrics
- Pattern recognition/price prediction using machine learning or neural networks
- Market sentiment analysis based on news headlines
- Improved UI and error handling
- Flask or Django integration
