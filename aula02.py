import pandas as pd
import numpy as np

#lOC
#ILOC
#QUERY

filmes = {
  'título':["Lagoa Azul", "Agente Secreto", "Gênio indomável", "A Freira", "Brinquedo Assasino", "Top Gun"],
  'categoria':["Romance","Ação", "Drama", "Terror", "Comédia", "Aventura"],
  'ano':["1980","2025","1997", "2022", "1995", "1986"],
  'Faturamento': [6.5,4,5.5,3,9,7.2]

}
indices = ['A','B','C','D','E','F']
tabela_filmes = pd.DataFrame(filmes, index=indices)

print(tabela_filmes)
# print(type(tabela_filmes))
# print(tabela_filmes)
# print(type(tabela_filmes))

# print(tabela_filmes.iloc[-1])
print('-'*20)
print(tabela_filmes.loc['B'])
print('-'*20)
print(tabela_filmes.loc['B':'E'])
print(tabela_filmes.iloc[1:3])
print('-'*20)
consulta1 = tabela_filmes.query("Faturamento == 5.5")
print(consulta1)
 # < > <= >= == != and or not in

 
   
