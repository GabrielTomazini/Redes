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

        def receivedAttack(self, msg):
            if msg[:2] == "A" and int(msg[1:3]) > self.className.CA:
                dano = int(msg[3:5])
            else:
                print("Seu inimigo errou o ATAQUE, seu D20 foi: ", msg[1:3])
                dano = 0
            print("DANO RECEBIDO : ", dano)
            nova_vida = self.getHP() - dano
            self.setHP(nova_vida)
            return nova_vida

        def getHP(self):
            return self.classe.HP

        def setHP(self, newHP):
            self.classe.HP = newHP


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

        msg = character.className.attackDamage()  # Atacando o Inimigo,

        player.send(
            msg.encode()
        )  # enviar teste ou D20 e o dano, msg = 'A' + '18' + '30'

        retorno = player.recv(1)  # mensagem

        if not retorno:
            sys.exit(-1)
        retorno = retorno.decode()

        if retorno == "A":
            enemyAction = player.recv(9)  # teste ou D20 e o Dano
            enemyAction = enemyAction.decode()

            leftHP = character.receivedAttack(enemyAction)
            print("Seu HP restante: ", leftHP)
            if leftHP <= 0:
                player.send("V".encode())
                finished = True
                break
            # msg = 'AD' + '18' + '30'
        elif retorno == "V":
            print(f"{character.name} venceu!")
            finished = True
            break


if __name__ == "__main__":
    main()
