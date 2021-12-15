from socket import *

HOST = '127.0.0.1'  # server IP
PORT = 49000  # server port
ADDR = (HOST, PORT)
BUFSIZE = 1024

with socket(AF_INET, SOCK_STREAM) as sock:
    sock.connect(ADDR)
    sock.send(b'Hi server')  # bytestring
    data = sock.recv(BUFSIZE).decode()

print(f'Received {data}')
