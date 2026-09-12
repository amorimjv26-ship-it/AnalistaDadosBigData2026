import pandas as pd

# # Carregar os dados do arquivo Excel.
# df_transacoes = pd.read_excel('base_invest.xlsx', sheet_name='Transacoes')
# df_ativo = pd.read_excel('base_invest.xlsx', sheet_name='Ativo')

# # Pergunta 1: Quais são as máximas e mínimas de operação de compra e venda das transações

# # Para encontr o máximoe o mínim para 'preco' e 'quantidade' , filtre o Dataframe p
# df_compra = df_transacoes[df_transacoes['operacao'] == 'compra']
# df_venda = df_transacoes[df_transacoes['operacao'] == 'venda']

# # Use .max() e min() para encontrar os valores mais altos e mais baixos na coluna 'preco'
# max_compra_preco = df_compra['preco'].max()
# max_compra_preco = df_compra['preco'].min()
# max_venda_preco = df_venda['preco'].max()
# min_venda_preco = df_venda['preco'].min()
# print(max_compra_preco)


# # Pergunta 2: Qual CNPJ tem o ativo de maior valor?


# df_transacoes['valor_total'] = df_transacoes['quantidade'] * df_transacoes['preco']
# print(df_transacoes)

# valor_por_ativo = df_transacoes.groupby('id_ativo')['valor_total'].sum()
# print(valor_por_ativo)
# id_ativo_maior_valor = valor_por_ativo.idxmax()
# print(valor_por_ativo)
# cnpj_maior_valor = df_ativo[df_ativo['id_ativo'] == id_ativo_maior_valor]['cnpj'].iloc[0]

# print("--- CNPJ com o ativo de maior valor ---")
# print(f"O CNPJ para o ativo com o maior valor total é: {cnpj_maior_valor}")
# print("\n")

# Pergunta 3: Qual valor total em transações de cada participante?

valor_por_participante =  df_transacoes.groupby('id_participante')

