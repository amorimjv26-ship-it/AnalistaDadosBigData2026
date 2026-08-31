print("\n--- 2. ADIVINHE O NÚMERO ---")

NUMERO_SECRETO = 42
TENTATIVAS_MAX = 5

for tentativa in range(1, TENTATIVAS_MAX + 1):

        palpite = int(input(f"tentativa {tentativa}: "))

        if palpite == NUMERO_SECRETO:
            print("parabéns você acertou!")
            break 
        elif palpite < NUMERO_SECRETO:
            print("o número é maior")
        else:
            print("o número é menor")
 
        print("digite um número válido")

