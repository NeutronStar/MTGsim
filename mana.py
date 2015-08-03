class Mana:
    WHITE = "White"
    BLUE = "Blue"
    BLACK = "Black"
    RED = "Red"
    GREEN = "Green"


class ManaCost:
    def __init__(self, white=0, blue=0, black=0, red=0, green=0, colorless=0):
        self.white = white
        self.blue = blue
        self.black = black
        self.red = red
        self.green = green
        self.colorless = colorless

    def cmc(self):
        return (self.white + self.blue + self.black + self.red + self.green 
                + self.colorless)

    def string(self):
        s = str(self.colorless)
        for i in range(self.white):
            s += "W"
        for i in range(self.blue):
            s += "U"
        for i in range(self.black):
            s += "B"
        for i in range(self.red):
            s += "R"
        for i in range(self.green):
            s += "G"
        return s
