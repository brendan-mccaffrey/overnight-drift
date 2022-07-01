# Overnight Drift

This was a quick codebase formed in response to a stunning paper: [Night Moves](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4139328)

Essentially, the paper analyzed the concept of *Overnight Drift*, how a majority of stock gains happen when the market is closed. The paper's findings can be summarized as follows:

> The overnight effect refers to the fact that, over at least the past three decades, investors have earned 100% or more of the return on a wide range of risky assets when the markets are closed, and, as sure as day follows night, have earned zero or negative returns for bearing the risk of owning those assets during the daytime, when markets are open. The effect is seen over a wide range of assets, including the broad stock market, individual stocks (particularly those popular with retail investors, and Meme stocks most of all), many ETFs, and cryptocurrencies.



## Results

Including tx costs greatly harms performance.

### Stocks

![](/assets/stocks/snp.png)  |  ![](/assets/stocks/nasdaq.png)
:-------------------------:|:-------------------------:
![](/assets/stocks/dow.png)  |  ![](/assets/stocks/gold.png)
![](/assets/stocks/energy.png)  |  ![](/assets/stocks/healthcare.png)
![](/assets/stocks/water.png)  |  ![](/assets/stocks/energy.png)

### Crypto

![](/assets/crypto/btc.png)  |  ![](/assets/crypto/eth.png)
:-------------------------:|:-------------------------:
![](/assets/crypto/sol.png)  |  ![](/assets/crypto/matic.png)
![](/assets/crypto/mkr.png)  

## Remaining Questions

I should better model costs to follow a half-cent fee (interactive brokers) per share - percentage of which is dependent on share price.

What if you were to deploy capital intraday and effectively earn the 0.001% fee? Hmmm

I should probably check specific intervals so that for nasdaq, djia and s&p the results arent so blurred by 30 years of money printing / only up environment.

