from api.oanda_api import OandaApi

from infrastructure.instrument_collection import instrumentCollection
from simulation.ma_cross import run_ma_sim

if __name__ == '__main__':
   api = OandaApi()

   #data = api.get_account_summary()
   #print(data)

   # instrumentCollection.CreateFile(api.get_account_instruments(), '../data')
   # instrumentCollection.LoadInstruments("../data")
   # instrumentCollection.PrintInstruments()
   
   run_ma_sim(curr_list=["EUR", "USD", "GBP", "JPY", "AUD", "CAD"])

   