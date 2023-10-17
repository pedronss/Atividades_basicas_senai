import my_math as m, os

while (True):
    os.system('cls') or None
    m.lista ()
    op=int(input())
    match op:
        case 1:
            os.system('cls') or None
            x=float(input("Digite o valor de x: "))
            y=float(input("Digite o valor de y: "))
            s_resultado= m.soma(x,y)
            print (x," + ",y," = ",s_resultado)
        case 2:
            os.system('cls') or None
            x=float(input("Digite o valor de x: "))
            y=float(input("Digite o valor de y: "))
            sub_resultado=m.sub(x,y)
            print (x," - ",y," = ",sub_resultado)
        case 3:
            os.system('cls') or None
            x=float(input("Digite o valor de x: "))
            y=float(input("Digite o valor de y: "))
            m_resultado=m.multi(x,y)
            print (x," x ",y," = ",m_resultado)
        case 4:
            os.system('cls') or None
            x=float(input("Digite o valor de x: "))
            y=float(input("Digite o valor de y: "))
            if y==0:
                print ("Não é possivel dividir por 0!!")
            else:
                d_resultado=m.divisao(x,y)
                print (x," : ",y," = ",d_resultado)
        case 5:
            os.system('cls') or None
            x=float(input("Digite o valor de x: "))
            y=float(input("Digite o valor de y: "))
            p_resultado=m.poten(x,y)
            print (x," ** ",y," = ",p_resultado)
        case 6:
            os.system('cls') or None
            x=float(input("Digite o valor de x: "))
            r_resultado=m.raiz(x)
            print (x," √ 2"," = ",r_resultado)
    input ("Aperte enter para continuar...")
