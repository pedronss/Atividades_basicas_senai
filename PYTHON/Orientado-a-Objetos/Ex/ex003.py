import os
class Pessoa:
    def __init__(self,nome,email,idade):
        self.nome=nome
        self.email=email
        if idade < 120 and idade > 0:
            self.idade=idade
    def getNome(self):
        return self.nome
    def getEmail(self):
        return self.email
    def getIdade(self):
        return self.idade
    def setNome(self,novonome):
        self.nome=novonome
    def setemail(self,novoemail):
        if "@"in novoemail:
            self.email=novoemail
        else:
            print("Invalido!")
    def setidade(self,novaidade):
        if novaidade < 120 and novaidade > 0:
            self.idade=novaidade
        
os.system

p1=Pessoa("Pedro","pedro@gmail.com",100)
p1.setemail("adsadasdad")
print(p1.getNome())
print(p1.getEmail())
print(p1.getIdade())
