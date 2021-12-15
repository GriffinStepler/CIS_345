from socket import *
import time

# define constants
HOST = gethostbyname(gethostname())
PORT = 49002
ADDR = (HOST, PORT)
BUFSIZE = 1024

# create a socket object


# bind socket to IP address and port


# listen for connections


# wait for connections, send encoded time, close client connection
