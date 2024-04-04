import tkinter as tk  #importanto as bibliotecas
import tkinter.font as tkfont

def login():  #Função para verificar o login
    usuario=usertxt.get()
    senha=passtxt.get()
    if (usuario != "admin" or senha != "admin"):  #Senha: admin  /  Usuário: admin 
        bv.config(text="")
        error.config(foreground="red",text="Usuário ou senha incorreto!")
    else:
        error.config(text="")
        bv.config(foreground="Green",text="Bem vindo!")
        

janela = tk.Tk()  #Criando a janela
janela.geometry ("250x210") #Determinando o tamanho da janela
error= tk.Label (janela, text="")  #Mensagem de erro caso o login falhar
error.place(x=60,y=180) #Posição da mensagem de erro

bv=tk.Label (janela,text="")
bv.place(x=100,y=160)

janela.title ("Login")   #Alterando o nome da janela
user= tk.Label(janela, text="Usuário:") #Adicionando a label "Usuário"
user.place(x=60,y=40)  #Posição da label
usertxt=tk.Entry(janela) #Criando text box
usertxt.place(x=60,y=60) #Posição da text box

pasw= tk.Label (janela,text="Senha") #Adicionando a label "Senha"
pasw.place(x=60,y=80)  #Posição da label

passtxt=tk.Entry(janela, show="*") #Criando text box
passtxt.place(x=60,y=100)  #Posição da text box

btlogin= tk.Button(janela, text= "Entrar",command=login) #Criando botão para entrar
btlogin.place(x=60,y=150) #Posição do botão

salvartxt=tk.Label (janela,text="Salvar senha?")
salvartxt.place(x=80,y=121)
salvar= tk.Checkbutton(janela)
salvar.place (x=55,y=120)



janela.mainloop() #Comando que mantém a janela aberta (loop)