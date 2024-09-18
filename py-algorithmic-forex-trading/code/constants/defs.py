import pandas as pd

account_data = pd.read_csv("~/Documents/temp/oanda/testnet_key.txt", sep=" ", header=None)

API_KEY = account_data[0][2]
ACCOUNT_ID = account_data[0][1]
OANDA_URL = account_data[0][0]