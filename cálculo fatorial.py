print("\n--- 8. CÁLCULO DE FATORIAL ---")

N = int(input("Digite um número: "))

if N < 0:
    print("Não existe fatorial de número negativo")

elif N == 0:
    print("Fatorial = 1")

else: 
    resultado_fatorial = 1
    for i in range(1,N + 1):
        resultado_fatorial = resultado_fatorial * i
        print("Fatorial =", resultado_fatorial)

        