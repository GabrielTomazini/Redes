# Level 5 Rogue Arcene Trickster Subclass Variant Human
# Feat: Sharpshooter: -5 in attack roll, +10 in damage
# Feat: Crossbow Expert: Don't impose disadvantage in ranged attack rolls 5ft from enemy
# Stats:
# STR: 8 | DEX: 16 | CON: 16 | INT:8 | WIS:14 | CHA:10
import random
import math
from colorama import init, Fore, Style, Back

init(autoreset=True)

bonusProficiencia = 3


class Ladino:
    modDestreza = 3
    espacosDeMagia = 3

    def __init__(self):
        self.CA = 16
        self.HP = 43

    def ataqueAcerto(self):
        ataque = input(
            Back.WHITE
            + Fore.CYAN
            + Style.BRIGHT
            + "Deseja usar o Franco Atirador ou ataque normal?\n (1)Franco Atirador\n (2)Ataque Normal\n "
        )
        # Vantagem da mira firme
        maiord20 = 0
        d20_1 = random.randint(1, 20)
        d20_2 = random.randint(1, 20)
        if d20_1 >= d20_2:
            maiord20 = d20_1
        else:
            maiord20 = d20_2

        if ataque == "1":
            d20Final = (
                maiord20 + self.modDestreza + bonusProficiencia - 5
            )  # -5 Sharpshooter
            dano = 0
            if maiord20 == 20:  # Ataque crítico, rola o dobro dos dados e modificadores
                d20Final = (
                    40  # acerto automático, valor ridiculamente alto para simular isso
                )
                for i in range(1, 8):
                    d6 = random.randint(1, 6)
                    dano = dano + d6
                dano = dano + 10 + self.modDestreza  # +10 sharpshooter
            else:
                for i in range(1, 4):
                    d6 = random.randint(1, 6)
                    dano = dano + d6
                dano = dano + 10 + self.modDestreza  # +10 sharpshooter
        elif ataque == "2":
            d20Final = maiord20 + self.modDestreza + bonusProficiencia
            dano = 0
            if d20Final == 20:  # Ataque crítico, rola o dobro dos dados e modificadores
                for i in range(1, 8):
                    d6 = random.randint(1, 6)
                    dano = dano + d6
                dano = dano + 2 * self.modDestreza  # +10 sharpshooter
            else:
                for i in range(1, 4):
                    d6 = random.randint(1, 6)
                    dano = dano + d6
                dano = dano + self.modDestreza  # +10 sharpshooter
        else:
            print(Back.WHITE + Fore.CYAN + Style.BRIGHT + "Digite um ataque válido!\n")
        print(
            Back.WHITE
            + Fore.CYAN
            + Style.BRIGHT
            + "Seu d20: "
            + str(d20Final)
            + "\nSeu dano: "
            + str(dano)
        )
        msg = "D" + "A" + str(d20Final).zfill(2) + str(dano)
        return msg

    def ataqueRecebido(self, msg):

        if msg[:1] == "E" and int(msg[1:3]) >= self.getTeste(msg[1:3]):
            dano = math.ceil(int(msg[3:5]) / 2)
        elif msg[:1] == "A" and int(msg[1:3]) >= self.CA:
            # Se o ataque for menor que CA+5, usa shield
            if int(msg[1:3]) < (self.CA + 5) and self.espacosDeMagia > 0:
                self.espacosDeMagia = self.espacosDeMagia - 1
                print(
                    Back.WHITE
                    + Fore.CYAN
                    + Style.BRIGHT
                    + "Você usou Escudo Arcano! Seu inimigo errou o Ataque, seu d20 foi: "
                    + msg[1:3]
                )
                if self.espacosDeMagia == 2:
                    print(
                        Back.WHITE
                        + Fore.CYAN
                        + Style.BRIGHT
                        + "\nEspaços de magia restantes:\n1º Ciclo: [][][x]"
                    )
                if self.espacosDeMagia == 1:
                    print(
                        Back.WHITE
                        + Fore.CYAN
                        + Style.BRIGHT
                        + "\nEspaços de magia restantes:\n1º Ciclo: [][x][x]"
                    )
                if self.espacosDeMagia == 0:
                    print(
                        Back.WHITE
                        + Fore.CYAN
                        + Style.BRIGHT
                        + "\nEspaços de magia restantes:\n1º Ciclo: [x][x][x]"
                    )
                dano = 0
            else:
                dano = int(msg[3:5])
        else:
            print(
                Back.WHITE
                + Fore.CYAN
                + Style.BRIGHT
                + "Seu inimigo errou o Ataque, seu d20 foi: "
                + msg[1:3]
            )
            dano = 0
        print(Back.WHITE + Fore.CYAN + Style.BRIGHT + "Dano recebido : " + str(dano))

        nova_vida = self.HP - dano
        self.HP = nova_vida
        return nova_vida
