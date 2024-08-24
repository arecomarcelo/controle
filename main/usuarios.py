# -- coding: utf-8 --
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from funcoes import MontaTela, LimparConsole, PosicionaBotao, FecharTela
from vars import *
import conexao as cn

LimparConsole()

##Funcoes Internas
def limpar():
    txtUsuario.delete(0,"end")
    txtNome.delete(0,"end")
    txtsenha.delete(0,"end")
    txtUsuario.focus_set()
    
def buscar():
    var_usuario = txtUsuario.get()
 
    con=cn.conexao()
    sql_txt = f"select usuario,nome,CAST(aes_decrypt(senha,'chave') as char) as senha from login where usuario = '{var_usuario}'"
    rs=con.consultar(sql_txt)
    if rs:
        limpar()
        txtUsuario.insert(0, rs[0])
        txtNome.insert(0,rs[1])
        txtsenha.insert(0,rs[2])
    else:
        messagebox.showwarning("Aviso", "Usuario não Encontrado")
        limpar()
        txtUsuario.focus_set()

    con.fechar()
    
def duplo_click(event):
    limpar()
    item = tree.item(tree.selection())
    txtUsuario.insert(0, item['values'][1])
    buscar()

    
def visualizar():
    con=cn.conexao()
    sql_txt = "select Codigo_int,usuario,nome,criado_em  from login order by nome"
    rs=con.consultar_tree(sql_txt)

    tree.bind("<Double-1>", duplo_click)
    
    for linha in tree.get_children():
        tree.delete(linha)
    
    for linha in rs:
        tree.insert("", tk.END,values=linha) 
    
def pesquisar_nome(p):
    ...
    # con=cn.conexao()
    # sql_txt = f"select * from clientes where nome like '%{p}%'"
    
    # rs=con.consultar_tree(sql_txt)

    # tree.bind("<Double-1>", duplo_click)
    
    # for linha in tree.get_children():
    #     tree.delete(linha)
    
    # for linha in rs:
    #     tree.insert("", tk.END, values=linha)

    # con.fechar()   

    # return True    
    
def gravar():
    ...
    # var_codigo = txtcodigo.get()
    # var_nome = txtnome.get()
    # var_telefone = txttelefone.get()
    # var_email = txtemail.get()
    # var_observacao = txtobservacao.get("1.0","end")

    # con=cn.conexao()
    # sql_txt = f"select codigo,nome,telefone,email,observacao from clientes where codigo = {var_codigo}"

    # rs=con.consultar(sql_txt)

    # if rs:
    #     sql_text = f"update clientes set nome='{var_nome}',telefone='{var_telefone}',email='{var_email}',observacao='{var_observacao}' where codigo = '{var_codigo}'"
    # else:
    #     sql_text = f"insert into clientes(codigo,nome,telefone,email,observacao) values ({var_codigo},'{var_nome}','{var_telefone}','{var_email}','{var_observacao}')"

    # print(sql_text)
    # if con.gravar(sql_text):
    #     messagebox.showinfo("Aviso", "Item Gravado com Sucesso", parent = tela_cli)
    #     limpar()
    # else:
    #     messagebox.showerror("Erro", "Houve um Erro na Gravação", parent = tela_cli)

    # con.fechar()

    # visualizar()    

def excluir():
    ...
    # var_del = messagebox.askyesno("Exclusão", "Tem certeza que deseja excluir?", parent = tela_cli)
    # if var_del == True:
    #     var_codigo = txtcodigo.get()

    #     con=cn.conexao()
    #     sql_text = f"delete from clientes where codigo = '{var_codigo}'"
    #     if con.gravar(sql_text):
    #           messagebox.showinfo("Aviso", "Item Excluído com Sucesso",parent = tela_cli)
    #           limpar()
    #     else:
    #         messagebox.showerror("Erro", "Houve um Erro na Exclusão",parent = tela_cli)
            
    #     con.fechar()

    #     visualizar()
    # else:
    #     limpar()
        
def menu():
    tela_usuario.destroy()
##Funcoes Internas

##Configura Tela
cor_fundo = "black"
cor_fonte = "WhiteSmoke"
fonte = "Roboto"
tela_usuario = MontaTela(cor_fundo,img_background, "Cadastro de Usuário", False)
##Configura Tela

##Implementa Controles
lblUsuario = tk.Label(tela_usuario, text ="Usuario:", bg=cor_fundo, fg=cor_fonte, font=(fonte, 12), anchor = "e")
lblUsuario.place(x = 50, y = 60, width=80,height=25)
entry = tk.Entry(tela_usuario, width = 100)
txtUsuario = tk.Entry(tela_usuario, font=(fonte, 12))
txtUsuario.place(x = 150, y = 60, width = 125, height=25)

lblNome = tk.Label(tela_usuario, text ="Nome:", bg=cor_fundo, fg=cor_fonte, font=(fonte, 12), anchor = "e")
lblNome.place(x = 50, y = 100, width=80, height=25)
txtNome = tk.Entry(tela_usuario, font=(fonte, 12))
txtNome.place(x = 150, y = 100, width = 360, height=25)

lblSenha = tk.Label(tela_usuario, text ="Senha:", bg=cor_fundo, fg=cor_fonte, font=(fonte, 12), anchor = "e")
lblSenha.place(x = 50, y = 140, width=80, height=25)
txtsenha = tk.Entry(tela_usuario, show = "*" , font=(fonte, 12))
txtsenha.place(x = 150, y = 140, width = 125, height=25)

#Botão Menu
imagem = Image.open(icone_voltar)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)
btnmenu = tk.Button(tela_usuario, text ="Menu",image=tkimage, compound='left', foreground='black', font=('Roboto', 12), command=menu, underline=0)
btnmenu.image = tkimage
btnmenu.pack(pady=20)
btnmenu.place(x = 435, y = 180, width = 90)
#Botão Menu

#Botão Limpar
imagem = Image.open(icone_limpar)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)
btnlimpar = tk.Button(tela_usuario, text ="Limpar",image=tkimage, compound='left', foreground='black', font=('Roboto', 12), command=limpar,  underline=0)
btnlimpar.image = tkimage
btnlimpar.pack(pady=20)
PosicionaBotao(tela_usuario, btnmenu, btnlimpar)
#Botão Limpar

#Botão Excluir
imagem = Image.open(icone_excluir)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)
btnexcluir = tk.Button(tela_usuario, text ="Excluir",image=tkimage, compound='left', foreground='black', font=('Roboto', 12), command=excluir, underline=0)
btnexcluir.image = tkimage
btnexcluir.pack(pady=20)
PosicionaBotao(tela_usuario, btnlimpar, btnexcluir)
#Botão Excluir

#Botão Gravar
imagem = Image.open(icone_gravar)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)
btngravar = tk.Button(tela_usuario, text ="Gravar",image=tkimage, compound='left', foreground='black', font=('Roboto', 12), command=gravar, underline=0)
btngravar.image = tkimage
btngravar.pack(pady=20)
PosicionaBotao(tela_usuario, btnexcluir, btngravar)
#Botão Gravar

buscabtn = tk.Button(tela_usuario, text ="Pesquisar", 
                      bg ='white',foreground='black', font=('Calibri', 12, 'bold'))
buscabtn.place(x = 280, y = 60, width = 90, height=25)

##Implementa Controles

style = ttk.Style()

style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=(fonte, 10))
style.configure("mystyle.Treeview.Heading", font=(fonte, 12, "bold"))


tree = ttk.Treeview(tela_usuario, column=("c1", "c2", "c3", "c4"), show='headings', style="mystyle.Treeview", padding=0)

tree.columnconfigure(0, weight=1)
tree.rowconfigure(0, weight=1)

tree.column("#1")
tree.heading("#1", text="Código")
tree.column("#1", width = 100, anchor ='c')

tree.column("#2")
tree.heading("#2", text="Usuario")
tree.column("#2", width = 130, anchor ='c')

tree.column("#3")
tree.heading("#3", text="Nome")
tree.column("#3", width = 250, anchor ='c')

tree.column("#4")
tree.heading("#4", text="Criado Em")
tree.column("#4", width = 200, anchor ='c')


tree.place(x=150, y=230, height=200)

scrollbar = ttk.Scrollbar(tela_usuario, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.place(x = 810, y = 230 , height=200)

txtUsuario.focus_set()

##Configura Atalhos
tela_usuario.bind_all("<Alt-m>", lambda e: menu())
tela_usuario.bind_all("<Alt-l>", lambda e: limpar())
tela_usuario.bind_all("<Alt-e>", lambda e: excluir())
tela_usuario.bind_all("<Alt-g>", lambda e: gravar())
tela_usuario.bind('<Escape>', lambda event: FecharTela(tela_usuario))

##Mantém a Tela Executando
tela_usuario.mainloop()