# -- coding: utf-8 --
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from funcoes import sair, sobre, MontaTela, PosicionaBotao, CriarBotao, FecharTela
from vars import *

cor = "WhiteSmoke"
largura_caixa = 90

def menu():
    tela_vendas.destroy()

tela_vendas = MontaTela(cor, img_em_construcao,"Vendas", False)

#Botão Menu
imagem = Image.open(icone_voltar)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)
btnmenu = tk.Button(tela_vendas, text ="Menu",image=tkimage, compound='left', foreground='black', font=('Roboto', 12), command=menu)
btnmenu.image = tkimage
btnmenu.pack(pady=20)
btnmenu.place(x = 5, y = 10, width = 90)
#Botão Menu

tela_vendas.bind('<Escape>', lambda event: FecharTela(tela_vendas))

#Mantêm a tela_cli em Execução
tela_vendas.mainloop()

