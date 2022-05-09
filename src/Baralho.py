import Carta as crt
import random

class Baralho(object):
    def __init__(self):
        self.__naipes = ["♥", "♠", "♦", "♣"]
        self.__simbolos = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.baralho = []

        for i in range(len(self.__naipes)):
            for j in range(len(self.__simbolos)):
                self.baralho.append((crt.Carta(self.__naipes[i], self.__simbolos[j])))
        Baralho.embaralha(self.baralho)

    def __str__(self):
        baralho = self.baralho
        s = ""
        for i in range(52):
            base = i * 8
            if i%5 == 0:
                print("\n")
            for c in baralho:
                p = str(c)
                s += p[base:base+7]
                s += "    "
            s += "\n"
        return s

    # TODO trocar cartas

    def getBaralho(self):
        return self.baralho

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
    return 0

if __name__ == "__main__":
    main()