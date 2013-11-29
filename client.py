import socket
from random import *

idCliente = str(choice(xrange(1, 30000)))
idPost = 1
serverIp = '192.168.254.12'
servers = [(serverIp, 5001),(serverIp, 5002),(serverIp, 5003)]

if __name__ == '__main__':
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.connect(choice(servers))
    print 'Conexao iniciada.'
    print 'Para sair use CTRL+C\n'

    while True:
        try:
            title = raw_input('Titulo: ')
            msg = raw_input('Mensagem: ')
            print '\n'
            post = str(idCliente) + '||' + str(idPost) + '||' + title + '||' + msg
            tcp.send(post)
            idPost+=1

        except KeyboardInterrupt:
            print 'Conexao Abortada pelo usuario.'
            tcp.close()
            break
