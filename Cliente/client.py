# -*- coding: utf-8 -*-

import socket
from sys import exit
from random import choice

idCliente = str(choice(xrange(1, 30000)))
idPost = 1
middleware = ('10.0.37.154', 9000)

try:
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.connect(middleware)

except socket.error: 
    print 'Middleware Down!'
    exit(0)

def publicaPost(title, msg):
    global idCliente
    global idPost
    
    post = idCliente + '||' + str(idPost) + '||' + title + '||' + msg
    tcp.send(post)
    idPost+=1

if __name__ == '__main__':
    print '############################################################################'
    print '# Bem vindo ao sistema de postagem de Noticias.'
    print '# UFC - Redes e Sistemas Distribuidos'
    print '#'
    print '# *Para sair use CTRL+C'
    print '############################################################################\n'

    while True:
        try:
            title = raw_input('Titulo: ')
            msg = raw_input('Mensagem: ')
            print ''
            publicaPost(title, msg)
            aviso = tcp.recv(1024)
            if aviso:
                print aviso

        except KeyboardInterrupt:
            print 'Conexao abortada pelo usuario.'
            tcp.close()
            break