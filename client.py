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
        if code == "A":
            acaoInimigo = player.recv(9)  # Receber Ataque inimigo
            acaoInimigo = acaoInimigo.decode()

            hpRestante = character2.receivedAttack(acaoInimigo)
            print("Seu HP eh: ", hpRestante)
            if hpRestante <= 0:
                player.send("V".encode())  # Envia "V" para indicar vitória
                finished = True
                break

            print("Sua vez")
            msg = character2.className.attackDamage(2)  # Atacar inimigo
            player.send(msg.encode())  # Envia a mensagem de ataque

        elif code == "V":
            print("Cliente Ganhou/n")
            sys.exit(-2)


if __name__ == "__main__":
    main()
