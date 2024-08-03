# -- coding: utf-8 --
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from funcoes import clientes,produtos, vendas, gestao, sair, sobre, MontaTela, LimparConsole
from vars import *

LimparConsole()

cor = "WhiteSmoke"

tela = MontaTela(cor,img_background, "Menu", True)
    
##Adiciona Barra de Menus
barramenu = tk.Menu(tela)
menu_func = tk.Menu(barramenu)
menu_ajuda = tk.Menu(barramenu)

barramenu.add_cascade(label="Funcionalidades", menu=menu_func)
barramenu.add_cascade(label="Ajuda", menu=menu_ajuda)
   
##Adiciona Itens de Menu Funcionalidades
menu_func.add_command(label="Clientes",command=clientes)
menu_func.add_command(label="Produtos/Serviços",command=produtos)
menu_func.add_command(label="Vendas",command=vendas)
menu_func.add_command(label="Gestão de Acessos",command=gestao)
menu_func.add_separator()
menu_func.add_command(label="Sair", command=lambda: sair(tela))

##Adiciona Itens de Menu Ajuda
menu_ajuda.add_command(label="Sobre", command=sobre)

##Executa a Tela
tela.config(menu=barramenu)

##Mantèm a Tela em Execução
tela.mainloop()



        
