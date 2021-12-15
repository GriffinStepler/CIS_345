# Griffin Stepler, CIS345, iCourse, PE11
from socket import *
from time import ctime

# set constants
HOST = gethostbyname(gethostname())
# HOST = 'localhost'  # used for testing
PORT = 49002
ADDR = (HOST, PORT)
BUFSIZE = 1024
count = 0

# create socket and bind
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(ADDR)
sock.listen(5)
print(f'Server online. Listening on {ADDR}')

while True:
    # connect to client, increment connection count, store info
    client, address = sock.accept()
    count += 1
    name = client.recv(BUFSIZE).decode()

    # print debug connection information
    print(f'Connection {count} from {name} - {address}')

    # format message and send to client
    message = f'Current time: {ctime()}\nGoodbye!'
    client.send(message.encode())
