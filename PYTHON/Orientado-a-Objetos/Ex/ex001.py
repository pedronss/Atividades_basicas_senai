#Criando uma classe com o nome de carro
class Carro:
    #Criando um método para exibir as informações de um carro
    def info(self):
        print(f"\nMarca: {self.marca} \nModelo: {self.modelo} \nAno: {self.ano}")

#Criando uma instância da classe carro
carro1=Carro()
carro1.marca= "VW"
carro1.modelo= "Gol"
carro1.ano="2012"
#Criando uma instância da classe carro
carro2=Carro()  
carro2.marca= "Ford"
carro2.modelo= "Fiesta"
carro2.ano="2016"
#Criando uma instância da classe carro
carro3=Carro()
carro3.marca="Fiat"
carro3.modelo= "Uno"
carro3.ano="2016"

#Declarando variaveis que recebem os atributos do carro
gol=carro1.marca,carro1.modelo,carro1.ano
fiesta=carro2.marca,carro2.modelo,carro2.ano
fiatuno=carro3.marca,carro3.modelo,carro3.ano

#Imprimindo com for
for atributos in fiesta,gol,fiatuno:
    print(*atributos)

#Imprimindo com o metodo criado
carro1.info()

#Imprimindo usando a concatenação
print(f"\nMarca: {carro1.marca} \nModelo: {carro1.modelo} \nAno: {carro1.ano}")
print(f"\nMarca: {carro2.marca} \nModelo: {carro2.modelo} \nAno: {carro2.ano}")
print(f"\nMarca: {carro3.marca} \nModelo: {carro3.modelo} \nAno: {carro3.ano}")


