"""import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip, port = ("127.0.0.1",2112)
s.bind((ip, port))
print("Connection from {0}:{1}".format(ip, port))
s.listen(5)

while True:
    client, address = s.accept()
    print("IP Client {0}:   {1}".format(address[0], address[1]))
    print(client.recv(1024).decode("utf-8"))
    client.send(input("").encode("utf-8"))
    client.close()
s.close()"""

import socket
import threading
from time import sleep as wait
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip, port = ("0.0.0.0",2112)
s.bind((ip, port))
print("Connection from {0}:{1}".format(ip, port))
s.listen(5)

def ClientConn(client, address):
    print("IP Client {0}:   {1}".format(address[0], address[1]))
    print("MESSAGE FROM CLIENT  :",client.recv(1024).decode("utf-8"))
    client.send(input("SEND TO CLIENT       : ").encode("utf-8"))
    wait(5)
    client.close()
while True:
    try:
        client, address = s.accept()
        threading.Thread(target=ClientConn, args=(client, address)).start()
    except:
        s.close()
        break