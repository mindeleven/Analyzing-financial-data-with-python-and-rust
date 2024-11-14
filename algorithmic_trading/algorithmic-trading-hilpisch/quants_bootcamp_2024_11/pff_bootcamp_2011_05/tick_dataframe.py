#
# Simple Tick Data Collector
# (using pandas DataFrame objects)
#
import zmq
import datetime
import pandas as pd

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('tcp://127.0.0.1:5555')
socket.setsockopt_string(zmq.SUBSCRIBE, '')

data = pd.DataFrame()
while True:
    msg = socket.recv_string()
    t = datetime.datetime.now()
    print(msg)
    symbol, price = msg.split()
    df = pd.DataFrame({'symbol': symbol, 'price': float(price)}, index=[t])
    data = pd.concat((data, df))
