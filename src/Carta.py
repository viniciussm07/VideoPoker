class Carta(object):
    
    def __init__(self, naipe, simbolo):
        self.naipe = naipe
        self.simbolo = simbolo

    def __str__(self):
        simbolo = self.getSimbolo()
        if simbolo == 14:
            simbolo = "A"
        elif simbolo == 13:
            simbolo = "K"
        elif simbolo == 12:
            simbolo = "Q"
        elif simbolo == 11:
            simbolo = "J"
        
        naipe = self.getNaipe()
        s = "+-----+\n|     |\n| " + str(simbolo)

        if simbolo == 10 :
            s += naipe + " |\n|     |\n+-----+\n"
        else: 
            s += " " + naipe + " |\n|     |\n+-----+\n"
        return s
    
    def getNaipe(self):
        return self.naipe

    def getSimbolo(self):
        return self.simbolo

