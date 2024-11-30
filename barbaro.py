import random

class Barbaro:
    def __init__(self):
        self.HP = 100  # Alto HP
        self.CA = 15   # Boa defesa
        self.dano_fisico = 12  # Ataque físico forte
    
    def ataqueAcerto(self):
        d20 = random.randint(1, 20)
        dano = random.randint(1, self.dano_fisico)
        return f"AM{d20:02d}{dano:02d}"  # Ataque Físico

    def getVida(self):
        return self.HP
    
    def setVida(self, novaVida):
        self.HP = novaVida

    def especial(self):
        bonus_ataque = random.randint(10, 20)  # Aumenta o dano por 5 a 10 no próximo ataque
        self.dano_fisico += bonus_ataque
        print(f"{self.__class__.__name__} entrou em FÚRIA! Próximo ataque terá bônus de {bonus_ataque} de dano!")
