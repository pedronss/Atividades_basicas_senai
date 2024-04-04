import os
class Livro:
    def __init__(self,titulo,autor,num_paginas,pagina_atual):
        self.titulo=titulo
        self.autor=autor
        self.num_paginas=num_paginas
        self.pagina_atual=pagina_atual
    def avancarPag(self):
        if self.pagina_atual < self.num_paginas:
            self.pagina_atual+=1
    def voltarPag(self):
        if self.pagina_atual >0:
            self.pagina_atual-=1

livro = Livro("Aventuras de André","André",10,1)
while(True):
    os.system('cls')
    print(f"Titulo: {livro.titulo}\nAutor: {livro.autor}\nNúmero de páginas: {livro.num_paginas}\nPagina atual: {livro.pagina_atual}")
    print("\n(1)Avançar Pagina\n(2)Voltar Pagina")
    option= int(input("O que deseja fazer?\n"))
    if option == 1:
        livro.avancarPag()
    if option == 2:
        livro.voltarPag()