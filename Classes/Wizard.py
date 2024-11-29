# Sugestão: Mago Abjurador lvl. 5
# Quero ver implementar a mecânica dos espaços e magia 💀


# Level 5 Wizard Abjurer Subclass
# Stats:
# STR: 8 | DEX: 16 | CON: 16 | INT:18 | WIS:8 | CHA:8
class Wizard:
    def __init__(self, nome):
        self.nome = nome
        self.CA = None
        self.HP = 100

    def ataque(self, personagemInimigo):
        return 10

    def setVida(self, vida):
        self.HP = vida
