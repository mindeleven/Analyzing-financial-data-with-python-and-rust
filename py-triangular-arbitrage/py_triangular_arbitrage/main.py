'''
The Poloniex API has changed very much since the course got published so I'm working with
Shaun McDonogh's GitHub repo here (https://github.com/CryptoWizardsNet/poloniex-triarb-new).
As it turns out the repo isn't up to date either because the API got modified once again.
We learn by trial and error. That's what they say.
'''
import func_arbitrage
import json
import time

# Setting url variables
# Matrket prices: get latest trade price for all symbols
coins_url = "https://api.poloniex.com/markets/price"
# Ticker: retrieve ticker in last 24 hours for all symbols
coin_price_url = "https://api.poloniex.com/markets/ticker24h"

"""
    Step 0: Finding coins which can be traded
    Exchange: Poloniex
    https://api-docs.poloniex.com/spot
    Poloniex Market Data: https://api-docs.poloniex.com/spot/api/public/market-data
"""

def step_0():

    # extract list of coins and prices from Exchange
    coin_json = func_arbitrage.get_coin_tickers(coins_url)

    # loop through each objects and find the tradeable pairs
    # all pairs seem to be tradeable with the current API
    # we still use the functin in case we've to add a filter later on
    coin_list = func_arbitrage.collect_tradeables(coin_json)

    # return list of tradeable coins
    return coin_list

""" 
    Step 1: Structuring Triangular Pairs
    Calculation Only
    Taking the list from Step 0 and doing a calculation on it
"""
def step_1(coin_list):

    # Structure the list of tradeable triangular arbitrage pairs
    structured_list = func_arbitrage.structure_triangular_pairs(coin_list)

    # Save structured list
    with open("./assets/data/json/structured_triangular_pairs.json", "w") as fp:
        json.dump(structured_list, fp)


""" MAIN """
if __name__ == "__main__":
    print("+ + + + + Step 0: Finding coins which can be traded + + + + +")
    coin_list = step_0()
    print(f"+ + + + + Retrieving list of cryptos... {len(coin_list)}       + + + + +")
    print(coin_list)

    print("+ + + + + Step 1: Structuring Triangular Pairs      + + + + +")
    structured_pairs = step_1(coin_list)
    print("+ + + + + Structuring cryptos into triangular pairs + + + + +")
'''
    print("Structuring cryptos into triangular pairs (2 mins)...")
    structured_pairs = step_1(coin_list)

    print("Running scanning algorithm (will run until killed)...")
    while True:
        time.sleep(1)
        step_2()
'''