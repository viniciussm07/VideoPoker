import Carta as crt
import random

class Baralho(object):
    def __init__(self):
        self.__naipes = ["♥", "♠", "♦", "♣"]
        self.__simbolos = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.baralho = []

        for i in range(len(self.__naipes)):
            for j in range(len(self.__simbolos)):
                self.baralho.append((crt.Carta(self.__naipes[i], self.__simbolos[j])))
        Baralho.embaralha(self.baralho)

    def __str__(self):
        mao = self.getMao()
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
        mao = []
        for i in range(n):
            mao.append(self.baralho[i])
            self.baralho.pop(0)
        return mao


    @staticmethod
    def embaralha(baralho):
        random.shuffle(baralho)



def main():
    baralho = Baralho()
    print(baralho.__str__())

if __name__ == "__main__":
    main()