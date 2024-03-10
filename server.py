import socket
import threading

from datetime import timedelta
from datetime import datetime


HEADER = 512
PORT = 5355
SERVER = "127.0.0.1"

ADDR = (SERVER, PORT)
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "!DISCONNECT"



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)



def handle_client(c, addr):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] Got connection from {addr}")

    c.send(bytes("Hello, this message is sent from the server.", FORMAT))

    resp=c.recv(HEADER)
    print(resp.decode(FORMAT))




def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()



if __name__ == "__main__":
    print("[STARTING] server is starting...")
    start()
