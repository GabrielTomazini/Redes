import random
import socket
import sys
from Classes.Barbaro import Barbaro
from Classes.Clerigo import Clerigo
from Classes.Ladino import Ladino
from Classes.Mago import Mago
from colorama import init, Fore, Back, Style

init(autoreset=True)

bonusProficiencia = 3


class Personagem:
    def __init__(self, classe):
        self.nome = None
        self.classe = None

        # Definindo a classe com base no parâmetro recebido
        if classe == "1":
            self.nome = "Groak"
            print(
                Fore.YELLOW
                + "\nVocê escolheu um Bárbaro!\nParabéns por escolher o Herói Groak!\n"
            )
            self.classe = Barbaro()
        elif classe == "2":
            self.classe = Mago()
        elif classe == "Ladino":
            self.classe = Ladino()
        elif classe == "3":
            self.nome = "Nephis"
            print(
                Fore.YELLOW
                + "\nVocê escolheu um Clérigo!\nParabéns por escolher Nephis, Estrela da mudança\n"
            )
            self.classe = Clerigo()


def main():
    jogador = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    endereco = ("127.0.0.1", 50000)

    jogador.connect(endereco)

    personagem2 = Personagem(
        input(
            Fore.YELLOW
            + "Escolha a classe do Personagem 2:\n(1)Barbaro\n(2)Mago\n(3)Clerigo\n(4)Ladino\n "
        )
    )

    encerrado = False

    while not encerrado:
        codigo = jogador.recv(1)  # Receber se ganhou ou não o Jogador 1
        if not codigo:
            sys.exit(-1)

        codigo = codigo.decode()
        if codigo == "D":
            acaoInimigo = jogador.recv(9)  # Receber Ataque inimigo
            acaoInimigo = acaoInimigo.decode()

            hpRestante = personagem2.classe.ataqueRecebido(acaoInimigo)
            print(Fore.CYAN + "\nSeu HP restante é: " + str(hpRestante))
            if hpRestante <= 0:
                jogador.send("V".encode())  # Envia "V" para indicar vitória
                encerrado = True
                break

            print(Fore.CYAN + "Sua vez\n")
            msg = personagem2.classe.ataqueAcerto()  # Atacar inimigo
            jogador.send(msg.encode())  # Envia a mensagem de ataque

        elif codigo == "V":
            print(Fore.YELLOW + f"\n👑 {personagem2.nome} Ganhou!👑\n")
            sys.exit(-2)


if __name__ == "__main__":
    main()
