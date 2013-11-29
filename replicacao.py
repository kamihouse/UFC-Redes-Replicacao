dbs = ['dbServer1.txt', 'dbServer2.txt', 'dbServer3.txt']

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
