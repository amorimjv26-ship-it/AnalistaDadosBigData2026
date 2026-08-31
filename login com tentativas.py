print("\n--- 5. LOGIN COM TENTATIVAS ---")

usuario_cadastrado = input("Crie um usúario: ")
senha_cadastrada = input("Crie uma senha: ")

tentativas_atuais = 0
TENTATIVAS_MAX = 4

while tentativas_atuais < TENTATIVAS_MAX:

    usuario = input("Usuario: ")
    senha = input("Senha: ")

    if usuario == usuario_cadastrado and senha == senha_cadastrada:
        print("Login realizado com sucessso")
        break 

else:
    print("Dados incorretos")
    tentativas_atuais += 1
    if tentativas_atuais == TENTATIVAS_MAX:
        print("Acesso bloqueado")
        

