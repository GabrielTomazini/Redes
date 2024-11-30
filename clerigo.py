# personagem.py
class Clerigo:
    def __init__(self, nome, classe, nivel):
        self.nome = nome
        self.CA = None
        self.HP = 100
        self.dano_fisico = 8
        self.dano_magico = 15
    
    def ataqueAcerto(self):
        tipo_ataque = random.choice(['AD', 'AM'])  # Alterna entre mágico e físico
        d20 = random.randint(1, 20)
        if tipo_ataque == 'AM':  # Ataque Físico
            dano = random.randint(1, self.dano_fisico)
            return f"{tipo_ataque}{d20:02d}{dano:02d}"
        else:  # Ataque Mágico
            dano = random.randint(1, self.dano_magico)
            return f"{tipo_ataque}{d20:02d}{dano:02d}"

    def especial(self):
        cura = random.randint(1, 20) + 3
        self.HP = self.HP + cura
        print(f"{self.__class__.__name__} usou CURA e recuperou {cura} pontos de vida! Vida atual: {self.HP}")

    
    def getVida(self):
        return self.HP
    
    def setVida(self, novaVida):
        self.HP = novaVida
