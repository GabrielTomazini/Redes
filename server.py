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

        # Definindo a classe com base no parâmetro recebido
        if className.upper() == "Barbaro".upper():
            self.className = Barbarian()
        elif className.upper() == "Mago".upper():
            self.className = Wizard()
        elif className.upper() == "Ladino".upper():
            self.className = Rogue()
        elif className.upper() == "Clerigo".upper():
            self.className = Cleric()


def main():
    socketConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = ("127.0.0.1", 50000)
    socketConnection.bind(address)
    socketConnection.listen(1)

    [player, _] = socketConnection.accept()

    character = Character(
        input("Digite o nome do personagem:"), input("Digite a classe do personagem:")
    )

    finished = False

    while not finished:
        print("Sua vez!\n")

        msg = character.className.whichAction()  # Escolhendo a ação,

        player.send(msg.encode())

        retorno = player.recv(1)  # mensagem

        if not retorno:
            sys.exit(-1)
        retorno = retorno.decode()

        if retorno == "A":
            enemyAction = player.recv(9)
            enemyAction = enemyAction.decode()

            remainingHP = character.className.receivedAttack(enemyAction)
            print("Seu HP restante é: ", remainingHP)
            if remainingHP <= 0:
                player.send("V".encode())
                finished = True
                break
            # msg = 'AD' + '18' + '30'
        elif retorno == "V":
            print(f"{character.name} Ganhou!\n")
            finished = True
            break


if __name__ == "__main__":
    main()
