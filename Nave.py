class Nave:
    def  __init__(self, nome, fabricante, quantidade_tripulacao, modelo, classe):
        self._nome = nome
        self._fabricante = fabricante
        self._quantidade_tripulacao = quantidade_tripulacao
        self._modelo = modelo
        self._classe = classe

    @property
    def nome(self):
        return "Nome da nave:" + self._nome

    @nome.setter
    def nome(self, novo_nome):
        if novo_nome != "":
            self._nome = novo_nome
        else:
            print("Não é permitido valor vazio")
    

    @property
    def fabricante(self):
        return "fabricante da nave:" + self._fabricante

    @fabricante.setter
    def fabricante(self, novo_fabricante):
        if novo_fabricante != "":
            self._fabricante = novo_fabricante
        else:
            print("Não é permitido valor vazio")
            

    @property
    def quantidade_tripulacao(self):
        return "quantidade da tripulação da nave:" + self._quantidade_tripulacao

    @quantidade_tripulacao.setter
    def quantidade_tripulacao(self, novo_quantidade_tripulacao):
        if novo_quantidade_tripulacao != 0 and novo_quantidade_tripulacao > 0  :
            self._quantidade_tripulacao = novo_quantidade_tripulacao
        else:
            print("Não é permitido uma nave com 0 membros na tripulação ou um numero negativo de membros")
    

    @property
    def modelo(self):
        return "modelo da nave:" + self._modelo

    @modelo.setter
    def modelo(self, novo_modelo):
        if novo_modelo != "":
            self._modelo = novo_modelo
        else:
            print("Não é permitido valor vazio")
    

    @property
    def classe(self):
        return "classe da nave:" + self._classe

    @classe.setter
    def classe(self, novo_classe):
        if novo_classe != "":
            self._classe = novo_classe
        else:
            print("Não é permitido valor vazio")