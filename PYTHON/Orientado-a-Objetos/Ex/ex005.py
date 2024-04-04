import os
os.system('cls')


class Funcionario:
    def __init__(self,nome,salario):
        self.nome=nome
        self.salario=salario
    def addAumento(self,valor):
        self.salario=self.salario+valor
    def ganhoAnual(self):
        print(f"{self.nome} ganha R$ {self.salario*12} por ano!")
    def exibirDados(self):
        print(f"Nome: {self.nome}\nSalário: R${self.salario}")

class Assistente(Funcionario):
    def __init__(self,nome,salario,matricula):
        super().__init__(nome,salario)
        self.matricula=matricula
    def getNome(self):
        return self.nome
    def getSalario(self):
        return self.salario
    def getMatricula(self):
        return self.matricula
    def setNome(self,nome):
        self.nome=nome
    def setSalario(self,salario):
        self.salario=salario
    def setMatricula(self,matricula):
        self.matricula=matricula

class Tecnico(Assistente):
    def __init__(self,nome,salario,matricula,):
        bonus=750
        super().__init__(nome,salario,matricula)
        self.salario = self.salario+bonus
    def exibirDados(self):
        super().exibirDados()
        print("Cargo: Assistente Técnico")
        print(f"Matricula: {self.matricula}")
class Administrativo(Assistente):
    def __init__(self,nome,salario,matricula,dia):
        self.dia= True
        adicional=500
        super().__init__(nome,salario,matricula)
        if not dia:
            self.dia= False
            self.salario = self.salario+adicional
    def exibirDados(self):
        super().exibirDados()
        print("Cargo: Assistente Administrativo")
        print(f"Matricula: {self.matricula}")
        if not self.dia:
            print("Turno: Noite")
        else:
            print("Turno: Dia")


pessoa1=Tecnico("Claudia",1000,4177)
pessoa2=Administrativo("Afonso",1000,6789,True)
pessoa3=Administrativo("Paula",1000,1234,False)
print("-----------------------------")
pessoa1.exibirDados()
pessoa1.ganhoAnual()
print("-----------------------------")
pessoa2.exibirDados()
pessoa2.ganhoAnual()
print("-----------------------------")
pessoa3.exibirDados()
pessoa3.ganhoAnual()
print("-----------------------------")

