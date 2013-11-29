# -*- coding: utf8 -*-
from Tkinter import *
import client


interface   = Tk()

titl        = StringVar(interface)
msg         = StringVar(interface)


# Definindo o método de efetuar postagem
def post():
    client.publicaPost(titl.get(), msg.get())
    # Limpando os campos



# Widgets vão aqui...
interface.title('Sistema de Notícias - R.C.BC')
interface.geometry('550x300+100+100')

mensagem    = Label(interface,text='Bem vindo ao Sistema de Notícias\nCom: Replicação, Consistência e Balanceamento de Carga').pack(pady=10)
alunos      = Label(interface,text='Alunos: Jefferson, João Marcos, Matheus e Thiago').pack(pady=5)

titulo      = Label(interface,text='Título:').pack(fill="x", pady=10)
ctitulo     = Entry(interface, textvar=titl, text="").pack(fill="x")

mensagem    = Label(interface,text='Mensagem:').pack(fill="x", pady=10)
cmensagem   = Entry(interface, textvar=msg, text="").pack(fill="x")


Button(text='Publicar esta postagem', command=post).pack(side=BOTTOM, pady=12)

# Tkinter event loop
interface.mainloop()