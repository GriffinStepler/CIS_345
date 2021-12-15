import socket

# create server constants (no constant variable in Python; all caps is for our own sake)
# HOST = 'localhost'  # 127.0.0.1 loopback IP Address; use this unless you want to communicate with another computer on your network
HOST = socket.gethostbyname('Hindsight-20')
PORT = 49000  # this port is usually unassigned
ADDR = (HOST, PORT)  # socket needs this information when it's bound

# create socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(ADDR)
# server_socket.bind(('127.0.0.1', 49000))  # this is the same as above
server_socket.listen(1)  # argument is the connection limit; can't allow more connection requests than this
print(f'Server started. Listening on {ADDR}\n{server_socket}')

# accept method returns two data: client socket obj and client address
client_socket, address = server_socket.accept()

with client_socket:
    print(f'Client connected {address}\n{client_socket}')
    while True:
        data = client_socket.recv(1024).decode()  # bytes read from the socket
        if not data:
            break
        client_socket.send(f'Server echo: {data}'.encode())  # .encode() turns it into bytes

server_socket.close()
