import os
os.system('cls')

class Clientes:
    def getSaldo(self):
        return self.saldo
    def addSaldo(self):
        saldo = int(input("Digite o valor:"))
        self.saldo= self.saldo+saldo
    def transferir(self,destino,valor):
        self.saldo = self.saldo-valor-15
        destino.saldo = destino.saldo+valor   
    def showInfo(self):
        print(f"Nome: {self.nome}\nSaldo: {self.saldo}\n")
class Ouro(Clientes):
    def transferir(self,destino,valor):
        super().transferir(destino,valor)
        self.saldo = self.saldo - (2*valor)/100
class Prata(Clientes):
    def transferir(self,destino,valor):
        super().transferir(destino,valor)
        self.saldo = self.saldo - (5*valor)/100
class Bronze(Clientes):
    def transferir(self,destino,valor):
        super().transferir(destino,valor)
        self.saldo = self.saldo - (10*valor)/100

def transf():
    os.system('cls')
    valor= int(input("Qual o valor deseja tranferir?"))
    print(f"\nPra quem deseja transferir?\n(1){c2.nome}(Bronze)\n(2){c3.nome}(Prata)\n(3){c4.nome}(Ouro)\n")
    opcao = int(input(""))
    
    match opcao:
        case 1:
            if c1.saldo >= valor+15 + (10*valor)/100:
                c1.transferir(c2,valor)
            else:
                print("\nSaldo insuficiente!")
                input("\nPressione enter para continuar...")
        case 1:
            if c1.saldo >= valor+15 + (5*valor)/100:
                c1.transferir(c3,valor)
            else:
                print("\nSaldo insuficiente!")
                input("\nPressione enter para continuar...")
        case 1:
            if c1.saldo >= valor+15 + (2*valor)/100:
                c1.transferir(c4,valor)
            else:
                print("\nSaldo insuficiente!")
                input("\nPressione enter para continuar...")

c1=Ouro()
c1.saldo=100

c2=Bronze()
c2.nome="Marcia"
c2.saldo=0

c3=Prata()
c3.nome="Claudio"
c3.saldo=0

c4=Ouro()
c4.nome="Douglas"
c4.saldo=0
while True:
    os.system('cls')
    print(f"Saldo: {c1.saldo}")
    print("\nVocê é Ouro!\n")
    print("(1)Transferir\n(2)Adicionar Saldo\n(3)Ver contatos")
    opcao= int(input(""))
    match opcao:
        case 1:
            transf()
        case 2:
            c1.addSaldo()
        case 3:
            os.system('cls')
            c2.showInfo()
            c3.showInfo()
            c4.showInfo()
            input("\nPressione enter para continuar...")