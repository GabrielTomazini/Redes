import socket
import sys
from Classes import Barbarian
from Classes import Cleric
from Classes import Rogue
from Classes import Wizard

proficiencyBonus = 3


class Character:
    def __init__(self, name, className):
        self.name = name
        self.className = None

        # Choosing the class based on receipt parameter
        if className == "Barbaro".upper():
            self.classeName = Barbarian()
        elif className == "Mago".upper():
            self.classe = Wizard()
        elif className == "Ladino".upper():
            self.classe = Rogue()
        elif className == "Clerigo".upper():
            self.classe = Cleric()


def main():
    player = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = ("127.0.0.1", 50000)
    player.connect(address)

    character2 = Character("Geraldo, o Bruto", "Barbaro")

    finished = False

    while not finished:
        code = player.recv(1)  # Receber se ganhou ou não o player 1
        if not code:
            sys.exit(-1)

        code = code.decode()
        if code == "D":
            acaoInimigo = player.recv(9)  # Receber Ataque inimigo
            acaoInimigo = acaoInimigo.decode()

            hpRestante = character2.ataqueRecebido(acaoInimigo)
            print("Seu HP eh: ", hpRestante)
            if hpRestante <= 0:
                player.send("V".encode())  # Envia "V" para indicar vitória
                encerrado = True
                break

            print("Sua vez")
            msg = character2.classe.ataqueAcerto()  # Atacar inimigo
            player.send(msg.encode())  # Envia a mensagem de ataque

        elif code == "V":
            print("Cliente Ganhou/n")
            sys.exit(-2)


if __name__ == "__main__":
    main()
