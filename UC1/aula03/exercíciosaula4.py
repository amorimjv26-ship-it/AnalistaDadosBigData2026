potência_lampada = 15
largura_cômodo = 4
comprimento_cômodo = 5

# Cálculos

area = 20 
potencia_necessária = 60
lâmpadas = 60 / 15 
bocais = 20 / 3 

# Saída 

qnt_lampadas = potencia_necessária / potência_lampada

resto = potencia_necessária % potência_lampada

if resto != 0:
    qnt_lampadas +=1

print("area:" , area)
print("potencia necessaria:", potencia_necessária)
print("quantidade de bocais:" , bocais)
print("quantidade de lampadas:" , qnt_lampadas)











