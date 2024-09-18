from genericpath import isfile
import pandas as pd
import os.path
from datetime import datetime
# extend path to import modules from other folders
import sys
# append everything above the level where we're now
sys.path.append("../")
from infrastructure.instrument_collection import instrumentCollection as ic

class MAResult:
    def __init__(self, df_trades, pairname, ma_l, ma_s, granularity):
        self.df_trades = df_trades
        self.pairname = pairname
        self.ma_l = ma_l
        self.ma_s = ma_s
        self.granularity = granularity
        self.result = self.result_obj()

    def __repr__(self):
        return str(self.result)
    
    def result_obj(self):
        return dict(
            pair = self.pairname,
            num_trades = self.df_trades.shape[0],
            total_gain = int(self.df_trades.GAIN.sum()),
            mean_gain = int(self.df_trades.GAIN.mean()),
            min_gain = int(self.df_trades.GAIN.min()),
            max_gain = int(self.df_trades.GAIN.max()),
            ma_l = self.ma_l,
            ma_s = self.ma_s,
            cross = f"{self.ma_s}_{self.ma_l}",
            granularity = self.granularity
        )

BUY = 1
SELL = -1
NONE = 0
get_ma_col = lambda x: f"MA_{x}"
add_cross = lambda x: f"{x.ma_s}_{x.ma_l}"

def is_trade(row):
    if row.DELTA >= 0 and row.DELTA_PREV < 0:
        return BUY
    elif row.DELTA < 0 and row.DELTA_PREV >= 0:
        return SELL
    return NONE

def load_price_data(pair, granularity, ma_list):
    # load the data frame for pair and granularity granularity
    df = pd.read_pickle(f"../assets/data/{pair}_{granularity}.pkl")
    # calculate moving averages
    for ma in ma_list:
        df[get_ma_col(ma)] = df.mid_c.rolling(window=ma).mean()
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

def get_trades(df_analysis, instrument, granularity):
    df_trades = df_analysis[df_analysis.TRADE != NONE].copy()
    df_trades["DIFF"] = df_trades.mid_c.diff().shift(-1)
    df_trades.fillna(0, inplace=True)
    df_trades["GAIN"] = df_trades.DIFF / instrument.pipLocation
    df_trades["GAIN"] = df_trades["GAIN"] * df_trades["TRADE"]
    df_trades["granularity"] = granularity
    df_trades["pair"] = instrument.name
    # adding cumulative sum of the gains
    df_trades["GAIN_C"] = df_trades["GAIN"].cumsum()
    # total_gain = df_trades["GAIN"].sum()
    # return dict(total_gain=int(total_gain), df_trades=df_trades)
    return df_trades

def assess_pair(price_data, ma_l, ma_s, instrument, granularity):
    df_analysis = price_data.copy()
    df_analysis["DELTA"] = df_analysis[ma_s] - df_analysis[ma_l]
    df_analysis["DELTA_PREV"] = df_analysis["DELTA"].shift(1)
    df_analysis["TRADE"] = df_analysis.apply(is_trade, axis=1)
    # print(instrument.name, ma_l, ma_s)
    # print(df_analysis.head(3))
    # return get_trades(df_analysis, instrument)
    df_trades = get_trades(df_analysis, instrument, granularity)
    df_trades["ma_l"] = ma_l
    df_trades["ma_s"] = ma_s
    df_trades["cross"] = df_trades.apply(add_cross, axis=1)

    return MAResult(
        df_trades,
        instrument.name,
        ma_l,
        ma_s,
        granularity
    )

def append_df_to_file(df, filename):
    # append data if file exists
    # create new file if it doesn't exist
    if os.path.isfile(filename):
        fd = pd.read_pickle(filename)
        df = pd.concat([fd, df])
    
    # reset index after concatination to avoid having 
    # duplicate indeces
    df.reset_index(inplace=True, drop=True)
    df.to_pickle(filename)

    print('################# NEW FILE ###################')
    print(filename, df.shape)
    print(df.tail(2))

def get_fullname(filepath, filename):
    return f"{filepath}/{filename}.pkl"

def process_macro(results_list, filename):
    # putting results list into data frame
    rl = [x.result for x in results_list]
    df = pd.DataFrame.from_dict(rl)
    # append dataframe to file
    append_df_to_file(df, filename)

def process_trades(results_list, filename):
    # concatenate list of data frames
    df = pd.concat([x.df_trades for x in results_list])
    append_df_to_file(df, filename)

def process_results(results_list, filepath):
    # add date and time to filename 
    # otherwise new results will be appended to alread existing file
    #current_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    current_time = datetime.now().strftime("%Y-%m-%d-%H")
    process_macro(results_list, get_fullname(filepath, current_time+'-ma_res'))
    process_trades(results_list, get_fullname(filepath, current_time+'-ma_trades'))
    # putting results list into data frame
    # rl = [x.result for x in results_list]
    # df = pd.DataFrame.from_dict(rl)
    # single data frame for each of the results that gets tested
    # print(df)
    # print(results_list[0].df_trades.head(2))
    # continiously append results to same file

def analyse_pair(instrument, granularity, ma_long, ma_short, filepath):
    
    ma_list = set(ma_long + ma_short)
    pair = instrument.name

    # load price data
    price_data = load_price_data(pair, granularity, ma_list)
    # print(pair)
    # print(price_data.head(3))

    # saving the results list
    results_list = []


    # assess a pair
    for ma_l in ma_long:
        for ma_s in ma_short:
            if ma_l <= ma_s:
                continue

            ma_result = assess_pair(
                price_data,
                get_ma_col(ma_l),
                get_ma_col(ma_s),
                instrument,
                granularity
            )
            # tg = result['total_gain']
            # nt = result['df_trades'].shape[0] # rows are first item of shape tuple
            # print(f"{pair} {granularity} {ma_s}-{ma_l} num-trades: {nt} tot-gain: {tg}")   
            print(ma_result)
            results_list.append(ma_result)
    
    # create df
    process_results(results_list, filepath)


def run_ma_sim(
    curr_list=["EUR", "USD", "AUD", "GBP"],
    granularity=["H1", "H4"],
    ma_long=[20, 40, 80, 120, 150],
    ma_short=[10, 20, 30, 40],
    filepath="../assets/data"
):
    ic.LoadInstruments("../assets/data")
    for g in granularity:
        for p1 in curr_list:
            for p2 in curr_list:
                pair = f"{p1}_{p2}"
                # check if pait in currency list
                if pair in ic.instruments_dict.keys():
                    analyse_pair(ic.instruments_dict[pair], g, ma_long, ma_short, filepath)