import socket as sockets
s=sockets.socket(sockets.AF_INET,sockets.SOCK_STREAM)
s.connect((sockets.gethostname(),1234))

msg=s.recv(1024)

print(msg.decode("utf-8"))