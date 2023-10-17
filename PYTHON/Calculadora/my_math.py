RED   = "\033[1;31m"
WHITE  = "\033[1;37m"
RESET = "\033[0;0m"

def soma (x,y):
    return (x+y)
def sub (x,y):
    return (x-y)
def multi (x,y):
    return (x*y)
def divisao (x,y):
    return (x/y)
def poten (x,y):
    return (x**y)
def raiz (x):
    return (x**(1/2))
def lista():
    print ("\n"+WHITE+"──────────────────────────────")
    print (WHITE+"│          CALCULADORA       │" )
    print (WHITE+"│(1)Soma                     │")
    print (WHITE+"│(2)Subtraição               │")
    print (WHITE+"│(3)Multiplicação            │")
    print (WHITE+"│(3)Divisão                  │")
    print (WHITE+"│(5)Potenciação              │")
    print (WHITE+"│(6)Raiz Quadrada            │")
    print (WHITE+"│                            │" )
    print ("──────────────────────────────\n"+RESET)
lista ()
