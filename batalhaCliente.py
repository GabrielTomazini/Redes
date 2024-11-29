class BatalhaNaval:

    def  __init__(self, tamanho: int, navios: list):
        
        self.tamanho = tamanho
        self.tabuleiro = [[-1] * tamanho for _ in range(tamanho)]
        self.tiros = [[0] * tamanho for _ in range(tamanho)]
        self.navios = navios
        self.numeroAtaques = [0,0,0]
        self.numeroNavios = len(navios)

        for i in range(len(self.navios)):
            valido = False
            while not valido:
                linha = int(input('Digite a linha em que deseja colocar o navio ' + str(i) + ', de tamanho ' + str(navios[i]) + ': '))
                coluna = int(input('Digite a coluna em que deseja colocar o navio ' + str(i) + ', de tamanho ' + str(navios[i]) + ': '))
                direcao = input('Digite a direção que deseja colocar o navio ' + str(i) + ' (N, S, L, O): ')
                if self.__verificarPosicao__(self.navios[i], linha, coluna, direcao):
                    valido = True
                    if (direcao == 'N'):
                        for _ in range(self.navios[i]):
                            self.tabuleiro[linha][coluna] = i
                            linha -= 1
                    elif (direcao == 'S'):
                        for _ in range(self.navios[i]):
                            self.tabuleiro[linha][coluna] = i
                            linha += 1
                    elif (direcao == 'L'):
                        for _ in range(self.navios[i]):
                            self.tabuleiro[linha][coluna] = i
                            coluna += 1
                    elif (direcao == 'O'):
                        for _ in range(self.navios[i]):
                            self.tabuleiro[linha][coluna] = i
                            coluna -= 1
                else:
                    print('Impossivel posicionar do modo desejado, tente novamente.')

    def __verificarPosicao__(self, navio, linha, coluna, direcao):
        if (linha < 0 or coluna < 0 or linha >= self.tamanho or coluna >= self.tamanho):
            return False
        if (direcao not in ['N', 'S', 'L', 'O']):
            return False
        if (direcao == 'N'):
            if (linha - navio + 1 < 0):
                return False
            for _ in range(navio):
                if self.tabuleiro[linha][coluna] != -1:
                    return False
                linha -= 1
        elif (direcao == 'S'):
            if (linha + navio - 1 >= self.tamanho):
                return False
            for _ in range(navio):
                if self.tabuleiro[linha][coluna] != -1:
                    return False
                linha += 1
        elif (direcao == 'L'):
            if (coluna + navio - 1 >= self.tamanho):
                return False
            for _ in range(navio):
                if self.tabuleiro[linha][coluna] != -1:
                    return False
                coluna += 1
        elif (direcao == 'O'):
            if (coluna - navio + 1 < 0):
                return False
            for _ in range(navio):
                if self.tabuleiro[linha][coluna] != -1:
                    return False
                coluna -= 1
        return True

    def checarAtaqueRecebido(self, tiroLinha: int, tiroColuna: int):
        resultado = None
        if (self.tabuleiro[tiroLinha][tiroColuna] == -1):
            resultado = -1
            self.tabuleiro[tiroLinha][tiroColuna] = -2
        elif (self.tabuleiro[tiroLinha][tiroColuna] == -2 or self.tabuleiro[tiroLinha][tiroColuna] == -3):
            resultado = -2
        else:
            indiceNavioAtacado = self.tabuleiro[tiroLinha][tiroColuna]
            resultado = self.navios[indiceNavioAtacado]
            self.numeroAtaques[indiceNavioAtacado] += 1
            self.tabuleiro[tiroLinha][tiroColuna] = -3
            if self.navios[indiceNavioAtacado] == self.numeroAtaques[indiceNavioAtacado]:
                self.numeroNavios -=1
        
        return resultado, self.numeroNavios
    
    def imprimirTabuleiro(self):
        print('Seu tabuleiro:')
        for i in range(len(self.tabuleiro)):
            for j in range(len(self.tabuleiro[i])):
                if (self.tabuleiro[i][j] == -1): # ainda não atacado
                    print('  ', end="")
                elif (self.tabuleiro[i][j] == -2): # tiro errado
                    print('o ', end="")
                elif (self.tabuleiro[i][j] == -3): # tiro certo
                    print('* ', end="")
                else:
                    print(str(self.tabuleiro[i][j]) + ' ', end="")
            print('\n')

    def atirar(self):
        while True:
            seuTiroLinha = int(input('Digite a linha do seu tiro: '))
            seuTiroColuna = int(input('Digite a coluna do seu tiro: '))
            if (seuTiroLinha >= 0 and seuTiroLinha < self.tamanho and seuTiroColuna >= 0 and seuTiroColuna < self.tamanho):
                return [seuTiroLinha, seuTiroColuna]
            
    def gravarTiro(self, linha, coluna, resultado):
        if (resultado == -1):
            print('Você errou o tiro')
            self.tiros[linha][coluna] = resultado
        elif (resultado == -2 or resultado == -3):
            print('Você já tinha atirado nesse lugar')
        else:
            print('Você acertou o navio ' + str(resultado))
            self.tiros[linha][coluna] = resultado

    def imprimirTiros(self):
        print('Seus tiros:')
        for i in range(len(self.tiros)):
            for j in range(len(self.tiros[i])):
                if (self.tiros[i][j] == 0): # ainda não atacado
                    print(chr(219) + " ", end="")
                elif (self.tiros[i][j] == -1): # tiro errado
                    print('  ', end="")
                else:
                    print(str(self.tiros[i][j]) + ' ', end="")
            print('\n')

import socket
import sys

def main():

    jogador = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    endereco = ('127.0.0.1', 50000)
    
    jogador.connect(endereco)

    tamanho = 8
    navios = [3,2,1]
    tabuleiro = BatalhaNaval(tamanho, navios)

    encerrado = False

    while not encerrado:

        codigo = jogador.recv(1)
        if not codigo:
            sys.exit(-1)
        codigo = codigo.decode()
        if (codigo == 'A'):
            linha = jogador.recv(1)
            coluna = jogador.recv(1)
            linha = int.from_bytes(linha, 'big')
            coluna = int.from_bytes(coluna, 'big')
            [resultado, naviosRestantes] = tabuleiro.checarAtaqueRecebido(linha, coluna)
            if (naviosRestantes == 0):
                msg = 'V'
                msg = msg.encode()
                jogador.send(msg)
            else:
                msg = 'R'.encode() + resultado.to_bytes(length=1, byteorder='big', signed=True)
                jogador.send(msg)
        else:
            print('Algo deu errado')
            sys.exit(-2)

        if (naviosRestantes == 0):
            print('Jogador 1 venceu')
            encerrado = True

        if not encerrado:

            print('sua vez')
            tabuleiro.imprimirTiros()
            [linhaTiro, colunaTiro] = tabuleiro.atirar()

            msg = 'A'.encode()
            msg += linhaTiro.to_bytes(1, 'big')
            msg += colunaTiro.to_bytes(1, 'big')

            jogador.send(msg)

            retorno = jogador.recv(1)
            if not retorno:
                sys.exit(-1)
            retorno = retorno.decode()

            if(retorno == 'R'):
                acao = jogador.recv(1)
                acao = int.from_bytes(bytes = acao, byteorder='big', signed=True)
                tabuleiro.gravarTiro(linhaTiro, colunaTiro, acao)
            elif (retorno == 'V'):
                print('Você venceu')
                encerrado = True
            else:
                pass


if __name__ == '__main__':
    main()