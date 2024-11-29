# Level 5 Rogue Arcene Trickster Subclass
# Stats:
# STR: 8 | DEX: 18 | CON: 16 | INT:8 | WIS:16 | CHA:8


class Rogue:
    def __init__(self, nome):
        self.nome = nome
        self.CA = None
        self.HP = 50

    def ataque(self, personagemInimigo):
        return 10

    def setVida(self, vida):
        self.HP = vida
