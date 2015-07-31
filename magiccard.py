from card import Card

class MagicCard(Card):

    def __init__(self, name, type, subtype=None):
        self.name = name
        self.type = type
        self.subtype = subtype

    def info(self):
        print("Name:", self.name) 
        print("Type:", self.type)
        print("Subtype:", self.subtype)
