import os
os.system('cls')

class Veiculo:
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
    def ligar(self):
        print(f"{self.modelo} está ligado!")
    def desligar(self):
        print(f"{self.modelo} está desligado!")
class Carro(Veiculo):
    def __init__(self,marca,modelo,num_de_portas):
        super().__init__(marca,modelo)
        self.num_de_portas=num_de_portas
    def destravar_porta(self):
        print(f"As portas do {self.modelo} foram destravadas!")

class Moto(Veiculo):
    def __init__(self,marca,modelo):
        super().__init__(marca,modelo)
    def grau(self):
        print(f"Dando grau na {self.modelo}!")

class Carro_eletrico(Carro):
    def __init__(self,marca,modelo,num_de_portas):
        super().__init__(marca,modelo,num_de_portas)
    def recarregar(self):
        print(f"{self.modelo} está carregando...")


c1= Carro("Honda","Civic",4)

c2= Carro_eletrico("Tesla","Model X",4)
c2.destravar_porta()
c2.ligar()
c2.recarregar()
m1= Moto("Yamaha","Crosser")
                                                                  