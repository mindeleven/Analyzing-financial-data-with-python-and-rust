#
# Simple Tick Data Server
#
import zmq
import time
import random

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://127.0.0.1:5555')

AAPL = 100.
MSFT = 100.

while True:
    if random.random() > 0.45:
        AAPL += random.gauss(0, 1) / 2
        msg = f'AAPL {AAPL:.3f}'
    else:
        MSFT += random.gauss(0, 1) / 2
        msg = f'MSFT {MSFT:.3f}'
    socket.send_string(msg)
    print(msg)
    time.sleep(random.random() * 2)
