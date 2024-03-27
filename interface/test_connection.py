import socket as sockets
s=sockets.socket(sockets.AF_INET,sockets.SOCK_STREAM)
s.bind((sockets.gethostname(),1234))
print(sockets.gethostname())
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    clientsocket.close()