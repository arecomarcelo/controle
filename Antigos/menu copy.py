# -- coding: utf-8 --
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from funcoes import clientes, sair, sobre
from vars import *

cor = "WhiteSmoke"

##Monta Tela
tela = tk.Tk() 
tela.geometry('1960x800+0+0')
tela.state('zoomed')
tela.title("Controle Comercial 1.0 - Menu")
tela['bg'] = cor

tkimage = ImageTk.PhotoImage(Image.open(img_desktop))
tk.Label(tela, image=tkimage).pack()
    
##Adiciona Barra de Menus
barramenu = tk.Menu(tela)
menu_func = tk.Menu(barramenu)
menu_ajuda = tk.Menu(barramenu)

barramenu.add_cascade(label="Funcionalidades", menu=menu_func)
barramenu.add_cascade(label="Ajuda", menu=menu_ajuda)
   
##Adiciona Itens de Menu Funcionalidades
menu_func.add_command(label="Clientes",command=clientes)
menu_func.add_command(label="Produtos/Serviços")
menu_func.add_command(label="Vendas")
menu_func.add_command(label="Gestão de Acessos")
menu_func.add_separator()
menu_func.add_command(label="Sair", command=lambda: sair(tela))

##Adiciona Itens de Menu Ajuda
menu_ajuda.add_command(label="Sobre", command=sobre)

##Executa a Tela
tela.config(menu=barramenu)

##Mantèm a Tela em Execução
tela.mainloop()



        
