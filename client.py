import socket
import sys
from Classes.Barbarian import Barbarian
from Classes.Cleric import Cleric
from Classes.Rogue import Rogue
from Classes.Wizard import Wizard

proficiencyBonus = 3


class Character:
    def __init__(self, name, className):
        self.name = name
        self.className = None

        # Choosing the class based on receipt parameter
        if className.upper() == "Barbaro".upper():
            self.className = Barbarian()
        elif className.upper() == "Mago".upper():
            self.className = Wizard()
        elif className.upper() == "Ladino".upper():
            self.className = Rogue()
        elif className.upper() == "Clerigo".upper():
            self.className = Cleric()


def main():
    player = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = ("127.0.0.1", 50000)
    player.connect(address)

    character2 = Character(
        input("Digite o nome do personagem:"), input("Digite a classe do personagem:")
    )

    finished = False

    while not finished:
        code = player.recv(1)  # Receber se ganhou ou não o player 1
        if not code:
            sys.exit(-1)

        code = code.decode()
        if code == "A":
            enemyAction = player.recv(9)  # Receber Ataque inimigo
            enemyAction = enemyAction.decode()

            remainingHP = character2.className.receivedAttack(enemyAction)
            print("Seu HP restante é: ", remainingHP, " \n")
            if remainingHP <= 0:
                player.send("V".encode())  # Envia "V" para indicar vitória
                finished = True
                break

            print("Sua vez")
            msg = character2.className.whichAction()  # Atacar inimigo
            player.send(msg.encode())  # Envia a mensagem de ataque

        elif code == "V":
            print(f"{character2.name} Ganhou!\n")
            sys.exit(-2)


if __name__ == "__main__":
    main()
