import socket

PORT = 5355
HEADER=512
SERVER = "127.0.0.1"
FORMAT = 'UTF-8'


def handle_server():
    c = socket.socket()  
    c.connect((SERVER, PORT))  # connect to the server
    data = c.recv(HEADER)
    print(data.decode(FORMAT))

    c.send(bytes("Hello, this message is sent from the client.", FORMAT))



if __name__ == '__main__':
    handle_server()