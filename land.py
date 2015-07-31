from magiccard import MagicCard
from mana import Mana


class Land(MagicCard):

    def __init__(self, name, type, subtype=None):
        super().__init__(name, type, subtype)

    def tap():
        return None


class BasicLandType:
    PLAIN = "Plains"
    ISLAND = "Island"
    SWAMP = "Swamp"
    MOUNTAIN = "Mountain"
    FOREST = "Forest"


class BasicLand(Land):

    def __init__(self, subtype): 
        super().__init__(subtype, "Basic Land", subtype=subtype)

    def tap(self):
        if self.subtype == BasicLandType.PLAIN:
            return Mana.WHITE
        elif self.subtype == BasicLandType.ISLAND:
            return Mana.BLUE
        elif self.subtype == BasicLandType.SWAMP:
            return Mana.BLACK
        elif self.subtype == BasicLandType.MOUNTAIN:
            return Mana.RED
        elif self.subtype == BasicLandType.FOREST:
            return Mana.GREEN
        else:
            raise Exception("Unknown Basic Land type.")


class NonbasicLand(Land):
    pass
