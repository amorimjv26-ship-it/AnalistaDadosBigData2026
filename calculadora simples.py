print("\n--- 6. CALCULADORA SIMPLES ---")

n1 = float(input("Primeiro número: "))
operacao = input("Operação (+,-,*,/): ")
n2 = float(input("Segundo número: "))

match operacao:
    case "+":
        print("Resultado =", n1 + n2)
    case "-":
        print("Resutado =", n1 - n2)
    case "*":
        print("Resultado =", n1 * n2) 
    case "/":
        if n2 == 0:
            print("Não existe divisão por zero")
        else: 
          print("Resultado =", n1 / n2)
    case _:
        print("Opção inválida")





