import tkinter as tk
from tkinter import messagebox

def clientes():
    messagebox.showinfo("Clientes", "Cadastro de Clientes")
    
def sobre():
    messagebox.showinfo("Sobre", "Sistema Comercial 1.0")
    
def sair(tela):
    var_sair = messagebox.askyesno("Sair", "Tem certeza que deseja sair?")
    if var_sair:
        tela.destroy()
