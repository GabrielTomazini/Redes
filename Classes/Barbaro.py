import random
import math
from colorama import init, Fore, Style, Back

init(autoreset=True)


class Barbaro:

    def __init__(self):
        self.CA = 15
        self.HP = 55
        self.esquivo = False
        self.danoFuria = 3
        self.Imprudente = False
        self.orc = False

    def ataqueAcerto(self):
        auxiliar = 0
        dano = 0
        imprudente = input(
            Back.RED
            + Style.BRIGHT
            + "Deseja usar ataque imprudente?\n (1) Sim \n (2) Não\n "
        )
        if imprudente == "1":
            self.Imprudente = True
        else:
            self.Imprudente = False
        ataque = input(
            Back.RED
            + Style.BRIGHT
            + "Deseja usar ataque utilizar?\n (1) Ataque com Machado 2x (2) Modo ESQUIVOOO\n "
        )
        if ataque == "1":
            d12 = random.randint(1, 12)
            print(
                Style.BRIGHT
                + Back.RED
                + "Soma entre 5 e :  "
                + str(d12)
                + str(self.danoFuria)
            )
            dano = d12 + 5 + self.danoFuria
            auxiliar = random.randint(1, 20)

            if self.Imprudente == True:
                auxiliar += 5
            print(
                Style.BRIGHT
                + Back.RED
                + "Seu D20: "
                + str(auxiliar)
                + "\nSeu dano: "
                + str(dano)
            )

        else:
            self.esquivo = True
            auxiliar = 0
            dano = 0
            print(
                Style.BRIGHT
                + Back.RED
                + "Modo Esquivo ativado! Me acerta que eu duvido"
            )
        msg = "D" + "A" + str(auxiliar).zfill(2) + str(dano)
        return msg
        # A mensagem de ataque agora inclui o valor correto do dano

    def ataqueRecebido(self, msg):
        if self.esquivo == True:
            CA = self.CA + 5
        elif self.Imprudente == True:
            CA = self.CA - 2
        else:
            CA = self.CA
        if msg[:1] == "E" and int(msg[1:3]) >= self.getTeste(msg[1:3]):
            dano = math.ceil(int(msg[3:5]) / 2)
        elif msg[:1] == "A" and int(msg[1:3]) >= CA:
            dano = math.ceil(int(msg[3:5]) / 2)
        else:
            print(
                Style.BRIGHT
                + Back.RED
                + "Seu inimigo errou o Ataque, seu d20 foi: "
                + msg[1:3]
            )
            dano = 0
        print(Style.BRIGHT + Back.RED + "Dano recebido : " + str(dano))

        nova_vida = self.HP - dano
        if dano > 20:
            Irina = input(
                Style.BRIGHT
                + Back.RED
                + "Você ira sofrer um dano monstruoso\n Deseja utilizar seu Trunfo Final(única utilização)? \n (1)Sim \n (2) Não\n "
            )
            print(
                Style.BRIGHT
                + Back.RED
                + "Sua AMADA Irina lhe salvou , Parabéns Herói GROAK, parece que até anjos estão de olho em você!"
            )
            nova_vida += 20

        if nova_vida <= 0 and self.orc == False:
            nova_vida = 1
            self.orc = True
            print(Style.BRIGHT + Back.RED + "EU SOU ORC SEU OTÁRIO!!!\n")

        self.HP = nova_vida
        self.Imprudente = False
        self.esquivo = False
        return nova_vida

    def getTeste(self):
        print("oi")
