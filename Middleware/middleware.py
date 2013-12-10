# -*- coding: utf-8 -*-

###################
# Middleware
# Porta: 5000
###################
import socket
import os
import sys
from random import choice
from time import sleep, time

serverIp = '10.0.37.154'
portaMiddleware = 9000

servers = [(serverIp, 5001),(serverIp, 5002)]
msgs_nao_enviadas = []

def verificaServidoresAtivos():
    lista_disponiveis = []
    for server in servers:
        try:
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp.connect(server)
            lista_disponiveis.append(server)
            tcp.close()
            print '-- Disponivel: ' + str(server)

        except:
            print '-- Indisponivel: ' + str(server)

    if len(lista_disponiveis) == 0:
        return None
    
    return lista_disponiveis

def postaNoServer(post, conexao):
    print '+---', cliente, post
    conexao.send(post)

def conecta_server(server):
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.connect(server)
    print '+--- Conectado: %s:%s' %(server[0], server[1])
    return tcp

def desconecta_server(conexao):
    conexao.close()
    print '+--- Desconectado'

def envia_msgs_arquivadas(tempo):
    global msgs_nao_enviadas
    if len(msgs_nao_enviadas) != 0 :
        if time() >= tempo + 10:
            tempo = time()
            lista_disponiveis = verificaServidoresAtivos()
            if lista_disponiveis:
                server_escolhido = choice(lista_disponiveis)
                for msg in msgs_nao_enviadas:
                    conexaoTemporaria = conecta_server(server_escolhido)
                    print msgs_nao_enviadas
                    try:
                        postaNoServer(msg, conexaoTemporaria)
                        desconecta_server(conexaoTemporaria)
                    except:
                        desconecta_server(conexaoTemporaria)
                        print '----- Nao foi possivel enviar'

                    msgs_nao_enviadas = []
            else:
                print '----- Servidores indisponiveis'
    else:
        print '----- Sem mensagens para enviar'

if __name__ == '__main__':
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Escolher o Servidor
    tcp.bind((serverIp, portaMiddleware))
    tcp.listen(1)
    con = None

    print 'Middleware iniciado!'

    try:
        tempo = time()
        while True:
            envia_msgs_arquivadas(tempo)
            con, cliente = tcp.accept()
            pid = os.fork()
            if pid == 0:
                tcp.close()
                print 'Conectado por', cliente
                while True:
                    envia_msgs_arquivadas(tempo)
                    post = con.recv(1024)
                    if not post:
                        con.close()
                        break
                    else:
                        lista_disponiveis = verificaServidoresAtivos()
                        if lista_disponiveis:
                            server_escolhido = choice(lista_disponiveis)
                            conexaoTemporaria = conecta_server(server_escolhido)
                            postaNoServer(post, conexaoTemporaria)
                            desconecta_server(conexaoTemporaria)
                            con.send('ok')
                        else:
                            print '- Atencao! Nenhum servidor disponivel'
                            msgs_nao_enviadas.append(post)
                            con.send('*Desculpe, nossos servidores estao todos ocupados no momento.\nSua noticia foi salva e sera publicada em breve.\n')
        
                print 'Finalizada a conexao do cliente', cliente
                con.close()
                sys.exit(0)
            else:
                con.close()

    except KeyboardInterrupt:
        if con: con.close()
        tcp.close()
        print '\nMiddleware Interrompido.'
        sys.exit(0)