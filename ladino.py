import random

class Ladino:
    def __init__(self):
        self.HP = 75  # HP médio
        self.CA = 14  # Boa evasão
        self.dano_fisico = 10  # Ataque preciso
    
    def ataqueAcerto(self):
        d20 = random.randint(1, 20)
        dano = random.randint(1, self.dano_fisico) + 3  # Bônus de precisão
        return f"AM{d20:02d}{dano:02d}"  # Ataque Físico

    def getVida(self):
        return self.HP
    
    def setVida(self, novaVida):
        self.HP = novaVida

    def especial(self):
        evasao = random.randint(1, 10)  # Aumenta CA temporariamente
        self.CA += evasao
        print(f"{self.__class__.__name__} ficou em modo FURTIVO! Sua CA aumentou em {evasao} por um turno.")
