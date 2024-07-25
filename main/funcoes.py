import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from enumeradores import Direcao
from vars import nome_aplicacao

def PosicionaBotao (tela, botao_anterior, botao_atual, direcao = Direcao.DIREITA):
    tela.update_idletasks()
    
    width = botao_anterior.winfo_width() + 5
    
    if direcao.name == "ESQUERDA":
        posx = botao_anterior.winfo_x() + width
    else:
        posx = botao_anterior.winfo_x() - width
    
    posy = botao_anterior.winfo_y()    
    
    botao_atual.place(x = posx, y = posy, width = 65)         

def clientes():
    exec(open("main\clientes.py", encoding="utf-8").read(),locals())
    
def sobre():
    messagebox.showinfo("Sobre", "Sistema Comercial 1.0")
    
def sair(tela):
    var_sair = messagebox.askyesno("Sair", "Tem certeza que deseja sair?")
    if var_sair:
        tela.destroy()
               

def MontaTela(cor_fundo, imagem, titulo, principal = False):
    if principal:
        tela = tk.Tk()
    else:
        tela = tk.Toplevel()    
        
    tela.geometry('1960x800+0+0')
    tela.state('zoomed')
    tela.title(f"{nome_aplicacao} - {titulo}")
    tela['bg'] = cor_fundo

    tkimage = ImageTk.PhotoImage(Image.open(imagem).resize((tela.winfo_screenwidth(), tela.winfo_screenheight())))
    label = tk.Label(tela, image=tkimage)
    label.image = tkimage  # Mantenha uma referência à imagem
    label.pack()
    
    return tela
