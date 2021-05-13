from Jedi import Jedi
from Nave import Nave
from Membro import Membro

def print_parametros(classe1, classe2 = None):
    index = vars(classe1)
    for item in index:
        if item == "_nave" and index[item] != None:
            print(">>>>>>>>>>>>>>>>>>>>>>>")
            print("Informações da nave:")
            index = vars(classe2)
            for item in index:
                print(item, ":", index[item])
            break
        elif item == "_nave" and index[item] == None:
            print("Sem nave cadastrada")
            break
        print(item, ":", index[item])

def cadastro_nave():
    nome_nave = input("Informe o nome da nave: ")
    fabricante = input("informe o fabricante da nave: ")
    quantidade_tripulacao = input("Informe a quantidade da tripulação:")
    modelo = input("Informe o modelo da nave:")
    classe = input("informe o classe da nave: ")
    newNave = Nave(nome_nave, fabricante, quantidade_tripulacao, modelo, classe)
    return(newNave)


print("Bem vindo ao sistema de cadastro da resistencia!!")
print("Gostaria de cadastra um membro, um jedi ou uma nave?")
escolha = input("Resposta: ")
if escolha.lower() == "membro": 
    nome = input("Informe o nome do membro: ")
    especie = input("Informe a espécie do membro: ")
    cargo = input("Informe o cargo do membro: ")
    possui_nave = input("Informe se o membro possui uma nave, (s) ou (n):")

    if possui_nave.lower() == "s":
        newNave = cadastro_nave()
        newMembro = Membro(nome, especie, cargo, newNave)
        print("{} Cadastrado com sucesso!!".format(escolha.lower()))
        print_parametros(newMembro, newNave)

    else: 
        newMembro = Membro(nome, especie, cargo)
        print("{} Cadastrado com sucesso!!".format(escolha.lower()))
        print_parametros(newMembro)

elif escolha.lower() == "jedi": 
    nome = input("Informe o nome do jedi: ")
    grau = input("Informe o grau do jedi: ")
    especie = input("Informe a espécie do jedi: ")
    cor_sabre = input("Informe a cor do sabre do jedi: ")
    possui_nave = input("Informe se o jedi possui uma nave, (s) ou (n):")

    if possui_nave.lower() == "s":
        newNave = cadastro_nave()
        newJedi = Jedi(nome, grau, especie, cor_sabre, newNave)
        print("{} Cadastrado com sucesso!!".format(escolha.lower()))
        print_parametros(newJedi, newNave)
    else: 
        newJedi = Jedi(nome, grau, especie, cor_sabre)
        print("{} Cadastrado com sucesso!!".format(escolha.lower()))
        print_parametros(newJedi)

elif escolha.lower() == "nave":
    newNave = cadastro_nave()
    print("{} Cadastrado com sucesso!!".format(escolha.lower()))
    print_parametros(newNave)

else:
    print("Opção invalida")

