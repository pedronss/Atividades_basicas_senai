import agenda as a

while (True):
    a.clear_screen()
    a.opcaoc()
    opcao=int(input())
    match (opcao):
        case 1 :
            a.clear_screen()
            a.add()
        case 2:
            a.clear_screen()
            a.editarc()
        case 3:
            a.clear_screen()
            print ("\n"+a.WHITE+"──────────────────────────────")
            a.listarc()
            print ("──────────────────────────────\n")
            input("Pressione enter para continuar...")
            print (a.RESET)
        case 4:
            a.clear_screen()
            print ("\n"+a.WHITE+"──────────────────────────────")
            a.listarc()
            print ("──────────────────────────────\n")
            a.excluirc()
            print (a.RESET)
        case 5:
            a.clear_screen()
            a.limparc()
        case _:
            
            print(a.RED+"Comando inválido!"+a.RESET)
            input("Pressione enter para continuar...")

