import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

# Dados de exemplo
carros = [
    {'marca': 'vw', 'modelo': 'gol', 'ano': 2018, 'preco': 45000},
    {'marca': 'ford', 'modelo': 'ka', 'ano': 2014, 'preco': 38000},
    {'marca': 'honda', 'modelo': 'civic', 'ano': 2010, 'preco': 40000},
    {'marca': 'honda', 'modelo': 'fit', 'ano': 2014, 'preco': 48000},
    {'marca': 'vw', 'modelo': 'jetta', 'ano': 2013, 'preco': 49000},
    {'marca': 'ford', 'modelo': 'focus', 'ano': 2017, 'preco': 62000},
]

# Função para imprimir ordenado
def imprimir_ordenado(criterio):
    texto_area.delete("1.0", tk.END)
    ordenados = sorted(carros, key=lambda item: item[criterio])
    texto_area.insert(tk.END, "Marca\tModelo\t\tAno\tPreço\n")
    texto_area.insert(tk.END, '---------------------------------------\n')

    for item in ordenados:
        texto_area.insert(tk.END, f"{item['marca']}\t{item['modelo']}\t\t{item['ano']}\t{item['preco']} \n")
    
    texto_area.insert(tk.END, '---------------------------------------')

# Configuração da janela
janela = ThemedTk(theme="radiance")  # Escolhendo o tema "radiance"
janela.geometry("800x600")
janela.title("Busca de Veículos")

# Estilizando o título
titulo = ttk.Label(janela, text="Busca de Veículos", font=("Helvetica", 30, "bold"), foreground="#333", background="#F4F4F4")
titulo.pack(pady=20)

# Estilizando os botões
estilo_botao = ttk.Style()
estilo_botao.configure("TButton", font=("Helvetica", 16), foreground="#F4F4F4", background="#333", width=20)

botao_marca = ttk.Button(janela, text="Ordenar por Marca", command=lambda: imprimir_ordenado('marca'))
botao_modelo = ttk.Button(janela, text="Ordenar por Modelo", command=lambda: imprimir_ordenado('modelo'))
botao_ano = ttk.Button(janela, text="Ordenar por Ano", command=lambda: imprimir_ordenado('ano'))
botao_preco = ttk.Button(janela, text="Ordenar por Preço", command=lambda: imprimir_ordenado('preco'))

botao_marca.pack(pady=10)
botao_modelo.pack(pady=10)
botao_ano.pack(pady=10)
botao_preco.pack(pady=10)

# Estilizando o Text Area
texto_area = tk.Text(janela, height=9, width=70, font=("Arial", 14))
texto_area.pack(pady=20)

janela.mainloop()
