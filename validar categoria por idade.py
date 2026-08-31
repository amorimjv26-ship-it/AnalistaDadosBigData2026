print("\n--- 10. VALIDAR CATEGORIA POR IDADE ---")

ANO_ATUAL = 2026

ano_nascimento = int(input("Ano de Nasciento: "))

idade = ANO_ATUAL - ano_nascimento
if idade < 12:
    print("Criança")

elif idade < 17:
    print("Adolescente")

else:
    print("Adulto")
    
