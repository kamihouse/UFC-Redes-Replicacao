import socket
from random import choice

idCliente = str(choice(xrange(1, 30000)))
idPost = 1
serverIp = '10.0.37.154'
servers = [(serverIp, 5001),(serverIp, 5002),(serverIp, 5003)]
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect(choice(servers))

def publicaPost(title, msg):
    global idCliente
    global idPost
    
    post = idCliente + '||' + str(idPost) + '||' + title + '||' + msg
    tcp.send(post)
    idPost+=1

if __name__ == '__main__':
    print 'Conexao iniciada.'
    print 'Para sair use CTRL+C\n'

    while True:
        try:
            title = raw_input('Titulo: ')
            msg = raw_input('Mensagem: ')
            print '\n'
            publicaPost(title, msg)

        except KeyboardInterrupt:
            print 'Conexao Abortada pelo usuario.'
            tcp.close()
            break
