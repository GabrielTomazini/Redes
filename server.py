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

        # Definindo a classe com base no parâmetro recebido
        if className.upper() == "Barbaro".upper():
            self.classeName = Barbarian()
        elif className.upper() == "Mago".upper():
            self.classeName = Wizard()
        elif className.upper() == "Ladino".upper():
            self.classeName = Rogue()
        elif className.upper() == "Clerigo".upper():
            self.classeName = Cleric()


def main():
    socketConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = ("127.0.0.1", 50000)
    socketConnection.bind(address)
    socketConnection.listen(1)

    [player, _] = socketConnection.accept()

    character = Character("Ronaldo, o Grande", "Barbaro")

    finished = False

    while not finished:
        print("Sua vez")

        msg = character.classe.ataqueAcerto()  # Atacando o Inimigo,

        player.send(
            msg.encode()
        )  # enviar teste ou D20 e o dano, msg = 'AD' + '18' + '30'

        retorno = player.recv(1)  # mensagem

        if not retorno:
            sys.exit(-1)
        retorno = retorno.decode()

        if retorno == "D":
            acaoInimigo = player.recv(9)  # teste ou D20 e o Dano
            acaoInimigo = acaoInimigo.decode()

            hpRestante = character.ataqueRecebido(acaoInimigo)
            print("Seu HP restante: ", hpRestante)
            if hpRestante <= 0:
                player.send("V".encode())
                encerrado = True
                break
            # msg = 'AD' + '18' + '30'
        elif retorno == "V":
            print(f"{character.nome} venceu!")
            encerrado = True
            break


if __name__ == "__main__":
    main()
