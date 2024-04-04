import os

categorias = 0
pilhas = []
removidos = [[], []]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pilha(stack):
    exit = False
    while not exit:
        clear_screen()
        print(len(pilhas[stack]) - 1, " livros")
        for elementos in pilhas[stack]:
            print(elementos)
        print("\n(1)Adicionar um livro a categoria ")
        print("(2)Remover livro da categoria ")
        print("(3)Analisar primeiro livro da categoria")
        print("(4)Restaurar livros")
        print("(5)Voltar para a estante de categorias")
        opcao = int(input("O que deseja fazer?\n"))
        
        if opcao == 1:
            clear_screen()
            item = input("Qual livro deseja adicionar? \n")
            autor = input("Qual o nome do autor?\n")
            pilhas[stack].append(item)
            
            pilhas[stack + 1].append(autor)
            
        elif opcao == 2:
            removidos[0].append(pilhas[stack][-1])
            removidos[1].append(autor[stack][-1])
            pilhas[stack].pop(-1)
        elif opcao == 3:
            clear_screen()
            if len(pilhas[stack]) > 1:
                print("Título:")
                print(pilhas[stack][0])
                print("\nAutor:")
                print(pilhas[stack + 1][0])
                input("\nPressione enter para continuar...")
            else:
                print("A categoria está vazia.")
                input("\nPressione enter para continuar...")
        elif opcao == 4 :
            clear_screen()
            if removidos[0]:
                for i, elemento in enumerate(removidos[0]):
                    print(i, ". ", elemento)
                opcao = int(input("Qual livro deseja restaurar?\n"))
                if 0 <= opcao < len(removidos[0]):
                    restaurar = removidos[0][opcao]
                    pilhas[stack].append(restaurar)
                    restaurar = removidos[1][opcao]
                    pilhas[stack + 1].append(restaurar)
        elif opcao == 5:
            exit = True

while True:
    clear_screen()
    if categorias == 0:
        ctg = input("Crie uma nova categoria: \n")
        pilhas.append([ctg])
        pilhas.append([])
        categorias += 1
    else:
        a = 1
        for elementos in range(0, len(pilhas), 2):
            if pilhas[elementos]:
                print(a, ". ", pilhas[elementos][0])
                a += 1
        print("Pressione qualquer tecla (0) para criar uma nova categoria...\n")
        opcao = int(input("Selecione a categoria: \n"))
        a = 1
        if opcao > 0 and opcao <= len(pilhas) / 2:
            stack = (opcao - 1) * 2
            pilha(stack)
        else:
            clear_screen()
            ctg = input("Crie uma nova categoria: \n")
            pilhas.append([ctg])
            pilhas.append([])
            categorias += 1
