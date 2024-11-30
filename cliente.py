import random
import socket
import sys
from barbaro import Barbaro
from mago import Mago
from ladino import Ladino
from clerigo import Clerigo

bonusProeficiencia = 3

class Personagem:
    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = None
        
        # Definindo a classe com base no parâmetro recebido
        if classe == "Barbaro":
            self.classe = Barbaro()
        elif classe == "Mago":
            self.classe = Mago()
        elif classe == "Ladino":
            self.classe = Ladino()
        elif classe == "Clerigo":
            self.classe = Clerigo()
        else:
            raise ValueError("Classe inválida!")
    
    def ataqueRecebido(self, msg):
        # Processando ataque físico ou mágico
        if msg[:2] == "AD" and int(msg[2:4]) > self.getTeste(msg[4:7]):
            dano = int(msg[7:9])
        elif msg[:2] == "AM" and int(msg[2:4]) > self.classe.CA:  
            dano = int(msg[4:6])
        elif msg[:2] == "ES":  # Verificando se é um ataque especial
            print(f"O inimigo usou uma habilidade especial!")
        else:
            print("Seu inimigo errou o ATAQUE, seu D20 foi: ", msg[2:4])
            dano = 0
        nova_vida = self.getVida() - dano
        self.setVida(nova_vida)
        return nova_vida

    def getVida(self):
        return self.classe.HP

    def setVida(self, novaVida):
        self.classe.HP = novaVida

    def getTeste(self, habilidade):
        return random.randint(1, 20) 

    def especial(self):
        # Chama o especial da classe
        return self.classe.usarEspecial()

def main():
    jogador = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    endereco = ('127.0.0.1', 50000)
    jogador.connect(endereco)

    # Recebe o nome e classe do personagem
    nome_personagem = input('Digite o nome do seu Personagem: ')
    classe_personagem = input('Digite a classe do seu Personagem: ')

    personagem2 = Personagem(nome_personagem, classe_personagem)

    encerrado = False
    
    while not encerrado:
        codigo = jogador.recv(1)  # Receber se ganhou ou não o Jogador 1
        if not codigo:
            sys.exit(-1)
        
        codigo = codigo.decode()
        if codigo == 'D':
            acaoInimigo = jogador.recv(9)  # Receber Ataque inimigo
            acaoInimigo = acaoInimigo.decode()

            hpRestante = personagem2.ataqueRecebido(acaoInimigo)
            print("Seu HP é: ", hpRestante)
            if hpRestante <= 0:
                jogador.send('V'.encode())  # Envia "V" para indicar vitória
                encerrado = True
                break

            print('Sua vez')
            escolha = input("Digite 'A' para atacar ou 'E' para usar especial: ").strip().upper()
            if escolha == 'A':
                msg = personagem2.classe.ataqueAcerto()  # Atacar inimigo
                jogador.send(msg.encode())  # Envia a mensagem de ataque
            elif escolha == 'E':
                # Usando o especial da classe
                msg_especial = personagem2.especial()
                jogador.send(msg_especial.encode())  # Envia a mensagem do especial
                print(f"{personagem2.nome} usou seu especial!")

        elif codigo == 'V':
            print('Cliente Ganhou!')
            sys.exit(-2)

if __name__ == '__main__':
    main()
