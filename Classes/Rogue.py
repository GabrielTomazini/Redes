class Rogue:
    def __init__(self, nome):
        self.nome = nome
        self.CA = None
        self.HP = 50

    def ataque(self, personagemInimigo):
        return 10

    def setVida(self, vida):
        self.HP = vida
