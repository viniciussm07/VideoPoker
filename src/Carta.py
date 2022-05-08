class Carta(object):
    
    def __init__(self, naipe, simbolo):
        self.naipe = naipe
        self.simbolo = simbolo

    def __str__(self):
        simbolo = self.getSimbolo()
        naipe = self.getNaipe()
        s = "+-----+\n|     |\n| " + simbolo

        if simbolo == "10":
            s += naipe + " |\n|     |\n+-----+\n"
        else: 
            s += " " + naipe + " |\n|     |\n+-----+\n"
        return s
    
    def getNaipe(self):
        return self.naipe

    def getSimbolo(self):
        return self.simbolo

