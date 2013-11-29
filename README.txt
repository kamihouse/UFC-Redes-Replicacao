##############################################################################
# Universidade Federal do Ceará.
# Redes de Computadores & Sistemas Distribuídos.
#
# Trabalho 2 - Implementar Replicação (3 Instâncias de Servidor)
#
# Prof:		Flávio R. C. Sousa
#
# Alunos:	Jefferson Silva
#			João Marcos Epifanio
#			Matheus Souza de Carvalho
#			Thiago Pereira Rosa
#
# GitHub:	https://github.com/kamihouse/UFC-Redes-Replicacao
###############################################################################

Sistema de Postagens de Notícias em Python com Replicação, Consistência e 
Balanceamento de Carga com armazenamento em Arquivos de texto.

1 - Requerido:
	a) Python 2.7 (+ as bibliotecas abaixo)
		a.a) sockets
		a.b) os
		a.c) sys
		a.d) replicacao (nossa biblioteca de replicação)
		a.e) random
	b) S.O. Linux e/ou Unix.
	c) Estar conectado em uma Rede de Computadores.

2 - Recomendações:
	a) Alterar as configurações de IP de acordo com a especificação da sua rede.
		a.a) client.py - Alterar a var servers na Linha 6 (servers = [('192.168.254.12', 5001), ...])
		a.b) server*.py - Alterar var servers na Linha 11 (servers = [('192.168.254.12', 5001), ...])

2 - Como executar os Servidores:
	a) Executar os servidores em máquinas separadas, ou em Portas diferentes na mesma máquina.
		utilizando os seguintes comandos (Logs de conexão serão exibidos):
		a.a) python server1.py
			 python server2.py
			 python server3.py

3 - Como executar os Clientes:
	a) (Linha de Comando) Executar o cliente em qualquer máquina com os seguintes comandos:
		a.a) python client.py
		a.b) Efetuar postagens com os campos TÍTULO e MENSAGEM.
			a.b.a) Para encerrar CTRL + C
	b) (Interface Gráfica) Executar o cliente em qualquer máquina com os seguintes comandos:
		a.a) python clientApp.py
		a.b) Efetuar postagens com os campos TÍTULO e MENSAGEM.
