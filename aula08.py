def calculadora_v1(n1,n2, operador="1"):

n1 = float(input("Digite seu primeiro número:"))
n2 = float(input("Digite seu segundo número:"))

operador=input("Informe a operação desejada entre: 1. adição 2. subtração; 3. multiplicação; 4 divisão;")

match operador:
    case "1":
        print(f"Resultado da soma:{n1+n2}.")
    case "2":
        print(f"Resultado da soma:{n1-n2}.")
    case "3":
        print(f"Resultado da soma:{n1*n2}.")
    case "4":
         if n2!=0:
            print(f"Resultado da soma: {n1/n2}.")
         else:
          print(f"Dividiu por zero. errou feio. errou rude!")
    case _ :
        print(f" infome um número de operador válido. ")



         


