#
# Simple Tick Data Client
#
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('tcp://127.0.0.1:5555')
socket.setsockopt_string(zmq.SUBSCRIBE, 'MSFT')

while True:
    msg = socket.recv_string()
    print(msg)
