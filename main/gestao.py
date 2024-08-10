# -- coding: utf-8 --
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from funcoes import MontaTela, PosicionaBotao, CriarBotao, FecharTela
from vars import *

cor = "WhiteSmoke"
largura_caixa = 90

def menu():
    tela_gestao.destroy()

tela_gestao = MontaTela(cor, img_em_construcao,"Gestão de Acessos", False)

#Botão Menu
imagem = Image.open(icone_voltar)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)
btnmenu = tk.Button(tela_gestao, text ="Menu",image=tkimage, compound='left', foreground='black', font=('Roboto', 12), command=menu)
btnmenu.image = tkimage
btnmenu.pack(pady=20)
btnmenu.place(x = 5, y = 10, width = 90)
#Botão Menu

tela_gestao.bind('<Escape>', lambda event: FecharTela(tela_gestao))

#Mantêm a tela_cli em Execução
tela_gestao.mainloop()

