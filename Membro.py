class Membro:
    def __init__(self, nome, especie, cargo, possui_nave = 'Não possui uma nave', nave = 'sem informações da nave'):
        self.nome = nome
        self.especie = especie
        self.cargo = cargo
        self.possui_nave = possui_nave
        self.nave = nave