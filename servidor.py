import random
import socket
import sys
from barbaro import Barbaro
from clerigo import Clerigo
from colorama import init, Fore, Back, Style

init(autoreset=True)

bonusProeficiencia = 3

class Personagem:
    def __init__(self,classe):
        self.nome = None
        self.classe = None
        
        # Definindo a classe com base no parâmetro recebido
        if classe == '1':
            self.nome = "GROAK"
            print(Fore.RED + "Você escolheu um Barbaro!! \n Parabéns por escolher o Herói GROAK ")
            self.classe = Barbaro()
        elif classe == '2':
            self.classe = Mago()
        elif classe == "Ladino":
            self.classe = Ladino()
        elif classe == '3':
            self.nome = "Nephis"
            print(Fore.YELLOW + "Você escolheu um clerigo!! \n Parabéns por escolher a ESTRELA DA MUDANÇA NEPHIS <3 ")
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

        print(Fore.RED + "Texto em vermelho")
        print(Fore.GREEN + "Texto em verde")
        print(Fore.YELLOW + "Texto em amarelo")
        print(Fore.BLUE + "Texto em azul")
        print(Fore.MAGENTA + "Texto em magenta")
        print(Fore.CYAN + "Texto em ciano")
        print(Fore.WHITE + "Texto em branco")

        # Fundo com cores
        print(Back.RED + "Fundo vermelho")
        print(Back.GREEN + "Fundo verde")
        print(Back.YELLOW + "Fundo amarelo")
        print(Back.BLUE + "Fundo azul")
        print(Back.MAGENTA + "Fundo magenta")
        print(Back.CYAN + "Fundo ciano")
        print(Back.WHITE+ Fore.RED + "Fundo branco")

        # Usando estilo
        print(Style.BRIGHT + "Texto brilhante (negrito)")
        print(Style.NORMAL + "Texto normal")
        print(Style.RESET_ALL + "Texto resetado para padrão")

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
