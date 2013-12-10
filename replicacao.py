dbs = ['dbServer1.txt', 'dbServer2.txt']

def replica(servidor):
    serverParaLista = int(servidor) - 1
    dbQueChamou = open(dbs[serverParaLista], 'r')
    lstAux = dbQueChamou.readlines()
    last_line = lstAux[-1]

    for db in dbs:
        if db <> dbs[serverParaLista]:
            dbAux = open(db, 'a')
            dbAux.write(last_line)
            dbAux.close()

def preencheBaseZerada(servidor):
	serverParaLista = int(servidor) - 1
	dbQueChamou = open(dbs[serverParaLista], 'a')
	for db in dbs:
		if db <> dbs[serverParaLista]:
			dbQueTemDados = open(db, 'r')
			for linha in dbQueTemDados.readlines():
				dbQueChamou.write(linha)

			dbQueTemDados.close()

	dbQueChamou.close()
