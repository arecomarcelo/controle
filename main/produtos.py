# -- coding: utf-8 --
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from funcoes import MontaTela, PosicionaBotao, FecharTela
from vars import *
import conexao as cn
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

largura_caixa = 90

def limpar():
    txtcodigo.delete(0,"end")
    txtdescricao.delete(0,"end")
    cmbtipo.delete(0,"end")
    txtquantidade.delete(0,"end")
    txtcusto.delete(0,"end")
    txtpreco.delete(0,"end")
    txtcodigo.focus_set()
    
def buscar():
    var_codigo = txtcodigo.get()
 
    con=cn.conexao()
    sql_txt = f"select codigo,descricao,tipo,quantidade,custo,preco from prodserv where codigo = {var_codigo}"
    rs=con.consultar(sql_txt)

    if rs:
    
        limpar()

        txtcodigo.insert(0, rs[0])
        txtdescricao.insert(0, rs[1])
        cmbtipo.insert(0,rs[2])
        txtquantidade.insert(0,rs[3])
        txtcusto.insert(0,locale.currency(rs[4]))
        txtpreco.insert(0,locale.currency(rs[5]))
    else:
        messagebox.showwarning("Aviso", "Código não Encontrado",parent = tela_prod)
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
    #sql_txt = "select codigo,descricao,tipo,quantidade,custo,preco from prodserv order by descricao"
    sql_txt = "select * from prodserv order by descricao"
    rs=con.consultar_tree(sql_txt)

    tree.bind("<Double-1>", duplo_click)
    
    for linha in tree.get_children():
        tree.delete(linha)
    
    for linha in rs:
        tree.insert("", tk.END, values=linha)

def gravar():
    var_codigo = txtcodigo.get()
    var_tipo = cmbtipo.get()
    var_descricao = txtdescricao.get()
    var_quantidade = txtquantidade.get()
    var_custo = txtcusto.get()
    var_custo = float(var_custo.replace('R$', '').strip().replace('.', '').replace(',', '.'))
    var_preco = txtpreco.get()
    var_preco = float(var_preco.replace('R$', '').strip().replace('.', '').replace(',', '.'))

    con=cn.conexao()
    sql_txt = f"select codigo,descricao,tipo,quantidade,custo,preco from prodserv where codigo = '{var_codigo}'"

    rs=con.consultar(sql_txt)

    if rs:
        sql_text = f"update prodserv set tipo='{var_tipo}',descricao='{var_descricao}',quantidade={var_quantidade},custo={var_custo},preco={var_preco} where codigo = '{var_codigo}'"
    else:
        sql_text = f"insert into prodserv(codigo,tipo,descricao,quantidade,custo,preco) values ('{var_codigo}','{var_tipo}','{var_descricao}',{var_quantidade},{var_custo},{var_preco})"

    if con.gravar(sql_text):
        messagebox.showinfo("Aviso", "Item Gravado com Sucesso",parent = tela_prod)
        limpar()
    else:
        messagebox.showerror("Erro", "Houve um Erro na Gravação",parent = tela_prod)

    con.fechar()

    visualizar()

def excluir():
    var_del = messagebox.askyesno("Exclusão", "Tem certeza que deseja excluir?",parent = tela_prod)
    if var_del == True:
        var_codigo = txtcodigo.get()

        con=cn.conexao()
        sql_text = f"delete from prodserv where codigo = '{var_codigo}'"
        if con.gravar(sql_text):
              messagebox.showinfo("Aviso", "Item Excluído com Sucesso",parent = tela_prod)
              limpar()
        else:
            messagebox.showerror("Erro", "Houve um Erro na Exclusío",parent = tela_prod)

        con.fechar()

        visualizar()
    else:
        limpar()
    
def menu():
    tela_prod.destroy()

tela_prod = MontaTela(cor, img_background,"Cadastro de Produtos e Serviços", False)

    
#Definição dos Controles
lblcodigo = tk.Label(tela_prod, text ="Codigo:", bg=cor_fundo, fg=cor_fonte, font=(fonte, 12), anchor = "e")
lblcodigo.place(x = 50, y = 60, width = largura_caixa,  height = 25)
txtcodigo = tk.Entry(tela_prod, width = 35, font=(fonte, 12))
txtcodigo.place(x = 150, y = 60, width = 100, height = 25)

lbltipo = tk.Label(tela_prod, text ="Tipo:", bg=cor_fundo, fg=cor_fonte, font=(fonte, 12), anchor = 'e')
lbltipo.place(x = 50, y = 100, width = 90)
tipos = ["PRODUTO", "SERVICO"]
cmbtipo = ttk.Combobox(tela_prod, values=tipos, font=(fonte, 10))
cmbtipo.place(x=150, y=100, width=120, height = 25)
# cmbtipo.current(0)

lbldescricao = tk.Label(tela_prod, text ="Descrição:", bg=cor_fundo, fg=cor_fonte, font=(fonte, 12), anchor = 'e')
lbldescricao.place(x = 50, y = 140, width = 90)
entry = tk.Entry(tela_prod, font=('Calibri', 12))
txtdescricao =  tk.Entry(tela_prod, font=(fonte, 12))
txtdescricao.place(x = 150, y = 140, width = 400)

lblquantidade = tk.Label(tela_prod, text ="Quantidade:", bg=cor_fundo, fg=cor_fonte, font=(fonte, 12), anchor = 'e')
lblquantidade.place(x = 50, y = 180, width = 90)
txtquantidade = tk.Entry(tela_prod, font=(fonte, 12))
txtquantidade.place(x = 150, y = 180, width = 120)

lblcusto = tk.Label(tela_prod, text ="Custo:", bg=cor_fundo, fg=cor_fonte, font=(fonte, 12), anchor = 'e')
lblcusto.place(x = 50, y = 220, width = 90)
txtcusto = tk.Entry(tela_prod, font=('Calibri', 12))
txtcusto.place(x = 150, y = 220, width = 120)

lblpreco = tk.Label(tela_prod, text ="Preço:", bg=cor_fundo, fg=cor_fonte, font=(fonte, 12), anchor = 'e')
lblpreco.place(x = 50, y = 260, width = 90)
txtpreco = tk.Entry(tela_prod, font=('Calibri', 12))
txtpreco.place(x = 150, y = 260, width = 120)
#Definição dos Controles

#Botão Menu
imagem = Image.open(icone_voltar)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)
btnmenu = tk.Button(tela_prod, text ="Menu",image=tkimage, compound='left', foreground='black', font=('Roboto', 12), command=menu, underline=0)
btnmenu.image = tkimage
btnmenu.pack(pady=20)
btnmenu.place(x = 435, y = 300, width = 90)
#Botão Menu

#Botão Limpar
imagem = Image.open(icone_limpar)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)
btnlimpar = tk.Button(tela_prod, text ="Limpar",image=tkimage, compound='left', foreground='black', font=('Roboto', 12),command=limpar,  underline=0)
btnlimpar.image = tkimage
btnlimpar.pack(pady=20)
PosicionaBotao(tela_prod, btnmenu, btnlimpar)
#Botão Limpar

#Botão Excluir
imagem = Image.open(icone_excluir)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)
btnexcluir = tk.Button(tela_prod, text ="Excluir",image=tkimage, compound='left', foreground='black', font=('Roboto', 12),command=excluir,  underline=0)
btnexcluir.image = tkimage
btnexcluir.pack(pady=20)
PosicionaBotao(tela_prod, btnlimpar, btnexcluir)
#Botão Excluir

#Botão Gravar
imagem = Image.open(icone_gravar)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)
btngravar = tk.Button(tela_prod, text ="Gravar",image=tkimage, compound='left', foreground='black', font=('Roboto', 12),command=gravar,  underline=0)
btngravar.image = tkimage
btngravar.pack(pady=20)
PosicionaBotao(tela_prod, btnexcluir, btngravar)
#Botão Gravar

style = ttk.Style()

style.configure("mystye.Treeview", font=("Calibri", 10))
style.configure("mystyle.Treeview.Heading", font=("Calibri", 12, "bold"))

tree = ttk.Treeview(tela_prod, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings', style="mystyle.Treeview", padding=0)

tree.columnconfigure(0, weight=1)
tree.rowconfigure(0, weight=1)

tree.column("#1")
tree.heading("#1", text="Código")
tree.column("#1", width = 100, anchor ='c')

tree.column("#2")
tree.heading("#2", text="Tipo")
tree.column("#2", width = 80, anchor ='c')

tree.column("#3")
tree.heading("#3", text="Descrição")
tree.column("#3", width = 200, anchor ='w')

tree.column("#4")
tree.heading("#4", text="Quantidade")
tree.column("#4", width = 100, anchor ='c')

tree.column("#5")
tree.heading("#5", text="Custo")
tree.column("#5", width = 100, anchor ='c')

tree.column("#6")
tree.heading("#6", text="Preço")
tree.column("#6", width = 100, anchor ='c')

tree.place(x=150,y=350,height=200)

scrollbar = ttk.Scrollbar(tela_prod, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.place(x = 831, y = 350,height=200)

visualizar()

txtcodigo.focus_set()


tela_prod.bind('<Escape>', lambda event: FecharTela(tela_prod))

#Mantêm a tela_prod em Execução
tela_prod.mainloop()

