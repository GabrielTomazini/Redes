# Lvl.5 Wizard Bladesinger Turtle
# Combate:
# Bladesong ativado durante o combate(soma Inteligência na CA), armadura arcana já ativada também

# Stats:
# STR: 8 | DEX: 18 | CON: 16 | INT:16 | WIS:8 | CHA:8
import random
from colorama import init, Fore, Style, Back

init(autoreset=True)

bonusProficiencia = 3


class Mago:

    espacos1Ciclo = 4
    espacos2Ciclo = 3
    espacos3Ciclo = 2

    modDestreza = 4
    modInteligencia = 3

    dodgeAction = False

    def __init__(self):
        self.CA = 20  # CA = 13(armadura arcana) + 4(destreza) + 3(bladesong)
        self.HP = 37

    def ataqueAcerto(self):
        acao = input(
            Back.MAGENTA
            + Fore.WHITE
            + Style.BRIGHT
            + "Qual ação deseja fazer?\n(1)Lâmina das trevas + Lâmina estrondosa\n "
        )
        if acao == "1":
            d20 = random.randint(1, 20)
            d20Final = d20 + self.modDestreza + bonusProficiencia
        else:
            print(
                Back.MAGENTA + Fore.WHITE + Style.BRIGHT + "Digite uma Ação Válida!\n"
            )
        dano = 0
        if d20 == 20:  # Crítico dobra os dados
            d20Final = (
                40  # acerto automático, valor ridiculamente alto para simular isso
            )
            for i in range(1, 8):
                d8 = random.randint(1, 8)
                dano = dano + d8
            dano = dano + self.modDestreza
        else:
            for i in range(1, 4):
                d8 = random.randint(1, 8)
                dano = dano + d8
            dano = dano + self.modDestreza

        print(
            Back.MAGENTA
            + Fore.WHITE
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
            dano = int(msg[3:5])
        elif msg[:1] == "A" and int(msg[1:3]) >= self.CA:
            # Se o ataque for menor que CA+5, usa shield
            if int(msg[1:3]) < (self.CA + 5) and self.espacos1Ciclo > 0:
                self.espacos1Ciclo = self.espacos1Ciclo - 1
                print(
                    Back.MAGENTA
                    + Fore.WHITE
                    + Style.BRIGHT
                    + "Você usou Escudo Arcano! Seu inimigo errou o Ataque, seu d20 foi: "
                    + msg[1:3]
                )
                if self.espacos1Ciclo == 3:
                    print(
                        Back.MAGENTA
                        + Fore.WHITE
                        + Style.BRIGHT
                        + "\nEspaços de magia restantes:\n1º Ciclo: [x][][][]"
                    )
                if self.espacos1Ciclo == 2:
                    print(
                        Back.MAGENTA
                        + Fore.WHITE
                        + Style.BRIGHT
                        + "\nEspaços de magia restantes:\n1º Ciclo: [x][x][][]"
                    )
                if self.espacos1Ciclo == 1:
                    print(
                        Back.MAGENTA
                        + Fore.WHITE
                        + Style.BRIGHT
                        + "\nEspaços de magia restantes:\n1º Ciclo: [x][x][x][]"
                    )
                if self.espacos1Ciclo == 0:
                    print(
                        Back.MAGENTA
                        + Fore.WHITE
                        + Style.BRIGHT
                        + "\nEspaços de magia restantes:\n1º Ciclo: [x][x][x][x]"
                    )
                dano = 0
            else:
                dano = int(msg[3:5])
        else:
            print(
                Back.MAGENTA
                + Fore.WHITE
                + Style.BRIGHT
                + "Seu inimigo errou o Ataque, seu d20 foi: "
                + msg[1:3]
            )
            dano = 0

        print(Back.MAGENTA + Fore.WHITE + Style.BRIGHT + "Dano recebido : " + str(dano))

        nova_vida = self.HP - dano
        self.HP = nova_vida
        return nova_vida
