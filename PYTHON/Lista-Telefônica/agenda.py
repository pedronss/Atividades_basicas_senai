import os
WHITE  = "\033[1;37m"
RESET = "\033[0;0m"
RED   = "\033[1;31m"
agenda = []
addcontat=[]
def add ():
    print (WHITE)
    nome= input("Qual contato deseja adicionar?")
    numero = input("Qual número deseja adicionar?")
    agenda.clear
    addcontat=[]
    addcontat.append(nome)
    addcontat.append(numero)
    agenda.append (addcontat)
    print (RESET)

def excluirc():
    print (WHITE)
    nome=int(input("Qual contato deseja excluir?"))
    agenda.pop (nome)
    print (RESET)
def editarc():
    print (WHITE)
    addcontat=[]
    contato=int(input("Qual contato deseja editar?"))
    nome=(input("Qual será o novo nome?"))
    numero=(input("Qual será o novo número?"))
    agenda.pop(contato)
    addcontat.append(nome)
    addcontat.append(numero)
    agenda.insert(contato,addcontat)
    print (RESET)

def listarc():
    a=0
    print (WHITE)
    if len(agenda)==0:
        print ("Sua agenda está vazia!")
    for i in range(len(agenda)):
        print(a,".",agenda[i])
        a+=1
    print (RESET)
def limparc():
    agenda.clear()
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
def opcaoc():
    print ("\n"+WHITE+"──────────────────────────────")
    print (WHITE+"│          AGENDA            │" )
    print (WHITE+"│(1)Adicionar contato...     │")
    print (WHITE+"│(2)Editar contato...        │")
    print (WHITE+"│(3)Ver lista de contatos... │")
    print (WHITE+"│(4)Excluir contatos...      │")
    print (WHITE+"│(5)Limpar contatos...       │")
    print (WHITE+"│                            │" )
    print ("──────────────────────────────\n"+RESET)
