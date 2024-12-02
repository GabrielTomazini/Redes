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
            self.nome = "Nephis"
            print("Você escolheu um clerigo!! \n Parabéns por escolher a ESTRELA DA MUDANÇA NEPHIS <3")
            self.classe = Clerigo()

    def ataqueRecebido(self , msg):
        
        if msg[:1] == "E" and int(msg[1:3]) > self.getTeste(msg[1:3]):
            dano = int(msg[3:5])
        elif msg[:1] == "A" and int(msg[1:3]) > self.classe.CA:  
            dano = int(msg[3:5])
        else:
            print("Seu inimigo errou o ATAQUE, seu D20 foi: ",msg[1:3])
            dano = 0
        print("DANO RECEBIDO : ", dano)
        nova_vida = self.getVida() - dano
        self.setVida(nova_vida)
        return nova_vida
    
    def getVida(self):
        return self.classe.HP
    
    def setVida(self, novaVida):
        self.classe.HP = novaVida

def main():

    socketConexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    endereco = ('127.0.0.1', 50000)
    socketConexao.bind(endereco)
    socketConexao.listen(1)

    [jogador, _] = socketConexao.accept()

    personagem1 = Personagem(input('Digite a classe do Personagem 1:\n (1) Barbaro\n (2) Mago\n (3)Clerigo\n  '))

    encerrado = False
    
    while not encerrado:
        print('Sua vez')

        msg = personagem1.classe.ataqueAcerto()  # Atacando o Inimigo,
        
        jogador.send(msg.encode()) # enviar teste ou D20 e o dano, msg = D +'AD' + '18' + '30' 

        retorno = jogador.recv(1) # mensagem
        
        if not retorno:
            sys.exit(-1)
        retorno = retorno.decode()

        if retorno == 'D':
            acaoInimigo = jogador.recv(6) # teste ou D20 e o Dano 
            acaoInimigo = acaoInimigo.decode()  
            print(acaoInimigo)
            hpRestante = personagem1.classe.ataqueRecebido(acaoInimigo)
            print("Seu HP restante: ", hpRestante)
            if (hpRestante <= 0):
                jogador.send('V'.encode())
                encerrado = True
                break
            # msg = 'AD' + '18' + '30'
        elif(retorno =='V'):
            print(f'{personagem1.nome} venceu!')
            encerrado = True
            break

if __name__ == '__main__':
    main()
