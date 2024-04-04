import os
class Pessoa:
    def __init__(self,nome,idade,altura):
        self.nome=nome
        self.altura=altura   
        if idade < 120 and idade > 0:
            self.idade=idade
    def falar(self):
        print (f"{self.nome} está falando ...")
        input ("Pressione enter para continuar")
    def aniversário(self):
        self.idade +=1
        print()
p=Pessoa("Pedro",17,1.82)
while(True):
    os.system('cls')
    print(f"Nome: {p.nome}\nIdade: {p.idade}\nAltura: {p.altura} ")
    print("\n(1)Falar\n(2)Fazer Aniversário")
    option= int(input("O que deseja fazer?\n"))
    if option ==1:
        p.falar()
    if option == 2:
        p.aniversário()