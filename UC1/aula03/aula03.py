print("olámundo")
nome = "maria"
idade = 30
preco = 19.99
esta_matriculada = True
notas = [8.0, 7.5]
aluno = ("maria", 30)
disciplinas = {"python", "lógica"}
cadastro = {"nome": "maria", "idade" : 30}


print(type("maria"))
print(type(30))
print(type(19.99))

print("inovacao")
nome = "joao"
idade = 21
preco = 22.9
esta_matriculado = False
notas = [9.2, 5.9]
aluno = ("joao", 21)
disciplinas = {"inglês", "física"}
cadastro = {"nome": "joao", "idade" :21}


print(type("joao"))
print(type(21))
print(type(22.99))

nota_1 = 2
nota_2 = 4


cnh = True
gt = False
      #True #True
posso_dirigir = cnh and not gt
print(posso_dirigir)

busaum = False
trenzin = False

venho_pra_aula = busaum or trenzin
print("venho pra aula?",venho_pra_aula)


locomocao = input("Diga qual sua locomocao:")

choveu = True


if choveu and locomocao=='moto':
    resultado = "Tô todo molhado :("

elif not choveu and locomocao=='moto':
    resultado = "Tô seco"
    
