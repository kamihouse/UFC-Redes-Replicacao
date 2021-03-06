###################
# Servidor 1
# Porta: 5001
###################
import socket
import os
import sys
from replicacao import *


db = 'dbServer1.txt'
serverIp = ('10.0.37.154', 5001)

# apenas para zerar a base de dados
def zeraDb():
    f = open(db, 'w')
    f.close()
    print '-- S1 - Base de dados zerada.'

def salvaPostDb(post):
    f = open(db, 'a')
    f.write(post + '\n')
    f.close()
    print '-- S1 - Post salvo.'

zeraDb()
preencheBaseZerada(1)

if __name__ == '__main__':
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Escolher o Servidor
    tcp.bind(serverIp)
    tcp.listen(1)
    con = None
    print 'Servidor iniciado!'

    try:
        while True:
            con, cliente = tcp.accept()
            pid = os.fork()
            if pid == 0:
                tcp.close()
                print 'Conectado por', cliente
                while True:
                    post = con.recv(1024)
                    if not post:
                        con.close()
                        break
            
                    print cliente, post
                    salvaPostDb(post)
                    replica(1)
        
                print 'Finalizando conexao do cliente', cliente
                con.close()
                sys.exit(0)
            else:
                con.close()
    except KeyboardInterrupt:
        if con: con.close()
        tcp.close()
        print '\nServidor Interrompido.'
        sys.exit(0)

