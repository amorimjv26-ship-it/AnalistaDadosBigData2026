print("\n--- 1. VALIDADOR DE TRIÂNGULO ---")

A = float(input("Digite o lado A: "))
B = float(input("Digite o lado B: "))
C = float(input("Digite o lado C: "))

if A + B > C and A + C > B and B + C > A:
    print("Triângulo válido!")
else:
    print("Não é um triângulo.")

print("Entrada inválida!")