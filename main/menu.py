# -- coding: utf-8 --
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from funcoes import clientes,produtos, vendas, gestao, sair, sobre, MontaTela, LimparConsole, fechar_tela
from vars import *

LimparConsole()

cor = "WhiteSmoke"

tela = MontaTela(cor,img_background, "Menu", True)
    
##Adiciona Barra de Menus
barramenu = tk.Menu(tela, tearoff=0)
menu_func = tk.Menu(barramenu, tearoff=0)
menu_ajuda = tk.Menu(barramenu, tearoff=0)

barramenu.add_cascade(label="Funcionalidades", menu=menu_func, underline=0)
   
##Adiciona Itens de Menu Funcionalidades
menu_func.add_command(label="Clientes",command=clientes, accelerator="Alt+ C", underline=0)
menu_func.add_command(label="Produtos/Serviços",command=produtos, accelerator="Alt+ P", underline=0)
menu_func.add_command(label="Vendas",command=vendas, accelerator="Alt+ V", underline=0)
menu_func.add_command(label="Gestão de Acessos",command=gestao, accelerator="Alt+ G", underline=0)
menu_func.add_separator()
menu_func.add_command(label="Sair", command=lambda: sair(tela), accelerator="Esc")


barramenu.add_cascade(label="Ajuda", menu=menu_ajuda, underline=0)
##Adiciona Itens de Menu Ajuda
menu_ajuda.add_command(label="Sobre", command=sobre, accelerator="F1")

##Executa a Tela
tela.config(menu=barramenu)

tela.bind_all("<Alt-c>", lambda e: clientes())
tela.bind_all("<Alt-p>", lambda e: produtos())
tela.bind_all("<Alt-v>", lambda e: vendas())
tela.bind_all("<Alt-g>", lambda e: gestao())
tela.bind_all("<F1>", lambda e: sobre())

tela.bind('<Escape>', lambda event: fechar_tela(tela))

##Mantèm a Tela em Execução
tela.mainloop()



        
