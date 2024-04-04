import os
class Cinema:
    def __init__(self,nome,capacidade,ingressos_vendidos):
        self.nome=nome
        self.capacidade=capacidade
        self.ingressos_vendidos=ingressos_vendidos
    def vender(self,quant):
        if self.capacidade < 100 and self.capacidade > 0 and quant > 0 and quant < 100:
            self.capacidade=self.capacidade-quant
            self.ingressos_vendidos=self.ingressos_vendidos+quant
    def cancelarVenda(self,quant):
        if self.capacidade < 100 and self.capacidade > 0 and quant > 0 and quant < 100:
            self.capacidade= self.capacidade+quant
            self.ingressos_vendidos=self.ingressos_vendidos-quant
cinema=Cinema("Cinema da Tuma da Mônica",50,0)
ultimavenda=0
while(True):
    os.system('cls')
    print(f"Cinema: {cinema.nome}\nCapacidade: {cinema.capacidade}\nIngressos Vendidos: {cinema.ingressos_vendidos}")
    print("\n(1)Vender ingressos\n(2)Cancelar venda")
    option= int(input("O que deseja fazer?\n"))
    if option ==1:
        quant=int(input("Quantos ingressos deseja vender?"))
        cinema.vender(quant)
    if option == 2:
        cinema.cancelarVenda(quant)