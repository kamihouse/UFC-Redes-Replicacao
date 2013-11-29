import socket
f = open('ip.txt', 'w')
f.write(socket.gethostbyname(socket.gethostname()))
f.close()

def getIp():
    f = open('ip.txt', 'r')
    return f.readline()
