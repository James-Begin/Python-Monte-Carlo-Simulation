#all data from Yahoo Finance
import yfinance
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime
import statistics

#reference beginning-end dates
start = datetime.datetime(2013,6,1)
end = datetime.datetime(2023,6,1)
data = yfinance.download('SPY', start, end)
figure1 = plt.figure()
plt.title("SP500, 10 Years to Date")
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.plot(data['Adj Close'])
plt.show()

#difference the downloaded close prices
#determine past volatility using standard deviation
#this past volatility will be used to simulate future prices
returns = data['Adj Close'].pct_change()
vol = returns.std()

#simulate future prices using Monte-Carlo
#In this case, drawing from a normal distribution with mean=0 and the standard deviation=vol
iter = 10000
#store predicted prices in a dataframe
df = pd.DataFrame()
#initialize the first price value
lastprice = data['Adj Close'][-1]
#store final prices for analysis
finalprices = []

for i in range(iter):
    #Initialize a first simulated price
    prices = []
    #update current price using prior price and randomly drawn change
    price = lastprice * (1 + np.random.logistic(0, vol))
    prices.append(price)

    #simulate one year of returns
    for x in range(251):
        price = prices[x] * (1 + np.random.logistic(0, vol))
        prices.append(price)

    #store simulate prices
    df[i] = prices
    finalprices.append(prices[-1])

#plot simulated prices
figure2 = plt.figure()
plt.title("SP500, One Year Monte Carlo Simulated Prices")
plt.xlabel('Days')
plt.ylabel('Price (USD)')
plt.plot(df)
plt.show()

#plot histogram of final prices
figure3 = plt.figure()
plt.hist(finalprices,bins=100)
plt.axvline(x = (np.mean(finalprices)),
            ymin = 0, ymax = max(finalprices), linestyle = "--", color = 'red', label = 'Mean')
plt.axvline(x = (np.mean(finalprices) + statistics.stdev(finalprices)),
            ymin = 0, ymax = max(finalprices), linestyle = "--", color = 'black', label = '+1 STD')
plt.axvline(x = (np.mean(finalprices) - statistics.stdev(finalprices)),
            ymin = 0, ymax = max(finalprices), linestyle = "--", color = 'black', label = '-1 STD')
plt.title('Final Prices of Logistic Distributed Simulated S&P 500 Returns (10000)')
plt.xlabel('Final Prices')
plt.ylabel('# of Occurences')
plt.show()
