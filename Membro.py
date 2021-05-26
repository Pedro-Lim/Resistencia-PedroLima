class Membro:
    def __init__(self, nome, especie, cargo, possui_nave = False, nave = None):
        self.__nome = nome
        self.__especie = especie
        self.__cargo = cargo
        self.__nave = nave
        self.__possui_nave = possui_nave

    @property
    def nome(self):
        return "Nome do Membro: " + self.__nome
    @nome.setter
    def nome(self, novo_nome):
        if novo_nome != "":
            self.__nome = novo_nome
        else:
            print("Não é permitido valor vazio")
    

    @property
    def especie(self):
        return "Especie do Membro: " + self.__especie
    @especie.setter
    def especie(self, novo_especie):
        if novo_especie != "":
            self.__especie = novo_especie
        else:
            print("Não é permitido valor vazio")
            

    @property
    def cargo(self):
        return "Cargo do Membro: " + self.__cargo
    @cargo.setter
    def cargo(self, novo_cargo):
        if novo_cargo != "":
            self.__cargo = novo_cargo
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
        return "Nave :" + self.__nave 
    @nave.setter
    def nave(self, nova_nave):
        if type(nova_nave) != "<class 'Nave.Nave'>":
            print("parametro não compativel. Esperava-se uma variavel do tipo Nave")

        else:
            self.__nave = nova_nave