import os
class Carro:
    def __init__(self,marca,modelo,tanque_combustivel,consumo):
        self.marca=marca
        self.modelo=modelo
        self.tanque_combustivel=tanque_combustivel
        self.consumo=consumo
        self.km=0
    def dirigir(self):
        self.km+=1
        self.tanque_combustivel-=self.consumo
    def abastecer(self,combustivel):
        if combustivel > 0 and combustivel <= 64 and self.tanque_combustivel < 64 and combustivel+self.tanque_combustivel < 64:
            self.tanque_combustivel=self.tanque_combustivel+combustivel
        else:
            print("Valor inválido")
            input("Pressione enter para continuar...")
carro=Carro("Porsche","911",64,12)
while(True):
    os.system('cls')
    print(f"Marca: {carro.marca}\nModelo: {carro.modelo}\nTanque: {carro.tanque_combustivel}\nConsumo: {carro.consumo}\nKm percorrido: {carro.km}")
    print("\n(1)Dirigir\n(2)Abastecer")
    option= int(input("O que deseja fazer?\n"))
    if option ==1:
        carro.dirigir()
    if option == 2:
        quant=int(input("Qual a quantidade de combustivel ?"))
        carro.abastecer(quant)