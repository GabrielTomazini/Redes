import random

class Mago:
    def __init__(self):
        self.HP = 50  # Baixo HP
        self.CA = 12  # Defesa baixa
        self.dano_magico = 20  # Ataque mágico poderoso
    
    def ataqueAcerto(self):
        d20 = random.randint(1, 20)
        dano = random.randint(1, self.dano_magico)
        return f"AD{d20:02d}{dano:02d}"  # Ataque Mágico

    def getVida(self):
        return self.HP
    
    def setVida(self, novaVida):
        self.HP = novaVida

    def especial(self):
        dano_bonus = random.randint(10, 20)  # Dano mágico extra
        print(f"{self.__class__.__name__} lançou uma BOLA DE FOGO, causando {dano_bonus} de dano extra!")
        return dano_bonus
