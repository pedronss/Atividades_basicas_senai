import os
class Conta:
    def __init__(self,titular,saldo):
        self.titular=titular
        self.saldo=saldo
    def setDeposito(self,deposito):
        self.saldo=self.saldo+deposito
    def setSaque(self,saque):
        if saque <= self.saldo:
            self.saldo=self.saldo-saque
        else:
            print("\033[31mSaldo insuficiente na conta.\033[0m")
            input("Pressione enter para continuar...")
conta=Conta("Pedro Nogueira Stephan",400)
while(True):
    os.system('cls')
    print(f"Titular: {conta.titular}\nSaldo: {conta.saldo}")
    print("\n(1)Depositar\n(2)Sacar")
    option= int(input("O que deseja fazer?\n"))
    if option ==1:
        deposito=int(input("Qual o valor do depósito?"))
        conta.setDeposito(deposito)
    if option == 2:
        saque=int(input("Qual o valor do saque?"))
        conta.setSaque(saque)