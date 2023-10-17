'''Criar uma lista de tarefas'''
import os
#inserir tarefas
a=0
tarefas = []
while (True):
    b=0
    if a==0: exit=1
    while(exit==1): 
        os.system('cls') or None
        tarefas.append(input("Escreva uma nova tarefa:"))
        exit = int(input ("Deseja adicionar mais tarefas?\n1)Sim\n2)Não\n"))    
        a=1
    #exibir tarefas
    os.system('cls') or None
    b=0
    for tarefa in tarefas:
        print (b,".",tarefa,"\n")
        b+=1
    opcao= int (input ("Oque deseja fazer agora?\n1)Marcar tarefas como feita\n2)Remover tarefas\n3)Limpar lista\n4)Adicionar mais tarefas\n"))
    if opcao == 1 :
        b=0
        os.system('cls') or None
        for tarefa in tarefas:
            print (b,".",tarefa,"\n")
            b+=1
        opcao2= int (input ("\nQual tarefa deseja marcar como feita?\n"))
        tarefas[opcao2] = tarefas[opcao2] + " ✔" 
        os.system('cls') or None
        b=0
        for tarefa in tarefas:
            print (b,".",tarefa,"\n")
            b+=1
    if opcao == 2 :
        b=0
        os.system('cls') or None
        for tarefa in tarefas:
            print (b,".",tarefa,"\n")
            b+=1
        opcao3=int(input("Qual tarefa deseja retirar?"))
        tarefas.pop(opcao3)
        os.system('cls') or None
        b=0
        for tarefa in tarefas:
            print (b,".",tarefa,"\n")
            b+=1
    if opcao == 3 : 
        tarefas.clear()
    if opcao == 4:
        a=0
        
