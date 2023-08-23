programa {
  inclua biblioteca Matematica --> mat
  funcao inicio() {
    inteiro cod, cont=0, quant=1, opcao, a=0, b=0, c1=0, d=0, opcao2
    real soma=0, pendrive=49.90, teclado=24.90, cartucho=68.90, mouse=119.90
    logico pen = falso, tec = falso, car = falso, mou = falso
    cadeia p="Pendrive 32GB", t="Teclado USB", c="Cartucho HP1220", m= "Mouse Bluetooth", produto
    faca{
      faca{
        opcao2=1
        cont=1
        limpa ()
        escreva ("-----------------------------------------------")
        escreva ("\nCódigo            Descrição            Preço")
        escreva ("\n1                 Pendrive 32GB        R$49.90")
        escreva ("\n2                 Teclado USB          R$24.90")
        escreva ("\n3                 Cartucho HP1220      R$68.90")
        escreva ("\n4                 Mouse Bluetooth      R$119.90")
        escreva ("\n-----------------------------------------------\n")
        escreva ("Digite o código do produto:\n")
        leia (cod)
      }
      enquanto (cod <= 0 ou cod > 4 )
      faca{
      se (quant <= 0  ){
        limpa ()
        escreva ("-----------------------------------------------")
        escreva ("\nCódigo            Descrição            Preço")
        escreva ("\n1                 Pendrive 32GB        R$49.90")
        escreva ("\n2                 Teclado USB          R$24.90")
        escreva ("\n3                 Cartucho HP1220      R$68.90")
        escreva ("\n4                 Mouse Bluetooth      R$119.90")
        escreva ("\n-----------------------------------------------\n")
        escreva ("Digite o código do produto:")
        escreva ("\n",cod, "\n")
      }
      escreva ("-----------------------------------------------\n")
      escreva ("Digite a quantidade do produto\n")
      leia (quant)
      }
      enquanto (quant <= 0 )
      escolha (cod){  
        caso 1 :
          produto = p
          pen = verdadeiro
          soma = soma + (pendrive*quant)
          a = a + quant
          pare
        caso 2 :
          produto = t
          tec = verdadeiro
          soma = soma + (teclado*quant)
          b = b + quant
          pare
        caso 3:
          produto = c
          car = verdadeiro
          soma = soma + (cartucho*quant)
          c1 = c1 + quant
          pare
        caso 4:
          produto = m
          mou = verdadeiro
          soma = soma + (mouse*quant)
          d = d + quant
          pare
      }
      limpa ()
      escreva ("-----------------------------"           )
      escreva ("\nVocê adicionou ao carrinho:\n"         )
      escreva (quant, " unidades do produto: ", produto  )
      escreva ("\n\nO que deseja fazer?"                 )
      escreva ("\n----------------------------\n"        )
      escreva ("1) Adicionar outro produto\n"            )
      escreva ("2) Ver o carrinho de compras\n"          )
      leia (opcao) 
      limpa ()
      enquanto (opcao > 2 ou opcao < 1){
        limpa()
        escreva ("-----------------------------"           )
        escreva ("\nVocê adicionou ao carrinho:\n"         )
        escreva (quant, " unidades do produto: ", produto  )
        escreva ("\n\nO que deseja fazer?"                 )
        escreva ("\n----------------------------\n"        )
        escreva ("1) Adicionar outro produto\n"            )
        escreva ("2) Ver o carrinho de compras\n"          )
        leia (opcao)
      }
      se(opcao==1) cont = 0 
      senao se (opcao ==2) {
        limpa ()
        escreva ("--------------------------------------------")
        escreva ("\nSeu carrinho de compras                   ")
        escreva ("\n\nDescrição                Quantidade     ")
        se (pen == verdadeiro){
          escreva ("\n", p, "            ", a)
        }
        se (tec == verdadeiro){
          escreva ("\n", t, "              ", b)
        }
        se (car == verdadeiro){
          escreva ("\n", c, "          ", c1)
        }
        se (mou == verdadeiro){
          escreva ("\n", m, "          ", d)
        }
      }
      se (cont==1){
        escreva ("\n","Valor total do carrinho: ", soma = mat.arredondar (soma,2))
        escreva ("\n--------------------------------------------"                )
        escreva ("\nO que deseja fazer?"                                         )
        escreva ("\n--------------------------------------------\n"              )
        escreva ("1) Adicionar outro produto\n"                                  )
        escreva ("2) Limpar carrinho de compras\n"                               )
        escreva ("3) Sair\n"                                                     ) 
        leia (opcao2)
        enquanto (opcao2 < 1 ou opcao2 > 3){
          limpa ()
          escreva ("\n--------------------------------------------"                )
          escreva ("\nO que deseja fazer?"                                         )
          escreva ("\n--------------------------------------------\n"              )
          escreva ("1) Adicionar outro produto\n"                                  )
          escreva ("2) Limpar carrinho de compras\n"                               )
          escreva ("3) Sair\n"                                                     )
          leia (opcao2)
        }
      }
      
      se (opcao2==1) cont = 0
      senao se (opcao2==2){
        soma = 0
        pen = falso, tec = falso, car = falso, mou = falso
        a=0
        b=0
        c1=0
        d=0
        cont = 0
        quant=1
      }
      senao se (opcao2==3) {
        limpa ()
        cont = 1
      }
    }
    enquanto (cont == 0)
  }
}
