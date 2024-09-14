# -- coding: utf-8 --
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from funcoes import MontaTela, PosicionaBotao, FecharTela
from vars import *
import conexao as cn

cor = "WhiteSmoke"
largura_caixa = 100

def menu():
    tela_vendas.destroy()
##Funcoes Internas
def limpar():
    ...
    # txtcodigo.delete(0,"end")
    # txtnome.delete(0,"end")
    # txttelefone.delete(0,"end")
    # txtemail.delete(0,"end")
    # txtobservacao.delete("1.0","end")
    # txtcodigo.focus_set()
    
def buscar():
    ...
    # var_codigo = txtcodigo.get()
 
    # con=cn.conexao()
    # sql_txt = f"select codigo,nome,telefone,email,observacao from clientes where codigo = {var_codigo}"
    # rs=con.consultar(sql_txt)

    # if rs:
    
    #     limpar()

    #     txtcodigo.insert(0, rs[0])
    #     txtnome.insert(0, rs[1])
    #     txttelefone.insert(0,rs[2])
    #     txtemail.insert(0,rs[3])
    #     txtobservacao.insert("1.0",(rs[4]))
    
    # else:
    #     tk.messagebox.showwarning("Aviso", "Código não Encontrado",parent = tela_cli)
    #     limpar()
    #     txtcodigo.focus_set()

    # con.fechar()  
    
def duplo_click(event):
    ...
    # limpar()
    # item = tree.item(tree.selection())
    # txtcodigo.insert(0, item['values'][0])
    # buscar()
    
def visualizar():
    ...
    # con=cn.conexao()
    # sql_txt = f"select * from clientes "
    # rs=con.consultar_tree(sql_txt)

    # tree.bind("<Double-1>", duplo_click)
    
    # for linha in tree.get_children():
    #     tree.delete(linha)
    
    # for linha in rs:
    #     tree.insert("", tk.END, values=linha)

    # con.fechar()    
    
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
    
##Configura Tela        
tela_vendas = MontaTela(cor, img_background,"Cadastro de Vendas", False)

#Definição dos Controles
#Insere um Label - anchor w= esquerda, e=direita, c=centralizada
lblnumero = tk.Label(tela_vendas, text ="Num. Venda:", bg="black", fg="WhiteSmoke", font=('Roboto', 12), anchor = "e")
lblnumero.place(x = 50, y = 60, width = largura_caixa,  height = 25)
lblnumero = tk.Entry(tela_vendas, width = 35, font=('Roboto', 12))
lblnumero.place(x = 150, y = 60, width = 100, height = 25)

lblcodigo = tk.Label(tela_vendas, text ="Codigo:", bg="black", fg="WhiteSmoke", font=('Roboto', 12), anchor = "e")
lblcodigo.place(x = 50, y = 100, width = largura_caixa,  height = 25)
txtcodigo = tk.Entry(tela_vendas, width = 35, font=('Roboto', 12))
txtcodigo.place(x = 150, y = 100, width = 100, height = 25)

lblnome = tk.Label(tela_vendas, text ="Nome:", bg="black", fg="WhiteSmoke", font=('Roboto', 12), anchor = "e")
lblnome.place(x = 50, y = 140, width = largura_caixa, height = 25)
txtnome = tk.Entry(tela_vendas, width = 35, font=('Roboto', 12))
txtnome.place(x = 150, y = 140, width = 500, height = 25)

lblcodigoproduto = tk.Label(tela_vendas, text ="Cód. Produto:", bg="black", fg="WhiteSmoke", font=('Roboto', 12), anchor = "e")
lblcodigoproduto.place(x = 50, y = 180, width = largura_caixa, height = 25)
txtcodigoproduto = tk.Entry(tela_vendas, width = 35, font=('Roboto', 12))
txtcodigoproduto.place(x = 150, y = 180, width = 500, height = 25)

lbldescricaoproduto = tk.Label(tela_vendas, text ="Descrição:", bg="black", fg="WhiteSmoke", font=('Roboto', 12), anchor = "e")
lbldescricaoproduto.place(x = 50, y = 220, width = largura_caixa, height = 25)
txtdescricaoproduto= tk.Entry(tela_vendas, font=('Roboto', 12))#Permite Quebra de Linha, diferente do Entry
txtdescricaoproduto.place(x=150, y=220, width=500, height=25)

lblQtdproduto = tk.Label(tela_vendas, text ="Qtd. Produto:", bg="black", fg="WhiteSmoke", font=('Roboto', 12), anchor = "e")
lblQtdproduto.place(x = 50, y = 260, width = largura_caixa, height = 25)
txtQtdproduto = tk.Entry(tela_vendas, width = 35, font=('Roboto', 12))
txtQtdproduto.place(x = 150, y = 260, width = 100, height = 25)

lblValorunitario = tk.Label(tela_vendas, text ="Vl.Unitário:", bg="black", fg="WhiteSmoke", font=('Roboto', 12), anchor = "e")
lblValorunitario.place(x = 250, y = 260, width = largura_caixa, height = 25)
txtValorunitario = tk.Entry(tela_vendas, width = 35, font=('Roboto', 12))
txtValorunitario.place(x = 350, y = 260, width = 100, height = 25)

lblValortotal = tk.Label(tela_vendas, text ="Vl.Total:", bg="black", fg="WhiteSmoke", font=('Roboto', 12), anchor = "e")
lblValortotal.place(x = 450, y = 260, width = largura_caixa, height = 25)
txtValortotal = tk.Entry(tela_vendas, width = 35, font=('Roboto', 12))
txtValortotal.place(x = 550, y = 260, width = 100, height = 25)

#Botão Excluir Produto
imagem = Image.open(icone_excluir)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)
btnmenu = tk.Button(tela_vendas, text ="Excluir",image=tkimage, compound='left', foreground='black', font=('Roboto', 12), command=menu, underline=0)
btnmenu.image = tkimage
btnmenu.pack(pady=20)
btnmenu.place(x = 560, y = 320, width = 90)
#Botão Excluir Produto

#Botão Limpar Produto
imagem = Image.open(icone_limpar)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)
btnmenu = tk.Button(tela_vendas, text ="Limpar",image=tkimage, compound='left', foreground='black', font=('Roboto', 12), command=menu, underline=0)
btnmenu.image = tkimage
btnmenu.pack(pady=20)
btnmenu.place(x = 360, y = 320, width = 90)
#Botão Limpar Produto

#Botão Incluir Produto
imagem = Image.open(icone_gravar)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)
btnmenu = tk.Button(tela_vendas, text ="Incluir",image=tkimage, compound='left', foreground='black', font=('Roboto', 12), command=menu, underline=0)
btnmenu.image = tkimage
btnmenu.pack(pady=20)
btnmenu.place(x = 160, y = 320, width = 90)
#Botão LiIncluirmpar Produto

##Configuração Grid
style = tk.ttk.Style()
style.configure("mystyle.Treeview", font=("Roboto", 10))
style.configure("mystyle.Treeview.Heading", font=("Roboto", 12, "bold"))

tree = tk.ttk.Treeview(tela_vendas, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings', style="mystyle.Treeview")

tree.column("#1")
tree.heading("#1", text="Linha")
tree.column("#1", width = 100, anchor ='c')

tree.column("#2")
tree.heading("#2", text="Código")
tree.column("#2", width = 200, anchor ='c')

tree.column("#3")
tree.heading("#3", text="Descrição")
tree.column("#3", width = 100, anchor ='w')

tree.column("#4")
tree.heading("#4", text="Quantidade")
tree.column("#4", width = 150, anchor ='c')

tree.column("#5")
tree.heading("#5", text="Vl. Unitário")
tree.column("#5", width = 300, anchor ='c')

tree.column("#6")
tree.heading("#6", text="Vl. Total")
tree.column("#6", width = 300, anchor ='c')

tree.place(x=150,y=380,height=150)
##Configuração Grid

##Configuração ScrollBar
scrollbar = tk.ttk.Scrollbar(tela_vendas, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.place(x = 1300, y = 380,height=150)
##Configuração ScrollBar

#Botão Menu
imagem = Image.open(icone_voltar)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)
btnmenu = tk.Button(tela_vendas, text ="Menu",image=tkimage, compound='left', foreground='black', font=('Roboto', 12), command=menu, underline=0)
btnmenu.image = tkimage
btnmenu.pack(pady=20)
btnmenu.place(x = 1220, y = 550, width = 100)
#Botão Menu

#Botão Cancelar
imagem = Image.open(icone_cancelar)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)
btncancelar = tk.Button(tela_vendas, text ="Cancelar",image=tkimage, compound='left', foreground='black', font=('Roboto', 12), command=limpar, underline=0)
btncancelar.image = tkimage
btncancelar.pack(pady=20)
PosicionaBotao(tela_vendas, btnmenu, btncancelar)
#Botão Cancelar

#Botão Imprimir
imagem = Image.open(icone_imprimir)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)
btnImprimir = tk.Button(tela_vendas, text ="Imprimir",image=tkimage, compound='left', foreground='black', font=('Roboto', 12), command=limpar, underline=0)
btnImprimir.image = tkimage
btnImprimir.pack(pady=20)
PosicionaBotao(tela_vendas, btncancelar, btnImprimir)
#Botão Imprimir

#Botão Gravar
imagem = Image.open(icone_gravar)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)
btngravar = tk.Button(tela_vendas, text ="Gravar",image=tkimage, compound='left', foreground='black', font=('Roboto', 12), command=gravar, underline=0)
btngravar.image = tkimage
btngravar.pack(pady=20)
PosicionaBotao(tela_vendas, btnImprimir, btngravar)
#Botão Gravar


tela_vendas.bind('<Escape>', lambda event: FecharTela(tela_vendas))

#Mantêm a tela_cli em Execução
tela_vendas.mainloop()

