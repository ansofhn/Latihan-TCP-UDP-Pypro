import socket
while True:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("192.168.43.39",8080))
    send=s.send(input("SEND TO SERVER   : ").encode("utf-8"))
    print(s.recv(1024).decode("utf-8"))
    s.close()