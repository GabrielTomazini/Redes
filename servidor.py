import random
import socket
import sys
from barbaro import Barbaro
from mago import Mago
from ladino import Ladino
from clerigo import Clerigo

# Comentário de versão, testes etc.
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
            print("Classe não reconhecida!")

    def ataqueRecebido(self, msg):
        """
        Processa o ataque recebido, considerando se o inimigo acertou ou não
        e calculando o dano.
        """
        if msg[:2] == "AD" and int(msg[2:4]) > self.getTeste(msg[4:7]):
            dano = int(msg[7:9])
        elif msg[:2] == "AM" and int(msg[2:4]) > self.classe.CA:
            dano = int(msg[4:6])
        elif msg[:2] == "ES":  # Verificando se é um ataque especial
            print(f"O inimigo usou uma habilidade especial!")
        else:
            print("Seu inimigo errou o ATAQUE, seu D20 foi: ", msg[2:4])
            dano = 0

        print("DANO RECEBIDO : ", dano)
        nova_vida = self.getVida() - dano
        self.setVida(nova_vida)
        return nova_vida

    def getVida(self):
        return self.classe.HP

    def setVida(self, novaVida):
        self.classe.HP = novaVida

    def especial(self):
        # Chama o especial da classe
        return self.classe.usarEspecial()

    def getTeste(self, habilidade):
        return random.randint(1, 20) 

def main():
    # Configurando o servidor
    socketConexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    endereco = ("127.0.0.1", 50000)
    socketConexao.bind(endereco)
    socketConexao.listen(1)

    # Espera por um cliente (Jogador)
    [jogador, _] = socketConexao.accept()

    # Criando o personagem do servidor
    personagem1 = Personagem(
        input("Digite o nome do Personagem 1: "),
        input("Digite a classe do Personagem 1: "),
    )

    encerrado = False

    while not encerrado:
        print("Sua vez")

        # Aqui o servidor escolhe entre ataque normal ou especial
        escolha = input("Digite 'A' para atacar ou 'E' para usar especial: ").strip().upper()
        if escolha == 'A':
            msg = personagem2.classe.ataqueAcerto()  # Atacar inimigo
            jogador.send(msg.encode())  # Envia a mensagem de ataque
        elif escolha == 'E':
            # Usando o especial da classe
            msg_especial = personagem2.especial()
            jogador.send(msg_especial.encode())  # Envia a mensagem do especial
            print(f"{personagem2.nome} usou seu especial!")

        jogador.send(msg.encode())  # Envia a mensagem de ataque (ex: 'AD18 30' ou 'ES15 30')

        retorno = jogador.recv(1)  # Recebe o retorno (se for 'D' ou 'V')
        if not retorno:
            sys.exit(-1)

        retorno = retorno.decode()

        if retorno == "D":
            acaoInimigo = jogador.recv(9)  # Recebe o ataque do inimigo
            acaoInimigo = acaoInimigo.decode()

            hpRestante = personagem1.ataqueRecebido(acaoInimigo)  # Calcula o dano
            print("Seu HP restante: ", hpRestante)

            if hpRestante <= 0:
                jogador.send("V".encode())  # Envia 'V' para indicar que o inimigo venceu
                encerrado = True
                break

        elif retorno == "V":
            print(f"{personagem1.nome} venceu!")
            encerrado = True
            break

if __name__ == "__main__":
    main()
