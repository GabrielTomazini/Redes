import random

class Barbaro:

    def __init__(self):
        self.CA = 15
        self.HP = 50
        self.esquivo = False
        self.danoFuria = 3
        self.Imprudente = False
        self.orc = False

    def ataqueAcerto(self):
        auxiliar = 0
        dano = 0 
        imprudente = input('Deseja usar ataque imprudente?\n (1) Sim \n (2) Não\n')
        if(imprudente == '1'):
            self.Imprudente = True
        else:
            self.Imprudente = False
        ataque = input('Deseja usar ataque utilizar?\n (1) Ataque com Machado 2x (2) Modo ESQUIVOOO\n')
        if(ataque == '1'):
            d12 = random.randint(1, 12)
            print("Soma entre 5 e :  ",d12 , self.danoFuria)
            dano =  d12 + 5 + self.danoFuria
            auxiliar = random.randint(1, 20)

            if(self.Imprudente == True):
                auxiliar+=5
            print("Seu D20: \n Seu dano:",auxiliar, dano)
            
        else:
            self.esquivo = True
            auxiliar = 0
            dano = 0
            print("Modo ESQUIVO ATIVADO, ME ACERTA QUE EU DUVIDO")
        msg = 'D' + 'A' + str(auxiliar).zfill(2) + str(dano)
        return msg
        # A mensagem de ataque agora inclui o valor correto do dano
        
    
    def ataqueRecebido(self , msg):
        if(self.esquivo == True ):
            CA = self.CA + 5
        elif(self.Imprudente == True):
            CA = self.CA - 2
        else:
            CA = self.CA
        if msg[:1] == "E" and int(msg[1:3]) > self.getTeste(msg[1:3]):
            dano = int(msg[3:5])/2
        elif msg[:1] == "A" and int(msg[1:3]) > CA:  
            dano = int(msg[3:5])/2
        else:
            print("Seu inimigo errou o ATAQUE, seu D20 foi: ",msg[1:3])
            dano = 0
        print("DANO RECEBIDO : ", dano)

        nova_vida = self.HP - dano
        if(dano > 20):
            Irina = input("Você ira sofrer um dano monstruoso\n Deseja utilizar seu Trunfo Final(única utilização)? \n (1)Sim \n (2) Não\n")
            print("Sua AMADA Irina lhe salvou , Parabéns Herói GROAK, parece que até anjos estão de olho em você!!")
            nova_vida +=20 
        
        if(nova_vida == 0 and self.orc == False):
            nova_vida = 1
            self.orc = True
            print("EU SOU ORC SEU OTÁRIO!!!\n")
        
        self.HP = nova_vida
        self.Imprudente= False
        self.esquivo = False
        return nova_vida
    def getTeste(self):
        print("oi")