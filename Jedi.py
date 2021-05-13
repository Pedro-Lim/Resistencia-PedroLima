class Jedi:
    def __init__(self, nome, grau, especie, cor_sabre, nave = None):
        self._nome = nome
        self._grau = grau
        self._especie = especie
        self._cor_sabre = cor_sabre
        self._nave = nave

    @property
    def nome(self):
        return "Nome do Jedi:" + self._nome

    @nome.setter
    def nome(self, novo_nome):
        if novo_nome != "":
            self._nome = novo_nome
        else:
            print("Não é permitido valor vazio")


    @property
    def grau(self):
        return self._grau

    @grau.setter
    def grau(self, novo_grau):
        if novo_grau != "padawan" or novo_grau!= "cavaleiro" or novo_grau != "mestre":
            print("Grau não corresponde as classes na ordem Jedi")
        else:
            self._grau = novo_grau
    

    @property
    def especie(self):
        return "especie do Jedi:" + self._especie

    @especie.setter
    def especie(self, novo_especie):
        if novo_especie != "":
            self._especie = novo_especie
        else:
            print("Não é permitido valor vazio")



    @property
    def cor_sabre(self):
        return "cor do sabre do Jedi:" + self._cor_sabre

    @cor_sabre.setter
    def cor_sabre(self, novo_cor_sabre):
        if novo_cor_sabre != "":
            self._cor_sabre = novo_cor_sabre
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


