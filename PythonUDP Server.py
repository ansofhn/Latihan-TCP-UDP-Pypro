import socket

UDPs=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip, port = ("0.0.0.0", 2112)
UDPs.bind((ip, port))
print("UDP Server Listening")

while True:
    message, address=UDPs.recvfrom(1024)
    print(f"IP Client {address[0]}:{address[1]}")
    print("MESSAGE FROM CLIENT  :",message.decode("utf-8"))
    UDPs.sendto(input("SEND TO CLIENT       : ").encode("utf-8"), address)
UDPs.close()