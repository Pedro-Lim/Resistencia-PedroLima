from Nave import Nave


class Jedi:
    def __init__(self, nome, grau, especie, cor_sabre, possui_nave = False,  nave = None):
        self.__nome = nome
        self.__grau = grau
        self.__especie = especie
        self.__cor_sabre = cor_sabre
        self.__possui_nave = possui_nave
        self.__nave = nave

    @property
    def nome(self):
        return "Nome do Jedi: " + self.__nome
    @nome.setter
    def nome(self, novo_nome):
        if novo_nome != "":
            self.__nome = novo_nome
        else:
            print("Não é permitido valor vazio")


    @property
    def grau(self):
        return self.__grau
    @grau.setter
    def grau(self, novo_grau):
        listajedi = ("mestre", "cavaleiro", "teste")
        if novo_grau.lower() in listajedi:
            self.__grau = novo_grau
        else:
            print("Grau não corresponde aos graus na ordem Jedi")
    

    @property
    def especie(self):
        return "especie do Jedi: " + self.__especie
    @especie.setter
    def especie(self, novo_especie):
        if novo_especie != "":
            self.__especie = novo_especie
        else:
            print("Não é permitido valor vazio")



    @property
    def cor_sabre(self):
        return "cor do sabre do Jedi: " + self.__cor_sabre
    @cor_sabre.setter
    def cor_sabre(self, novo_cor_sabre):
        if novo_cor_sabre != "":
            self.__cor_sabre = novo_cor_sabre
        else:
            print("Não é permitido valor vazio")
    
    
    @property
    def possui_nave(self):
        return "Possui nave: " + self.__possui_nave
    @possui_nave.setter
    def possui_nave(self, novo_possui_nave):
        if type(novo_possui_nave) == bool:
            self.__possui_nave = novo_possui_nave
        else:
            print("So é permitido valor booleano(True ou False)")


    @property
    def nave(self):
        return "Nave : " + self.__nave    
    @nave.setter
    def nave(self, nova_nave):
        if type(nova_nave) != Nave:
            print("parametro não compativel. Esperava-se uma variavel do tipo Nave")
        else:
            self.__nave = nova_nave


