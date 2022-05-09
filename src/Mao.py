import Baralho as brl


class Mao(object):

    def __init__(self, baralho, n=5):
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
    def getMao(self, n=5):
        return self.mao

    def trocarCartas(self, baralho):
        troca = input(
            "Insira quais cartas deseja trocar separadas por espaço\n").split()

        for i in range(len(troca)):
            try:
                troca[i] = int(troca[i]) - 1
            except:
                print(
                    "Você não digitou um número ou digitou algum número maior que a quantidade de cartas em sua mão")
        for i in range(len(troca)):
            self.mao[troca[i]] = baralho.pegarCarta()

    def add(self):
        copiaMao = self.mao.copy()
        copiaMao = Mao.ordena(copiaMao)

        if Mao.royalStraightFlush(copiaMao):
            self.__saldo += self.aposta * 200
            print("Parabéns!!!!\nVocê acabou de fazer um Royal Straight Flush!\nSeu saldo atua é de {:d}".format(
                self.__saldo))
        elif Mao.straightFlush(copiaMao):
            self.__saldo += self.aposta * 100
            print("Parabéns!\nVocê acabou de fazer um Straight Flush!\nSeu saldo atua é de {:d}".format(
                self.__saldo))
        elif Mao.quadra(copiaMao):
            self.__saldo += self.aposta * 50
            print("Parabéns!\nVocê acabou de fazer um Uma Quadra!\nSeu saldo atua é de {:d}".format(
                self.__saldo))
        elif Mao.fullHand(copiaMao):
            self.__saldo += self.aposta * 20
            print("Parabéns!\nVocê acabou de fazer um Full Hand!\nSeu saldo atua é de {:d}".format(
                self.__saldo))
        elif Mao.flush(copiaMao):
            self.__saldo += self.aposta * 10
            print("Parabéns!\nVocê acabou de fazer um Flush!\nSeu saldo atua é de {:d}".format(
                self.__saldo))
        elif Mao.straight(copiaMao):
            self.__saldo += self.aposta * 5
            print("Você acabou de fazer um Straight!\nSeu saldo atua é de {:d}".format(
                self.__saldo))
        elif Mao.trinca(copiaMao):
            self.__saldo += self.aposta * 2
            print("Você acabou de fazer uma Trinca!\nSeu saldo atua é de {:d}".format(
                self.__saldo))
        elif Mao.doisPares(copiaMao):
            self.__saldo += self.aposta
            print("Você acabou de fazer um Par!\nSeu saldo atua é de {:d}".format(
                self.__saldo))
        else:
            self.__saldo -= self.aposta
            print("Infelizmente você não conseguiu fazer nenhuma combinação :( \nSeu saldo atual é de: {:d}".format(
                self.__saldo))
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
        if self.__saldo == 0:
            return True
        else:
            return False

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
        if (mao[0].getSimbolo() == 10) and (Mao.flush(mao)) and (Mao.straight(mao)):
            return True
        else:
            return False

    @staticmethod
    def straightFlush(mao):
        if Mao.flush(mao) and Mao.straight(mao):
            return True
        else:
            return False

    @staticmethod
    def quadra(mao):
        if mao[0].getSimbolo() == mao[1].getSimbolo() and mao[0].getSimbolo() == mao[2].getSimbolo() and mao[0].getSimbolo() == mao[3].getSimbolo():
            return True
        else:
            return False

    @staticmethod
    def fullHand(mao):
        if mao[0].getSimbolo() == mao[1].getSimbolo() and mao[2].getSimbolo() == mao[3].getSimbolo() and mao[2].getSimbolo() == mao[4].getSimbolo() or \
                mao[0].getSimbolo() == mao[1].getSimbolo() and mao[1].getSimbolo() == mao[2].getSimbolo() and mao[3].getSimbolo() == mao[4].getSimbolo():
            return True
        else:
            return False

    @staticmethod
    def flush(mao):
        if mao[0].getNaipe() == mao[1].getNaipe() and mao[1].getNaipe() == mao[2].getNaipe() and mao[2].getNaipe() == mao[3].getNaipe() and mao[3].getNaipe() == mao[4].getNaipe():
            return True
        return False

    @staticmethod
    def straight(mao):
        if (mao[0].getSimbolo() == (mao[1].getSimbolo() - 1)) and (mao[1].getSimbolo() == (mao[2].getSimbolo() - 1)) and (mao[2].getSimbolo() == (mao[3].getSimbolo() - 1)) and (mao[3].getSimbolo() == (mao[4].getSimbolo() - 1)):
            return True
        return False

    @staticmethod
    def trinca(mao):
        if (mao[0].getSimbolo() == mao[1].getSimbolo() and mao[1].getSimbolo() == mao[2].getSimbolo()) or (mao[4].getSimbolo() == mao[3].getSimbolo() and mao[3].getSimbolo() == mao[2].getSimbolo()):
            return True
        return False

    @staticmethod
    def doisPares(mao):
        if (mao[0].getSimbolo() == mao[1].getSimbolo()) or (mao[4].getSimbolo() == mao[3].getSimbolo()):
            return True
        return False


def main():
    baralho = brl.Baralho()
    mao = Mao(baralho)

    print(mao)

    mao.trocarCartas(baralho)
    print(mao)
    mao.trocarCartas(baralho)
    print(mao)

    mao.add()

    return


if __name__ == "__main__":
    main()
