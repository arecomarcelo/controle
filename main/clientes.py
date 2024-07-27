# -- coding: utf-8 --
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from funcoes import clientes, sair, sobre, MontaTela, PosicionaBotao, CriarBotao
from vars import *

cor = "WhiteSmoke"
largura_caixa = 90

def menu():
    tela_cli.destroy()

tela_cli = MontaTela(cor, img_background,"Cadastro de Clientes", False)

#Insere um Label - anchor w= esquerda, e=direita, c=centralizada
lblcodigo = tk.Label(tela_cli, text ="Codigo:", bg="black", fg="WhiteSmoke", font=('Roboto', 12), anchor = "e")
lblcodigo.place(x = 50, y = 60, width = largura_caixa,  height = 25)
txtcodigo = tk.Entry(tela_cli, width = 35, font=('Roboto', 12))
txtcodigo.place(x = 150, y = 60, width = 100, height = 25)

lblnome = tk.Label(tela_cli, text ="Nome:", bg="black", fg="WhiteSmoke", font=('Roboto', 12), anchor = "e")
lblnome.place(x = 50, y = 100, width = largura_caixa, height = 25)
txtnome = tk.Entry(tela_cli, width = 35, font=('Roboto', 12))
txtnome.place(x = 150, y = 100, width = 375, height = 25)

lbltelefone = tk.Label(tela_cli, text ="Telefone:", bg="black", fg="WhiteSmoke", font=('Roboto', 12), anchor = "e")
lbltelefone.place(x = 50, y = 140, width = largura_caixa, height = 25)
txttelefone = tk.Entry(tela_cli, width = 35, font=('Roboto', 12))
txttelefone.place(x = 150, y = 140, width = 375, height = 25)

lblemail = tk.Label(tela_cli, text ="E-mail:", bg="black", fg="WhiteSmoke", font=('Roboto', 12), anchor = "e")
lblemail.place(x = 50, y = 180, width = largura_caixa, height = 25)
txtemail = tk.Entry(tela_cli, width = 35, font=('Roboto', 12))
txtemail.place(x = 150, y = 180, width = 375, height = 25)

lblobservacao = tk.Label(tela_cli, text ="Observação:", bg="black", fg="WhiteSmoke", font=('Roboto', 12), anchor = "e")
lblobservacao.place(x = 50, y = 220, width = largura_caixa, height = 25)
txtobservacao= tk.Text(tela_cli, font=('Roboto', 12))#Permite Quebra de Linha, diferente do Entry
txtobservacao.place(x=150, y=220, width=375, height=80)

# btnmenu = tk.Button(tela_cli, text ="Menu", bg ='silver',foreground='black', font=('Roboto', 12), command=menu)
# btnmenu.place(x = 445, y = 320, width = 65)

# btnlimpar = tk.Button(tela_cli, text ="Limpar", bg ='silver',foreground='black', font=('Roboto', 12))
# PosicionaBotao(tela_cli, btnmenu, btnlimpar)

# btnexcluir = tk.Button(tela_cli, text ="Excluir", bg ='silver',foreground='black', font=('Roboto', 12))
# PosicionaBotao(tela_cli, btnlimpar, btnexcluir)

# btngravar = tk.Button(tela_cli, text ="Gravar", bg ='silver',foreground='black', font=('Roboto', 12))
# PosicionaBotao(tela_cli, btnexcluir, btngravar)

#Botão Menu
imagem = Image.open(icone_voltar)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)

btnmenu = tk.Button(tela_cli, text ="Menu",image=tkimage, compound='left', foreground='black', font=('Roboto', 12), command=menu)
btnmenu.image = tkimage
btnmenu.pack(pady=20)
btnmenu.place(x = 435, y = 320, width = 90)

#Botão Limpar
imagem = Image.open(icone_limpar)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)

btnlimpar = tk.Button(tela_cli, text ="Limpar",image=tkimage, compound='left', foreground='black', font=('Roboto', 12), command=menu)
btnlimpar.image = tkimage
btnlimpar.pack(pady=20)
PosicionaBotao(tela_cli, btnmenu, btnlimpar)

#Botão Excluir
imagem = Image.open(icone_excluir)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)

btnexcluir = tk.Button(tela_cli, text ="Excluir",image=tkimage, compound='left', foreground='black', font=('Roboto', 12), command=menu)
btnexcluir.image = tkimage
btnexcluir.pack(pady=20)
PosicionaBotao(tela_cli, btnlimpar, btnexcluir)

#Botão Gravar
imagem = Image.open(icone_gravar)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)

btngravar = tk.Button(tela_cli, text ="Gravar",image=tkimage, compound='left', foreground='black', font=('Roboto', 12), command=menu)
btngravar.image = tkimage
btngravar.pack(pady=20)
PosicionaBotao(tela_cli, btnexcluir, btngravar)



#Mantêm a tela_cli em Execução
tela_cli.mainloop()