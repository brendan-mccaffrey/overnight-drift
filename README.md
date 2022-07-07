# Overnight Drift

This was a quick codebase formed in response to a stunning paper: [Night Moves](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4139328)

Essentially, the paper analyzed the concept of *Overnight Drift*, how a majority of stock gains happen when the market is closed. The paper's findings can be summarized as follows:

> The overnight effect refers to the fact that, over at least the past three decades, investors have earned 100% or more of the return on a wide range of risky assets when the markets are closed, and, as sure as day follows night, have earned zero or negative returns for bearing the risk of owning those assets during the daytime, when markets are open. The effect is seen over a wide range of assets, including the broad stock market, individual stocks (particularly those popular with retail investors, and Meme stocks most of all), many ETFs, and cryptocurrencies.

## Files

Forgive me for the poorly organized codebase, but quick overview of the scripts:

- `main.py` | Entrypoint: Define assets, pull data, chart data, supports crypto from FTX and stocks from Yahoo Finance
- `ftx.py` | Pulls and processes data from FTX. At 15 min interval (needed to get open - no 30 min interval available), FTX caps results around 10 days, so the script makes subsequent queries, combines them, extracts 'open' and 'close' price - 9:30 am and 4 pm Eastern, and compiles to single pandas df.
- `yahoo.py` | Pulls data from yahoo finance - doesn't require processing to the same extent as FTX data for obvious reasons.
- `manager.py` | Helper functions including saving and pulling pickle files.

## Results

In the long run, tx costs greatly affect the performance of the strategy. There is still potential for a strategy here, but you must face the following questions.

- How can you reduce tx cost?
- On which assets/asset classes is the strategy most performant (given your current view of market environment)?
- Can you generate intraday yield on idle capital (particularly, enough to cover tx cost)?

This will be my last commit to this public repo - further work will remain private.

## Charts

### Stocks

![](/charts/arkk.png)  |  ![](/charts/arkw.png)
:-------------------------:|:-------------------------:
![](/charts/crsp.png)  |  ![](/charts/tsm.png)
![](/charts/bci.png)  |  ![](/charts/grain.png)
![](/charts/mp.png)  |  ![](/charts/pll.png)
![](/charts/copper.png)  |  ![](/charts/steel.png)

## Explanation

There are many explanations for why overnight drift exists (see paper linked at top), but I'm not satisfied with them. Especially because the effect exists in crypto markets...

I have some theories, but open to thoughts. If you want to offer an explanation feel free to contact me *brendan*`at`*undefined*`dot`*xyz*



