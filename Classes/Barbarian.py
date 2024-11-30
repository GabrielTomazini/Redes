import random


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
            d20 = random.randomint(1, 20)
            total_attack_roll_value = d20 + proficiencyBonus + self.strengthModifier
            vectorAttacks.append(total_attack_roll_value)
        return vectorAttacks

    def attackDamage(self, successfulAttacks):
        total_damage = 0
        for i in range(successfulAttacks):
            d12 = random.randint(1, 12)
            total_damage = (
                total_damage + d12 + self.strengthModifier + self.furyExtraDamage
            )
        # Mensagem ficará nesse formato:
        # A0613 ou A1907
        msg = "A" + str(random.randint(1, 20)).zfill(2) + str(total_damage).zfill(2)
        return msg

    def whichAction(self):
        attacks = []
        action = input("Qual ação o personagem fará? 1-Ataque\n")
        if action == 1:
            attacks = self.attackRoll()

        else:
            print("Ação inválida, digite uma ação válida!\n")
