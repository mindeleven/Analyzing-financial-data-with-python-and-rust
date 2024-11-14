#
# Simple Tick Data Collector
#
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('tcp://127.0.0.1:5555')
socket.setsockopt_string(zmq.SUBSCRIBE, '')

raw = list()
while True:
    msg = socket.recv_string()
    print(msg)
    symbol, price = msg.split()
    raw.append((symbol, float(price)))
