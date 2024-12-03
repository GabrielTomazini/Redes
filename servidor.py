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

    def ataqueRecebido(self, msg):

        if msg[:1] == "E" and int(msg[1:3]) > self.getTeste(msg[1:3]):
            dano = int(msg[3:5])
        elif msg[:1] == "A" and int(msg[1:3]) > self.classe.CA:
            dano = int(msg[3:5])
        else:
            print(
                Fore.CYAN + "Seu inimigo errou o Ataque, seu d20 foi: ",
                Fore.CYAN + msg[1:3],
            )
            dano = 0
        print(Fore.CYAN + "Dano recebido: ", Fore.CYAN + dano)
        nova_vida = self.getVida() - dano
        self.setVida(nova_vida)
        return nova_vida

    def getVida(self):
        return self.classe.HP

    def setVida(self, novaVida):
        self.classe.HP = novaVida


def main():

    socketConexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    endereco = ("127.0.0.1", 50000)
    socketConexao.bind(endereco)
    socketConexao.listen(1)

    [jogador, _] = socketConexao.accept()

    personagem1 = Personagem(
        input(
            Fore.YELLOW
            + "Escolha a classe do Personagem 1:\n(1)Barbaro\n(2)Mago\n(3)Clerigo\n(4)Ladino\n "
        )
    )

    encerrado = False

    while not encerrado:
        print(Fore.CYAN + "Sua vez\n")
        msg = personagem1.classe.ataqueAcerto()  # Atacando o Inimigo,

        jogador.send(
            msg.encode()
        )  # enviar teste ou D20 e o dano, msg = D +'AD' + '18' + '30'

        retorno = jogador.recv(1)  # mensagem

        if not retorno:
            sys.exit(-1)
        retorno = retorno.decode()

        if retorno == "D":
            acaoInimigo = jogador.recv(6)  # teste ou D20 e o Dano
            acaoInimigo = acaoInimigo.decode()
            hpRestante = personagem1.classe.ataqueRecebido(acaoInimigo)
            print(Fore.CYAN + "\nSeu HP restante é: " + str(hpRestante))
            if hpRestante <= 0:
                jogador.send("V".encode())
                encerrado = True
                break
            # msg = 'AD' + '18' + '30'
        elif retorno == "V":
            print(Fore.YELLOW + f"\n👑 {personagem1.nome} Ganhou!👑\n")
            encerrado = True
            break


if __name__ == "__main__":
    main()
