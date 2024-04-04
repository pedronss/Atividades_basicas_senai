import tkinter as tk
import os
from tkinter import font
carros=[
    {'marca':'vw','modelo':'gol','ano':2018,'preco':45000},
    {'marca':'ford','modelo':'ka','ano':2014,'preco':38000},
    {'marca':'honda','modelo':'civic','ano':2010,'preco':40000},
    {'marca':'honda','modelo':'fit','ano':2014,'preco':48000},
    {'marca':'vw','modelo':'jetta','ano':2013,'preco':49000},
    {'marca':'ford','modelo':'focus','ano':2017,'preco':62000},
]

def imprimir_ordenado(criterio):
    texto_area = tk.Text(janela, height=9, width=40)
    texto_area.place(x=200,y=150)
    ordenados = sorted(carros, key=lambda item: item[criterio])
    # Limpa o Text Area se já houver algo
    texto_area.delete("1.0", tk.END)
    # Cabeçalho
    texto_area.insert(tk.END, "Marca\tModelo\t\tAno\tPreço\n")
    texto_area.insert(tk.END, '---------------------------------------\n')

    # Conteúdo ordenado
    for item in ordenados:
        texto_area.insert(tk.END, f"{item['marca']}\t{item['modelo']}\t\t{item['ano']}\t{item['preco']} \n")
    
    texto_area.insert(tk.END, '---------------------------------------')

janela=tk.Tk()
janela.geometry("600x400")
janela.maxsize(700,500)
titulo=font.Font(family="Helvetica", size=12, weight="bold")
label=tk.Label(janela,text="Busca de Veículos(Ordem)",font=titulo)
label.place(x=250,y=100) 
marca=tk.Button(janela,text="Marca",command=lambda: imprimir_ordenado('marca'))
marca.place(x=65,y=150,height=30, width=50) 

modelo=tk.Button(janela,text="Modelo",command=lambda: imprimir_ordenado('modelo'))
modelo.place(x=65,y=190,height=30, width=50)

ano=tk.Button(janela,text="Ano",command=lambda: imprimir_ordenado('ano'))
ano.place(x=65,y=230,height=30, width=50)

preco=tk.Button(janela,text="Preço",command=lambda: imprimir_ordenado('preco'))
preco.place(x=65,y=270,height=30, width=50)

texto_area = tk.Text(janela, height=9, width=40)
texto_area.place(x=200,y=150)


janela.mainloop()