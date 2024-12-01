import random
import sys

# Level 5 Barbarian Bear Totem Subclass
# Stats:
# STR: 18 | DEX: 16 | CON: 16 | INT:8 | WIS:8 | CHA:8

proficiencyBonus = 3


class Barbarian:

    strengthModifier = 4
    dexterityModifier = 3
    constitutionModifier = 3
    intelligenceModifier = -1
    wisdomModifier = -1
    charismaModifier = -1

    furyExtraDamage = 2

    def __init__(self):
        self.CA = 10 + self.dexterityModifier + self.constitutionModifier
        self.HP = 55

    def attackRoll(self):
        vectorAttacks = []
        numberOfAttacks = 2
        for i in range(numberOfAttacks):
            d20 = random.randint(1, 20)
            total_attack_roll_value = d20 + proficiencyBonus + self.strengthModifier
            vectorAttacks.append(total_attack_roll_value)
        return vectorAttacks

    def attackDamage(self, attacks):
        total_damage = []
        for i in range(len(attacks)):
            d12 = random.randint(1, 12)
            damage = d12 + self.strengthModifier + self.furyExtraDamage
            total_damage.append(damage)
        # Mensagem ficará nesse formato:
        # AA06111909 A{d20Ataque1}{dano}{d20Ataque2}{dano}
        msg = (
            "AA"
            + str(attacks[0]).zfill(2)
            + str(total_damage[0]).zfill(2)
            + str(attacks[1]).zfill(2)
            + str(total_damage[1]).zfill(2)
        )
        return msg

    def whichAction(self):
        attacks = []
        action = input("Qual ação o personagem fará? (1-Ataque) ")
        if int(action) == 1:
            attacks = self.attackRoll()
            msg = self.attackDamage(attacks)
            return msg
        else:
            print("Ação inválida, digite uma ação válida!\n")

    def receivedAttack(self, msg):
        total_damage = 0
        attack1 = False
        attack2 = False
        if msg[:1] == "A":  # carater 0
            if int(msg[1:3]) >= self.CA:  # 1:3 = caracter 1 e 2
                total_damage = int(msg[3:5])  # 3:5 = caracter 3 e 4
                print(
                    "Seu inimigo acertou o ataque! \n d20: ",
                    msg[1:3],
                    " dano: ",
                    msg[3:5],
                    "\n",
                )
                attack1 = True
            if int(msg[5:7]) >= self.CA:  # 5:7 = caracter 5 e 6
                total_damage = total_damage + int(msg[7:9])  # 5:7 = caracter 7 e 8
                print(
                    "Seu inimigo acertou o ataque! \n d20: ",
                    msg[5:7],
                    " dano: ",
                    msg[7:9],
                    "\n",
                )
                attack2 = True
            if not attack1:
                print("Seu inimigo errou o ataque! \n d20:", msg[1:3], "\n")
            if not attack2:
                print("Seu inimigo errou o ataque! \n d20:", msg[5:7], "\n")
        else:
            print("Mensagem não identificada, algo deu errado!\n")
            sys.exit(-1)

        newHP = self.getHP() - total_damage
        self.setHP(newHP)
        return newHP

    def getHP(self):
        return self.HP

    def setHP(self, newHP):
        self.HP = newHP
