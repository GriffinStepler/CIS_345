# Griffin Stepler, CIS345, iCourse, PE11
from socket import *

# constants
HOST = 'localhost'
PORT = 49001
ADDR = (HOST, PORT)
BUFSIZE = 1024
EXIT = '[Q]'
screen_name = input('Enter screen name: ')

# socket creation and connection
sock = socket(AF_INET, SOCK_STREAM)
print('connecting...')
sock.connect(ADDR)
print('connected')

# sending client screen_name
sock.send(screen_name.encode())

# receive server screen_name and store
s_screen_name = sock.recv(BUFSIZE).decode()
print(f'\n{s_screen_name} has connected to the chat')
print('Type [Q] to Exit')

# main messaging loop
while True:
    try:
        s_message = sock.recv(BUFSIZE).decode()
        print(f'{s_screen_name}: {s_message}')

        c_message = input('Message: ')

        if c_message.upper == EXIT:
            sock.send(f'{screen_name} has left the chat'.encode())
            break

        sock.send(c_message.encode())

    except (OSError, ConnectionAbortedError):  # this prevents errors when one side disconnects, and the other tries to
        print('Disconnected')
        break

sock.close()
