import Baralho as brl

class Mao(object):

    def __init__(self, baralho, n = 5):
        self.__saldo = 200
        self.aposta = 0
        self.mao = baralho.getMao()

    def __str__(self):
        mao = self.mao
        s = ""
        for i in range(5):
            base = i * 8
            for c in mao:
                p = str(c)
                s += p[base:base+7]
                s += "    "
            s += "\n"
        return s
    
    def getMao(self, n = 5):
        return self.mao

    def trocarCartas(self, baralho):
        troca = input("Insira quais cartas deseja trocar separadas por espaço\n").split()

        for i in range(len(troca)):
            try:
                troca[i] = int(troca[i]) - 1
            except:
                print("Você não digitou um número ou digitou algum número maior que a quantidade de cartas em sua mão")
        for i in range(len(troca)):
            self.mao[troca[i]] = baralho.pegarCarta()

    def add(self):
        copiaMao = self.mao.copy()
        copiaMao = Mao.ordena(copiaMao)

        if Mao.royalStraightFlush(copiaMao):
            self.__saldo += self.aposta * 200
            print("Parabéns!!!!\nVocê acabou de fazer um Royal Straight Flush!\nSeu saldo atua é de {:d}".format(self.__saldo))
        elif Mao.straightFlush(copiaMao):
            self.__saldo += self.aposta * 100
            print("Parabéns!\nVocê acabou de fazer um Straight Flush!\nSeu saldo atua é de {:d}".format(self.__saldo))
        elif Mao.quadra(copiaMao):
            self.__saldo += self.aposta * 50
        elif Mao.fullHand(copiaMao):
            self.__saldo += self.aposta * 20
            print("Full Hand")
        elif Mao.flush(copiaMao):
            self.__saldo += self.aposta * 10
        elif Mao.straight(copiaMao):
            self.__saldo += self.aposta * 5
        elif Mao.trinca(copiaMao):
            self.__saldo += self.aposta * 2
        elif Mao.doisPares(copiaMao):
            self.__saldo += self.aposta
        else:
            self.__saldo -= self.aposta
        return
        
    def getSaldo(self):
        return self.__saldo
    
    def setAposta(self, aposta):
        if self.__saldo < aposta:
            print("Faça uma aposta menor ou igual ao seu saldo")
            return
        else:
            self.aposta = aposta

    def fimDeJogo(self):
        if self.__saldo == 0: return True
        else: return False

    @staticmethod
    def ordena(mao):
        for i in range(len(mao) - 1):
            for j in range(i, len(mao)):
                if mao[i].getSimbolo() > mao[j].getSimbolo():
                    aux = mao[i]
                    mao[i] = mao[j]
                    mao[j] = aux
        return mao

    @staticmethod
    def royalStraightFlush(mao):
        if (mao[0].getSimbolo == 10) and (Mao.flush(mao)) and (Mao.straight(mao)): return True
        else: return False
    
    @staticmethod
    def straightFlush(mao):
        if Mao.flush(mao) and Mao.straight(mao): return True
        else: return False
    
    @staticmethod
    def quadra(mao):
        if mao[0].getSimbolo == mao[1].getSimbolo and mao[0].getSimbolo == mao[2].getSimbolo and mao[0].getSimbolo == mao[3].getSimbolo: return True
        else: return False

    @staticmethod
    def fullHand(mao):
        if mao[0].getSimbolo == mao[1].getSimbolo and mao[2].getSimbolo == mao[3].getSimbolo and mao[2].getSimbolo == mao[4].getSimbolo or \
            mao[0].getSimbolo == mao[1].getSimbolo and mao[1].getSimbolo == mao[2].getSimbolo and mao[3].getSimbolo == mao[4].getSimbolo: return True
        else: return False

    @staticmethod
    def flush(mao):
        #TODO
        return True
    
    @staticmethod
    def straight(mao):
        #TODO
        return True

    @staticmethod
    def trinca(mao):
        #TODO
        return

    @staticmethod
    def doisPares(mao):
        #TODO
        return


def main():
    baralho = brl.Baralho()
    mao = Mao(baralho)
    print(mao)
    # mao.add()
    # print(baralho)
    mao.trocarCartas(baralho)
    # print(baralho.pegarCarta())
    print(mao)

    return

if __name__ == "__main__":
    main()