# nome = int(input("infome seu nome:"))

# if nome=="Pyetro":
#     resposta= "Pyetro presente!"
#  elif  nome=="Phelippe":
#         resposta= "Phelippe presente!"

# mes = int(input("Informe o mês de nascimento:"))

# #Visão IF/ELSE
# if mes==1:
#     Signo="Aquário"
# elif mes==2:
#         Signo="Peixes"
# elif mes==3:
#         Signo="Ariés"
# elif mes==4:
#         Signo="Touro"        
# elif mes==5:
#         Signo="Gemêos"    
# elif mes==6:
#         Signo="Câncer"
# elif mes==7:
#         Signo="Leão"        
# elif mes==8:
#         Signo="Virgem"
# elif mes==9:
#         Signo="Libra"
# elif mes==10:
#         Signo="Escorpião"                
# elif mes==11:
#         Signo="Sagitário"
# elif mes==12:
#         Signo="Capricornio" 

# print(F"seu signo é {Signo}.")

#Visão Match Case:
mes = int(input("Informe o mês de nascimento:"))
match mes:
     case 1:
         Signo="Aquário"
     case 2:
         Signo="Aries"
     case 3:
        Signo="Touro"
     case 4:
        Signo="Gêmeos"
     case 5:
         Signo="Câncer"
     case _:
        Signo= "Número de mês inválido"

print(f"{Signo}.")



