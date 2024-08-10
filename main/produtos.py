# -- coding: utf-8 --
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from funcoes import MontaTela, PosicionaBotao, FecharTela
from vars import *
import conexao as cn


largura_caixa = 90

def menu():
    tela_prod.destroy()

tela_prod = MontaTela(cor, img_background,"Cadastro de Produtos e Serviços", False)

#Definição dos Controles
lblcodigo = tk.Label(tela_prod, text ="Codigo:", bg=cor_fundo, fg=cor_fonte, font=(fonte, 12), anchor = "e")
lblcodigo.place(x = 50, y = 60, width = largura_caixa,  height = 25)
txtcodigo = tk.Entry(tela_prod, width = 35, font=(fonte, 12))
txtcodigo.place(x = 150, y = 60, width = 100, height = 25)

lbltipo = tk.Label(tela_prod, text ="Tipo:", bg=cor_fundo, fg=cor_fonte, font=(fonte, 12), anchor = 'e')
lbltipo.place(x = 50, y = 100, width = 90)
tipos = ["PRODUTO", "SERVICO"]
cmbtipo = ttk.Combobox(tela_prod, values=tipos, font=(fonte, 10))
cmbtipo.place(x=150, y=100, width=120, height = 25)
# cmbtipo.current(0)

lbldescricao = tk.Label(tela_prod, text ="Descrição:", bg=cor_fundo, fg=cor_fonte, font=(fonte, 12), anchor = 'e')
lbldescricao.place(x = 50, y = 140, width = 90)
entry = tk.Entry(tela_prod, font=('Calibri', 12))
txtdescricao =  tk.Entry(tela_prod, font=(fonte, 12))
txtdescricao.place(x = 150, y = 140, width = 400)

lblquantidade = tk.Label(tela_prod, text ="Quantidade:", bg=cor_fundo, fg=cor_fonte, font=(fonte, 12), anchor = 'e')
lblquantidade.place(x = 50, y = 180, width = 90)
txtquantidade = tk.Entry(tela_prod, font=(fonte, 12))
txtquantidade.place(x = 150, y = 180, width = 120)

lblcusto = tk.Label(tela_prod, text ="Custo:", bg=cor_fundo, fg=cor_fonte, font=(fonte, 12), anchor = 'e')
lblcusto.place(x = 50, y = 220, width = 90)
txtcusto = tk.Entry(tela_prod, font=('Calibri', 12))
txtcusto.place(x = 150, y = 220, width = 120)

lblpreco = tk.Label(tela_prod, text ="Preço:", bg=cor_fundo, fg=cor_fonte, font=(fonte, 12), anchor = 'e')
lblpreco.place(x = 50, y = 260, width = 90)
txtpreco = tk.Entry(tela_prod, font=('Calibri', 12))
txtpreco.place(x = 150, y = 260, width = 120)

#Definição dos Controles


#Botão Menu
imagem = Image.open(icone_voltar)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)
btnmenu = tk.Button(tela_prod, text ="Menu",image=tkimage, compound='left', foreground='black', font=('Roboto', 12), command=menu, underline=0)
btnmenu.image = tkimage
btnmenu.pack(pady=20)
btnmenu.place(x = 435, y = 320, width = 90)
#Botão Menu

#Botão Limpar
imagem = Image.open(icone_limpar)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)
btnlimpar = tk.Button(tela_prod, text ="Limpar",image=tkimage, compound='left', foreground='black', font=('Roboto', 12),  underline=0)#command=limpar,
btnlimpar.image = tkimage
btnlimpar.pack(pady=20)
PosicionaBotao(tela_prod, btnmenu, btnlimpar)
#Botão Limpar

#Botão Excluir
imagem = Image.open(icone_excluir)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)
btnexcluir = tk.Button(tela_prod, text ="Excluir",image=tkimage, compound='left', foreground='black', font=('Roboto', 12),  underline=0)#command=excluir,
btnexcluir.image = tkimage
btnexcluir.pack(pady=20)
PosicionaBotao(tela_prod, btnlimpar, btnexcluir)
#Botão Excluir

#Botão Gravar
imagem = Image.open(icone_gravar)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)
btngravar = tk.Button(tela_prod, text ="Gravar",image=tkimage, compound='left', foreground='black', font=('Roboto', 12),  underline=0)#command=gravar,
btngravar.image = tkimage
btngravar.pack(pady=20)
PosicionaBotao(tela_prod, btnexcluir, btngravar)
#Botão Gravar


tela_prod.bind('<Escape>', lambda event: FecharTela(tela_prod))

#Mantêm a tela_prod em Execução
tela_prod.mainloop()

