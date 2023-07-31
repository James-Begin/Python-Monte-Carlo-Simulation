# Python-Monte-Carlo-Simulation
Monte Carlo simulations are a powerful computational technique used to estimate and analyze complex systems or processes that involve random variables. It relies on repeated random sampling to obtain numerical results, making it suitable for problems that are difficult or impossible to solve analytically. Monte Carlo simulation is particularly useful in scenarios where there are multiple uncertain variables interacting with each other, leading to complex and unpredictable outcomes. By repeating the simulation with different random inputs, it provides a distribution of possible results, offering a comprehensive understanding of the system's behavior and aiding in making better-informed decisions. One specific scenario is finance. Financial markets are inherently uncertain, and numerous factors influence their behavior. Monte Carlo simulation allows one to incorporate this uncertainty by using random sampling of input variables, such as interest rates, asset returns, and economic indicators, to model a wide range of possible scenarios.
## The Process
In this case, the simulation will be applied to the S&P 500 to generate one year (252 trading days) of returns. The reason for this is that the S&P represents the broader market and is less subject to volatility in any specific equity which can help improve the accuracy of our model considering the predictions are drawn from a normal distribution (for now).   
  
![myplot1](https://github.com/James-Begin/Python-Monte-Carlo-Simulation/assets/103123677/a505b31a-49d3-430d-8c5c-1e6ea7c640e4)  
*Historical Price of the S&P 500 Index from 2013 to 2023*  

Generating a Monte Carlo Simulation in Python can be done in only a few lines of code. First acquire the financial data you want to simulate (SPY in our case):  
```
import yfinance
start = datetime.datetime(2013,6,1)
end = datetime.datetime(2023,6,1)
data = yfinance.download('SPY', start, end)
```
Next, calculate the past volatility using NumPy's standard deviation function. This standard deviation will be used in our distribution.  
```
returns = data['Adj Close'].pct_change()
vol = returns.std()
```
Next intialize the first generated value:  
```
lastprice = data['Adj Close'][-1]
prices = []
price = lastprice * (1 + np.random.normal(0, vol))
prices.append(price)
```
Finally, generate the next years worth of daily close prices:  
```
for x in range(251):
  price = prices[x] * (1 + np.random.normal(0, vol))
  prices.append(price)
```
Here is an example of a single year of generated prices:  
![myplot2](https://github.com/James-Begin/Python-Monte-Carlo-Simulation/assets/103123677/53d7f0e6-d78d-4025-bffa-5a9761026a0e)  
  
However, one simulation is not very useful. Instead, we can generate many different years of simulated prices to view a wide variety of results:  
![myplot3](https://github.com/James-Begin/Python-Monte-Carlo-Simulation/assets/103123677/00e12819-262b-428f-a89e-e121bbc2cbc3)  
*10 different years of simulated prices of the S&P 500*  
  
![myplot4](https://github.com/James-Begin/Python-Monte-Carlo-Simulation/assets/103123677/e8f55e49-17d4-4b6e-afad-b41b69076a22)  
*100 different years of simulated prices of the S&P 500*  
  
![myplot5](https://github.com/James-Begin/Python-Monte-Carlo-Simulation/assets/103123677/20e658d5-064d-402a-be0d-15e529218c27)  
*1000 different years of simulated prices of the S&P 500*  
