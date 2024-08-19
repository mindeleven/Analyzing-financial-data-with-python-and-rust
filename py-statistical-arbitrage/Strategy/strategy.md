# StatBot Strategy

Strategy for building a trading bot that accesses the ByBit API as outlined by Shaun McDonogh in his [Statistical Arbitrage Bot Build course](https://www.udemy.com/course/statistical-arbitrage-bot-build-in-crypto-with-python-a-z/learn/lecture/31161520#overview) on Udemy.

## StatBot - Gameplan

The StatBot needs to follow a **gameplan** that tells us which logic we're going to implement in the strategy and execution section.

<font size="4" style="line-height:1.3">**Definition from [CoinDesk](https://www.coindesk.com/learn/what-is-a-perpetual-swap-contract/):** Derivatives are financial instruments that derive their value from an underlying asset. Like other types of derivatives, including futures and options, perpetual swaps provide a means to speculate on the value of assets while the contract is held.</font>

## Strategy

The strategy we're looking for will allow us to search for all the possible cryptos that we can go long and short on on Bybit within their perpetual derivatives contract.  

Next we're going to filter through all the cryptos we found and our goal is to find what pairs or cointegrated. This data will be saved as a spreadsheet that can be opened with Google Sheets or Excel.  

This spreadsheet should tell us what are the best looking code integrated pairs on both hourly data or daily data are.

## Coding Step (1) - Get Tradable Symbols

- Connect to the ByBit API

- Ask Bybit for all the available tickers, assets or tradable symbols

## Coding Step (2) - Get The Price History

- Get the price history for all of those symbols

## Coding Step (4) - Analyze findings (Spread/ZScore)

- After cointegration calculation, analyze the findings using spread and Z-score

- Calculate the spread and the Z-score

- Visualize findings in a chart

- Apply a filter that tells you how often the spread crosses the zero line

## Coding Step (5) - Excel Back Test

- Testing the cointegrated pairs with Excel

- Next step will be the execution of StatBotOne



