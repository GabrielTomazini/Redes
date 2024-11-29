class Cleric:
    def __init__(self, nome, classe, nivel):
        self.nome = nome
        self.CA = None
        self.HP = 100

    def ataque(self, personagemInimigo):
        return 10

    def setVida(self, vida):
        self.HP = vida
