from Baralho import *
from Mao import *


saldo = 200
while(True):
    if saldo == 0:
        print("Seu saldo acabou, fim de jogo :(")
        break

    baralho = Baralho()
    mao = Mao(baralho)

    print("Saldo atual: " + str(saldo))

    aposta = input("Digite o valor da aposta, ou F para sair do jogo\n")
    if aposta == "F" or aposta == "f":
        print("Você finalizou o jogo com {:d} de saldo".format(saldo))
        break
    aposta = int(aposta)
    mao.setAposta(saldo, aposta)

    print(mao)
    print("  (1)        (2)        (3)        (4)        (5)")

    mao.trocarCartas(baralho)
    print(mao)
    print("  (1)        (2)        (3)        (4)        (5)")
    mao.trocarCartas(baralho)
    print(mao)
    print("  (1)        (2)        (3)        (4)        (5)")

    saldo = mao.add(saldo)