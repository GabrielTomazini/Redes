import random
import socket
import sys
from barbaro import Barbaro
from mago import Mago
from ladino import Ladino
from clerigo import Clerigo

bonusProeficiencia = 3

class Personagem:
   def __init__(self,classe):
        self.nome = None
        self.classe = None
        
        # Definindo a classe com base no parâmetro recebido
        if classe == '1':
            self.nome = "GROAK"
            print("Você escolheu um Barbaro!! \n Parabéns por escolher o Herói GROAK")
            self.classe = Barbaro()
        elif classe == '2':
            self.classe = Mago()
        elif classe == "Ladino":
            self.classe = Ladino()
        elif classe == "Clerigo":
            self.classe = Clerigo()

def main():
    jogador = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    endereco = ('127.0.0.1', 50000)
  
    jogador.connect(endereco)

    personagem2 = Personagem(input('Digite a classe do Personagem 2:\n (1) Barbaro\n (2) Mago\n (3)Clerigo\n  '))

    encerrado = False
    
    while not encerrado:
        codigo = jogador.recv(1)  # Receber se ganhou ou não o Jogador 1
        if not codigo:
            sys.exit(-1)
        
        codigo = codigo.decode()
        if codigo == 'D':
            acaoInimigo = jogador.recv(9)  # Receber Ataque inimigo
            acaoInimigo = acaoInimigo.decode()

            hpRestante = personagem2.classe.ataqueRecebido(acaoInimigo)
            print("Seu HP eh: ", hpRestante)
            if hpRestante <= 0:
                jogador.send('V'.encode())  # Envia "V" para indicar vitória
                encerrado = True
                break

            print('Sua vez')
            msg = personagem2.classe.ataqueAcerto()  # Atacar inimigo
            jogador.send(msg.encode())  # Envia a mensagem de ataque

        elif(codigo == 'V'):
            print('Cliente Ganhou/n')
            sys.exit(-2)

if __name__ == '__main__':
    main()
