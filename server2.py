###################
# Servidor 2
# Porta: 5002
###################
import socket
import os
import sys
import replicacao
import toolip

db = 'dbServer2.txt'
serverIp = toolip.getIp()
servers = [(serverIp, 5001),(serverIp, 5002),(serverIp, 5003)]

# apenas para zerar a base de dados
def zeraDb():
    f = open(db, 'w')
    f.close()
    print '-- S2 - Base de dados zerada.'

def salvaPostDb(post):
    f = open(db, 'a')
    f.write(post + '\n')
    f.close()
    print '-- S2 - Post salvo.'

zeraDb()

if __name__ == '__main__':
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Escolher o Servidor
    tcp.bind(servers[1])
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
            
                    # Efetuando Replicacao
                    replicacao.replica(2)
            
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
