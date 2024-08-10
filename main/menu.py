# -- coding: utf-8 --
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from funcoes import sair, sobre, MontaTela, LimparConsole, AbreTela, FecharTela
from vars import *

LimparConsole()

##Configura Tela
cor = "WhiteSmoke"
tela = MontaTela(cor,img_background, "Menu", True)
    
##Configura Barra de Menus
barramenu = tk.Menu(tela, tearoff=0)
menu_func = tk.Menu(barramenu, tearoff=0)
menu_ajuda = tk.Menu(barramenu, tearoff=0)

   
##Configura Menu Funcionalidades
barramenu.add_cascade(label="Funcionalidades", menu=menu_func, underline=0)
menu_func.add_command(label="Clientes",command=lambda: AbreTela("clientes.py"), accelerator="Alt+ C", underline=0)
menu_func.add_command(label="Produtos/Serviços",command=lambda: AbreTela("produtos.py"), accelerator="Alt+ P", underline=0)
menu_func.add_command(label="Vendas",command=lambda: AbreTela("vendas.py"), accelerator="Alt+ V", underline=0)
menu_func.add_command(label="Gestão de Acessos",command=lambda: AbreTela("gestao.py"), accelerator="Alt+ G", underline=0)
menu_func.add_separator()
menu_func.add_command(label="Sair", command=lambda: sair(tela), accelerator="Esc")

##Configura Menu Menu Ajuda
barramenu.add_cascade(label="Ajuda", menu=menu_ajuda, underline=0)
menu_ajuda.add_command(label="Sobre", command=sobre, accelerator="F1")

##Executa a Tela
tela.config(menu=barramenu)

##Configura Atalhos
tela.bind_all("<Alt-c>", lambda e: AbreTela("clientes.py"))
tela.bind_all("<Alt-p>", lambda e: AbreTela("produtos.py"))
tela.bind_all("<Alt-v>", lambda e: AbreTela("vendas.py"))
tela.bind_all("<Alt-g>", lambda e: AbreTela("gestao.py"))
tela.bind_all("<F1>", lambda e: sobre())
tela.bind('<Escape>', lambda event: FecharTela(tela))

##Mantèm a Tela em Execução
tela.mainloop()



        
