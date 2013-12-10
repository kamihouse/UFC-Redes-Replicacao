# -*- coding: utf-8 -*-

###################
# Middleware
# Porta: 5000
###################
import socket
import os
import sys
import thread
from random import choice
from time import sleep

serverIp = '192.168.254.2'
portaMiddleware = 10000

servers = [(serverIp, 5001),(serverIp, 5002),(serverIp, 5003)]

def envio_msgs_nao_enviadas(delay):
    while True:
        temp = open('msgs_nao_enviadas.txt', 'r')
        linhas = temp.readlines()
        temp.close()
        del(temp)

        temp = open('msgs_nao_enviadas.txt', 'w')

        print '----- th - Thread de atualização'
        if len(linhas) != 0:
            lista_disponiveis = verificaServidoresAtivos()
            if lista_disponiveis:
                server_escolhido = choice(lista_disponiveis)
                conexaoTemporaria = conecta_server(server_escolhido)
                for linha in linhas:
                    try:
                        postaNoServer(linha.split('\n')[0], conexaoTemporaria)
                        linhas.remove(linha)
                    except:
                        desconecta_server(conexaoTemporaria)
                        temp.write(linha)
                        print '----- th - Erro servidor %s indisponivel' %(str(server_escolhido))
                        break
            else:
                print '----- th - Ainda nao ha servidor disponivel'

        temp.close()
        del(linhas)
        sleep(delay)

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

if __name__ == '__main__':
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Escolher o Servidor
    tcp.bind((serverIp, portaMiddleware))
    tcp.listen(1)
    con = None
    msgs_nao_enviadas = open('msgs_nao_enviadas.txt', 'w')
    msgs_nao_enviadas.close()
    del(msgs_nao_enviadas)

    #executando thread de consistencia - delay de 10 segundos
    thread.start_new_thread(envio_msgs_nao_enviadas, tuple([10]))

    print 'Middleware iniciado!'

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
                    else:
                        lista_disponiveis = verificaServidoresAtivos()
                        if lista_disponiveis:
                            server_escolhido = choice(lista_disponiveis)
                            conexaoTemporaria = conecta_server(server_escolhido)
                            postaNoServer(post, conexaoTemporaria)
                            desconecta_server(conexaoTemporaria)
                        else:
                            print '- Atencao! Nenhum servidor disponivel'
                            temp = open('msgs_nao_enviadas.txt', 'a')
                            temp.write(post + '\n')
                            temp.close()
                            con.send('*Desculpe, nossos servidores estao todos ocupados no momento.\nSua noticia foi salva e sera publicada em breve.\n')
        
                print 'Finalizada a conexao do cliente', cliente
                con.close()
                sys.exit(0)
            else:
                con.close()

    except KeyboardInterrupt:
        thread.exit()
        if con: con.close()
        tcp.close()
        print '\nMiddleware Interrompido.'
        sys.exit(0)