###############################################################################
# Universidade Federal do Ceará.
# Redes de Computadores & Sistemas Distribuídos.
#
# Trabalho 2 - Implementar Replicação (3 Instâncias de Servidor)
#
# Prof:		Flávio R. C. Sousa
#
# Alunos:	Jefferson Silva
#		João Marcos Epifanio
#		Matheus Souza de Carvalho
#		Thiago Pereira Rosa
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
		a.d) replicação (nossa biblioteca de replicação)
		a.e) random
	b) S.O. Linux e/ou Unix.
	c) Estar conectado em uma Rede de Computadores.

2 - Recomendações:
	a) Utilize os Servidores e o Middleware em ambiente Linux de preferência.

2 - Como executar os Servidores:
	a) utilize o comando abaixo para iniciar o servidor:
		python server.py
		(Execute para cada um dos servidores que deseja iniciar)

3 - Como executar os Clientes:
	a) (Linha de Comando) Executar o cliente em qualquer máquina com os seguintes comandos:
		a.a) python client.py
		a.b) Efetuar postagens com os campos TÍTULO e MENSAGEM.
			a.b.a) Para encerrar CTRL + C
	b) (Interface Gráfica) Executar o cliente em qualquer máquina com os seguintes comandos:
		a.a) python clientApp.py
		a.b) Efetuar postagens com os campos TÍTULO e MENSAGEM.
