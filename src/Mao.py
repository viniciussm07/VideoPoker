class Mao(object):

    def __init__(self):
        self.saldo = 200
        self.aposta = 0
        self.mao = []

    def add(self):
        if royalStraightFlush(self.mao):
            self.saldo += self.aposta * 200
        elif straightFlush(self.mao):
            self.saldo += self.aposta * 100
        elif quadra(self.mao):
            self.saldo += self.aposta * 50
        elif fullHand(self.mao):
            self.saldo += self.aposta * 20
        elif flush(self.mao):
            self.saldo += self.aposta * 10
        elif straight(self.mao):
            self.saldo += self.aposta * 5
        elif trinca(self.mao):
            self.saldo += self.aposta * 2
        elif doisPares(self.mao):
            self.saldo += self.aposta
        else:
            self.saldo -= self.aposta
    
    def setAposta(self, aposta):
        if self.saldo < aposta:
            print("Faça uma aposta menor ou igual ao seu saldo")
            return
        else:
            self.aposta = aposta

    def fimDeJogo(self):
        if self.saldo == 0: return True
        else: return False

    #Dois pares x1
    #Trinca x2