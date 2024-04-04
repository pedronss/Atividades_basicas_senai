from datetime import datetime
# criando a função
def saudacao ():
    hora = datetime.now().hour
    print("Current Time =", hora)
    if hora >=0 and hora <=12:
        print ("Boa tarde!")
    elif hora>17:
        print ("Boa noite!")
    else:
        print ("Bom dia!")
#Ultilizando a função'
saudacao()