import Carta as crt
import random

class Baralho(object):
    def __init__(self):
        self.__naipes = ["♥", "♠", "♦", "♣"]
        self.__simbolos = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        self.baralho = []

        for i in range(len(self.__naipes)):
            for j in range(len(self.__simbolos)):
                self.baralho.append((crt.Carta(self.__naipes[i], self.__simbolos[j])))
        Baralho.embaralha(self.baralho)

    def __str__(self):
        baralho = self.baralho
        s = ""
        for a in range(0, 52, 13):
            for i in range(5):
                base = i * 8
                for c in range(a, a + 13):
                    p = str(baralho[c])
                    s += p[base:base+7]
                    s += "    "
                s += "\n"
        return s

    def getBaralho(self):
        return self.baralho

    def getMao(self, n = 5):
        mao = []
        for i in range(n):
            mao.append(self.baralho[i])
            self.baralho.pop(0)
        return mao

    def pegarCarta(self):
        cartaRetirada = self.baralho.pop(0)
        return cartaRetirada

    @staticmethod
    def embaralha(baralho):
        random.shuffle(baralho)



def main():
    # OBS: usar um terminal com um tamanho de pelo menos 143 x 22 para visualizar o baralho inteiro
    baralho = Baralho()
    print(len(baralho.baralho))
    print(baralho)
    return 0

if __name__ == "__main__":
    main()