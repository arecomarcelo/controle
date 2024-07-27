import tkinter as tk
from PIL import Image, ImageTk

def criar_botao_com_texto_e_imagem():
    root = tk.Tk()
    root.geometry('800x600')

    # Carregar e redimensionar a imagem
    imagem = Image.open("imagens\limpar.ico")
    imagem = imagem.resize((50, 50))  # Redimensione conforme necessário
    tkimage = ImageTk.PhotoImage(imagem)

    # Criar o botão com a imagem e o texto
    botao = tk.Button(root, text="Limpar", image=tkimage, compound='left', command=lambda: print("Botão clicado!"))
    botao.image = tkimage  # Manter uma referência à imagem
    botao.pack(pady=20)

    root.mainloop()

criar_botao_com_texto_e_imagem()
