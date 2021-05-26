from Jedi import Jedi
from Membro import Membro


class Nave:
    def  __init__(self, nome, fabricante, quantidade_tripulacao, modelo, classe, capitao, tripulacao = []):
        self.__nome = nome
        self.__fabricante = fabricante
        self.__quantidade_tripulacao = quantidade_tripulacao
        self.__modelo = modelo
        self.__classe = classe
        self.__tripulacao = tripulacao
        self.__capitao = capitao


    @property
    def nome(self):
        return "Nome da nave:" + self.__nome
    @nome.setter
    def nome(self, novo_nome):
        if novo_nome != "":
            self.__nome = novo_nome
        else:
            print("Não é permitido valor vazio")
    

    @property
    def fabricante(self):
        return "Fabricante da nave:" + self.__fabricante
    @fabricante.setter
    def fabricante(self, novo_fabricante):
        if novo_fabricante != "":
            self.__fabricante = novo_fabricante
        else:
            print("Não é permitido valor vazio")
            

    @property
    def quantidade_tripulacao(self):
        return "quantidade da tripulação da nave:" + self.__quantidade_tripulacao
    @quantidade_tripulacao.setter
    def quantidade_tripulacao(self, novo_quantidade_tripulacao):
        if  novo_quantidade_tripulacao > 0  :
            self.__quantidade_tripulacao = novo_quantidade_tripulacao
        else:
            print("Não é permitido uma nave com 0 membros na tripulação ou um numero negativo de membros")


    @property
    def tripulacao(self):
        return "tripulacao da nave:" + self.__tripulacao
    @tripulacao.setter
    def tripulacao(self, novo_tripulacao):
        if type(novo_tripulacao) == list:
            if len(novo_tripulacao) > 0:
                self.__tripulacao = novo_tripulacao
            else:
                print("A tripulação precisa ter pelo menos 1 nome")
        else:
            print("Esperava-se uma lista com os nomes da tripulação")   


    @property
    def modelo(self):
        return "modelo da nave:" + self.__modelo
    @modelo.setter
    def modelo(self, novo_modelo):
        if novo_modelo != "":
            self.__modelo = novo_modelo
        else:
            print("Não é permitido valor vazio")
    

    @property
    def classe(self):
        return "classe da nave:" + self.__classe
    @classe.setter
    def classe(self, novo_classe):
        if novo_classe != "":
            self.__classe = novo_classe
        else:
            print("Não é permitido valor vazio")


    @property
    def capitao(self):
        return "capitâo : " + self.__capitao    
    @capitao.setter
    def capitao(self, novo_capitao):
        if type(novo_capitao) != Membro or type(novo_capitao) != Jedi :
            print("parametro não compativel. Esperava-se uma variavel do tipo Membro ou Jedi")
        else:
            self.__capitao = novo_capitao