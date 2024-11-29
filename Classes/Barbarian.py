import random


class Barbarian:

    def __init__(self):
        self.CA = 15
        self.HP = 50
        self.danoFuria = 5

    def ataqueAcerto(self):
        print(input("Pressione 1 para atacar duas vezes: "))
        auxiliar = 0
        for i in range(2):
            d12 = random.randint(1, 12)
            print("Soma entre 5 e :  ", d12, self.danoFuria)
            auxiliar += d12 + 5 + self.danoFuria
        print("O total foi: ", auxiliar)
        # A mensagem de ataque agora inclui o valor correto do dano
        msg = "D" + "AM" + str(random.randint(1, 20)).zfill(2) + str(auxiliar)
        return msg
