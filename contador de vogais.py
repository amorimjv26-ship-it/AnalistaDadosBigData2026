print("\n--- 4. CONTADOR DE VOGAIS ---")

frase = input("Digite uma palavra ou frase: ").lower()

contador_vogais = 0

for letra in frase:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        contador_vogais += 1

        print("Quantidade de vogais:", contador_vogais)


  