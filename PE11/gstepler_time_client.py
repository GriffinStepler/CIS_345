# Griffin Stepler, CIS345, iCourse, PE11
from socket import *

# set constants
# HOST = 'localhost'
HOST = '192.168.1.20'
PORT = 49002
ADDR = (HOST, PORT)
BUFSIZE = 1024

# create socket and bind
sock = socket(AF_INET, SOCK_STREAM)
# connect to
sock.connect(ADDR)
# send and receive information
sock.send(b"Griffin's Desktop")
time = sock.recv(BUFSIZE).decode()
# close the socket
sock.close()

print(time)
