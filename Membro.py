class Membro:
    def __init__(self, nome, especie, cargo, nave = None):
        self._nome = nome
        self._especie = especie
        self._cargo = cargo
        self._nave = nave
    

    @property
    def nome(self):
        return "Nome do Membro:" + self._nome

    @nome.setter
    def nome(self, novo_nome):
        if novo_nome != "":
            self._nome = novo_nome
        else:
            print("Não é permitido valor vazio")
    

    @property
    def especie(self):
        return "especie do Membro:" + self._especie

    @especie.setter
    def especie(self, novo_especie):
        if novo_especie != "":
            self._especie = novo_especie
        else:
            print("Não é permitido valor vazio")
            

    @property
    def cargo(self):
        return "cargo do Membro:" + self._cargo

    @cargo.setter
    def cargo(self, novo_cargo):
        if novo_cargo != "":
            self._cargo = novo_cargo
        else:
            print("Não é permitido valor vazio")

    @property
    def nave(self):
        return
    
    @nave.setter
    def nave(self, nova_nave):
        if str(type(nova_nave)) != "<class 'Nave.Nave'>":
            print("parametro não compativel. Espera-se uma variavel do tipo classe")

        else:
            self._nave = nova_nave