# Griffin Stepler, CIS345, iCourse, PE11
from socket import *

# constants
HOST = 'localhost'
PORT = 49001
ADDR = (HOST, PORT)
BUFSIZE = 1024
EXIT = '[Q]'
screen_name = input('Enter Screen Name: ')

# socket creation
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(ADDR)

sock.listen(1)
print(f'Server listening on {ADDR}')

client, address = sock.accept()
print(f'Connected to: {address[0]} | {address[1]}')

c_screen_name = client.recv(BUFSIZE).decode()
print(f'\n{c_screen_name} has entered the chat')
print('Press [Q] to Exit')

client.send(screen_name.encode())

while True:
    try:
        message = input('Say something: ')

        if message.upper() == EXIT:
            client.send(b'Server shutting down...')
            break

        client.send(message.encode())

        r_message = client.recv(BUFSIZE).decode()
        print(f'{c_screen_name}: {r_message}')

    except (OSError, ConnectionAbortedError):  # this prevents errors when one side disconnects, and the other tries to
        print('Disconnected')
        break

sock.close()
