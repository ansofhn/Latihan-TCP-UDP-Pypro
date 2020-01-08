import socket

ip, port=("192.168.43.92", 2112)
while True:
    UDPc=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    UDPc.sendto(input("\nSEND TO SERVER   : ").encode("utf-8"),((ip, port)))
    recieve, addr=UDPc.recvfrom(1024)
    print("\nServer Message   :",recieve.decode("utf-8"))
    