# -- coding: utf-8 --
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from funcoes import MontaTela, PosicionaBotao, FecharTela
from vars import *
import conexao as cn

##Funcoes Internas
def limpar():
    txtcodigo.delete(0,"end")
    txtnome.delete(0,"end")
    txttelefone.delete(0,"end")
    txtemail.delete(0,"end")
    txtobservacao.delete("1.0","end")
    txtcodigo.focus_set()
    
def buscar():
    var_codigo = txtcodigo.get()
 
    con=cn.conexao()
    sql_txt = f"select codigo,nome,telefone,email,observacao from clientes where codigo = {var_codigo}"
    rs=con.consultar(sql_txt)

    if rs:
    
        limpar()

        txtcodigo.insert(0, rs[0])
        txtnome.insert(0, rs[1])
        txttelefone.insert(0,rs[2])
        txtemail.insert(0,rs[3])
        txtobservacao.insert("1.0",(rs[4]))
    
    else:
        tk.messagebox.showwarning("Aviso", "Código não Encontrado",parent = tela_cli)
        limpar()
        txtcodigo.focus_set()

    con.fechar()  
    
def duplo_click(event):
    limpar()
    item = tree.item(tree.selection())
    txtcodigo.insert(0, item['values'][0])
    buscar()
    
def visualizar():
    con=cn.conexao()
    sql_txt = f"select * from clientes "
    rs=con.consultar_tree(sql_txt)

    tree.bind("<Double-1>", duplo_click)
    
    for linha in tree.get_children():
        tree.delete(linha)
    
    for linha in rs:
        tree.insert("", tk.END, values=linha)

    con.fechar()    
    
def pesquisar_nome(p):
    con=cn.conexao()
    sql_txt = f"select * from clientes where nome like '%{p}%'"
    
    rs=con.consultar_tree(sql_txt)

    tree.bind("<Double-1>", duplo_click)
    
    for linha in tree.get_children():
        tree.delete(linha)
    
    for linha in rs:
        tree.insert("", tk.END, values=linha)

    con.fechar()   

    return True    
    
def gravar():
    var_codigo = txtcodigo.get()
    var_nome = txtnome.get()
    var_telefone = txttelefone.get()
    var_email = txtemail.get()
    var_observacao = txtobservacao.get("1.0","end")

    con=cn.conexao()
    sql_txt = f"select codigo,nome,telefone,email,observacao from clientes where codigo = {var_codigo}"

    rs=con.consultar(sql_txt)

    if rs:
        sql_text = f"update clientes set nome='{var_nome}',telefone='{var_telefone}',email='{var_email}',observacao='{var_observacao}' where codigo = '{var_codigo}'"
    else:
        sql_text = f"insert into clientes(codigo,nome,telefone,email,observacao) values ({var_codigo},'{var_nome}','{var_telefone}','{var_email}','{var_observacao}')"

    print(sql_text)
    if con.gravar(sql_text):
        messagebox.showinfo("Aviso", "Item Gravado com Sucesso", parent = tela_cli)
        limpar()
    else:
        messagebox.showerror("Erro", "Houve um Erro na Gravação", parent = tela_cli)

    con.fechar()

    visualizar()    

def excluir():
    var_del = messagebox.askyesno("Exclusão", "Tem certeza que deseja excluir?", parent = tela_cli)
    if var_del == True:
        var_codigo = txtcodigo.get()

        con=cn.conexao()
        sql_text = f"delete from clientes where codigo = '{var_codigo}'"
        if con.gravar(sql_text):
              messagebox.showinfo("Aviso", "Item Excluído com Sucesso",parent = tela_cli)
              limpar()
        else:
            messagebox.showerror("Erro", "Houve um Erro na Exclusão",parent = tela_cli)
            
        con.fechar()

        visualizar()
    else:
        limpar()
        
def menu():
    tela_cli.destroy()
##Funcoes Internas

##Configura Tela        
largura_caixa = 90    
tela_cli = MontaTela(cor, img_background,"Cadastro de Clientes", False)
pes_nome = tela_cli.register(func=pesquisar_nome)

#Definição dos Controles
#Insere um Label - anchor w= esquerda, e=direita, c=centralizada
lblcodigo = tk.Label(tela_cli, text ="Codigo:", bg="black", fg="WhiteSmoke", font=('Roboto', 12), anchor = "e")
lblcodigo.place(x = 50, y = 60, width = largura_caixa,  height = 25)
txtcodigo = tk.Entry(tela_cli, width = 35, font=('Roboto', 12))
txtcodigo.place(x = 150, y = 60, width = 100, height = 25)
txtcodigo.place(x = 150, y = 60, width = 100, height = 25)

lblnome = tk.Label(tela_cli, text ="Nome:", bg="black", fg="WhiteSmoke", font=('Roboto', 12), anchor = "e")
lblnome.place(x = 50, y = 100, width = largura_caixa, height = 25)
txtnome = tk.Entry(tela_cli, width = 35, font=('Roboto', 12))
txtnome.place(x = 150, y = 100, width = 375, height = 25)

lbltelefone = tk.Label(tela_cli, text ="Telefone:", bg="black", fg="WhiteSmoke", font=('Roboto', 12), anchor = "e")
lbltelefone.place(x = 50, y = 140, width = largura_caixa, height = 25)
txttelefone = tk.Entry(tela_cli, width = 35, font=('Roboto', 12))
txttelefone.place(x = 150, y = 140, width = 375, height = 25)

lblemail = tk.Label(tela_cli, text ="E-mail:", bg="black", fg="WhiteSmoke", font=('Roboto', 12), anchor = "e")
lblemail.place(x = 50, y = 180, width = largura_caixa, height = 25)
txtemail = tk.Entry(tela_cli, width = 35, font=('Roboto', 12))
txtemail.place(x = 150, y = 180, width = 375, height = 25)

lblobservacao = tk.Label(tela_cli, text ="Observação:", bg="black", fg="WhiteSmoke", font=('Roboto', 12), anchor = "e")
lblobservacao.place(x = 50, y = 220, width = largura_caixa, height = 25)
txtobservacao= tk.Text(tela_cli, font=('Roboto', 12))#Permite Quebra de Linha, diferente do Entry
txtobservacao.place(x=150, y=220, width=375, height=80)

lbl_pes_nome = tk.Label(tela_cli, text ="Pesquisar por Nome :", font=('Roboto', 12, 'bold'), anchor = "w")
lbl_pes_nome.place(x = 150, y = 380, width=200, height = 25)
txt_pes_nome = tk.Entry(tela_cli, width = 35, font=('Roboto', 12),validate='key', validatecommand=(pes_nome,'%P'))
txt_pes_nome.place(x = 315, y = 380, width = 360, height = 25)

#Definição dos Botões
buscabtn = tk.Button(tela_cli, text ="Pesquisar", 
                     bg ='white',foreground='black', font=('Roboto', 12, 'bold'), command = buscar)
buscabtn.place(x = 280, y = 60, width = 90, height = 25)

#Botão Menu
imagem = Image.open(icone_voltar)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)
btnmenu = tk.Button(tela_cli, text ="Menu",image=tkimage, compound='left', foreground='black', font=('Roboto', 12), command=menu, underline=0)
btnmenu.image = tkimage
btnmenu.pack(pady=20)
btnmenu.place(x = 435, y = 320, width = 90)
#Botão Menu

#Botão Limpar
imagem = Image.open(icone_limpar)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)
btnlimpar = tk.Button(tela_cli, text ="Limpar",image=tkimage, compound='left', foreground='black', font=('Roboto', 12), command=limpar, underline=0)
btnlimpar.image = tkimage
btnlimpar.pack(pady=20)
PosicionaBotao(tela_cli, btnmenu, btnlimpar)
#Botão Limpar

#Botão Excluir
imagem = Image.open(icone_excluir)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)
btnexcluir = tk.Button(tela_cli, text ="Excluir",image=tkimage, compound='left', foreground='black', font=('Roboto', 12), command=excluir, underline=0)
btnexcluir.image = tkimage
btnexcluir.pack(pady=20)
PosicionaBotao(tela_cli, btnlimpar, btnexcluir)
#Botão Excluir

#Botão Gravar
imagem = Image.open(icone_gravar)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)
btngravar = tk.Button(tela_cli, text ="Gravar",image=tkimage, compound='left', foreground='black', font=('Roboto', 12), command=gravar, underline=0)
btngravar.image = tkimage
btngravar.pack(pady=20)
PosicionaBotao(tela_cli, btnexcluir, btngravar)
#Botão Gravar

##Configuração Grid
style = tk.ttk.Style()
style.configure("mystyle.Treeview", font=("Roboto", 10))
style.configure("mystyle.Treeview.Heading", font=("Roboto", 12, "bold"))

tree = tk.ttk.Treeview(tela_cli, column=("c1", "c2", "c3", "c4", "c5"), show='headings', style="mystyle.Treeview")

tree.column("#1")
tree.heading("#1", text="Código")
tree.column("#1", width = 100, anchor ='c')

tree.column("#2")
tree.heading("#2", text="Nome")
tree.column("#2", width = 200, anchor ='c')

tree.column("#3")
tree.heading("#3", text="Telefone")
tree.column("#3", width = 100, anchor ='w')

tree.column("#4")
tree.heading("#4", text="E-mail")
tree.column("#4", width = 150, anchor ='c')

tree.column("#5")
tree.heading("#5", text="Observação")
tree.column("#5", width = 300, anchor ='c')

tree.place(x=150,y=430,height=150)
##Configuração Grid

##Configuração ScrollBar
scrollbar = tk.ttk.Scrollbar(tela_cli, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.place(x = 982, y = 430,height=150)
##Configuração ScrollBar

##Ações Inicializar
visualizar()
txtcodigo.focus_set()

##Configura Atalhos
tela_cli.bind_all("<Alt-m>", lambda e: menu())
tela_cli.bind_all("<Alt-l>", lambda e: limpar())
tela_cli.bind_all("<Alt-e>", lambda e: excluir())
tela_cli.bind_all("<Alt-g>", lambda e: gravar())
tela_cli.bind('<Escape>', lambda event: FecharTela(tela_cli))

#Mantêm a tela_cli em Execução
tela_cli.mainloop()

