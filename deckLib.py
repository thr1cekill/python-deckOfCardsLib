import random

class Card:
    def __init__(self, suitInt, value):
        self.suitInt = suitInt
        self.value = value
        if(self.value > 1 and self.value < 11):
            self.type = str(self.value)
        if(self.value == 1):
            self.type = "Ace"
        if(self.value == 11):
            self.type = "Jack"
        if(self.value == 12):
            self.type = "Queen"
        if(self.value == 13):
            self.type = "King"
        if(self.value == 14):
            self.type = "Joker"
            
        if(self.suitInt == 0):
            self.suitStr = "Clubs"
            self.colour = "Black"
        if(self.suitInt == 1):
            self.suitStr = "Diamonds"
            self.colour = "Red"
        if(self.suitInt == 2):
            self.suitStr = "Spades"
            self.colour = "Black"
        if(self.suitInt == 3):
            self.suitStr = "Hearts"
            self.colour = "Red"
        if(self.suitInt == 4):
            self.suitStr = "Black"
            self.colour = "Black"
        if(self.suitInt == 5):
            self.suitStr = "Red"
            self.colour = "Red"

        if(self.value == 14):
            self.name = self.suitStr + " " + self.type
        else:
            self.name = self.type + " of " + self.suitStr

class Deck:
    def __init__(self, deck):
        self.deck = deck
        self.size = len(deck)

    def Shuffle(self):
        random.shuffle(self.deck)

    def Draw(self):
        topCard = self.deck[0]
        del self.deck[0]
        return topCard
    
    def ListDeck(self):
        for x in range(0, self.size):
            print(self.deck[x].name)

#Clubs = suit 0#
#Diamonds = suit 1#
#Spades = suit 2#
#Hearts = suit 3#

#red suits = odd#
#black suits = even#

clbAce = Card(0,1)
diaAce = Card(1,1)
spdAce = Card(2,1)
hrtAce = Card(3,1)
clb2 = Card(0,2)
dia2 = Card(1,2)
spd2 = Card(2,2)
hrt2 = Card(3,2)
clb3 = Card(0,3)
dia3 = Card(1,3)
spd3 = Card(2,3)
hrt3 = Card(3,3)
clb4 = Card(0,4)
dia4 = Card(1,4)
spd4 = Card(2,4)
hrt4 = Card(3,4)
clb5 = Card(0,5)
dia5 = Card(1,5)
spd5 = Card(2,5)
hrt5 = Card(3,5)
clb6 = Card(0,6)
dia6 = Card(1,6)
spd6 = Card(2,6)
hrt6 = Card(3,6)
clb7 = Card(0,7)
dia7 = Card(1,7)
spd7 = Card(2,7)
hrt7 = Card(3,7)
clb8 = Card(0,8)
dia8 = Card(1,8)
spd8 = Card(2,8)
hrt8 = Card(3,8)
clb9 = Card(0,9)
dia9 = Card(1,9)
spd9 = Card(2,9)
hrt9 = Card(3,9)
clb10 = Card(0,10)
dia10 = Card(1,10)
spd10 = Card(2,10)
hrt10 = Card(3,10)
clbJck = Card(0,11)
diaJck = Card(1,11)
spdJck = Card(2,11)
hrtJck = Card(3,11)
clbQue = Card(0,12)
diaQue = Card(1,12)
spdQue = Card(2,12)
hrtQue = Card(3,12)
clbKng = Card(0,13)
diaKng = Card(1,13)
spdKng = Card(2,13)
hrtKng = Card(3,13)
blkJok = Card(4,14)
redJok = Card(5,14)

deckOfCards = [clbAce, diaAce, spdAce, hrtAce,
               clb2, dia2, spd2, hrt2,
               clb3, dia3, spd3, hrt3,
               clb4, dia4, spd4, hrt4,
               clb5, dia5, spd5, hrt5,
               clb6, dia6, spd6, hrt6,
               clb7, dia7, spd7, hrt7,
               clb8, dia8, spd8, hrt8,
               clb9, dia9, spd9, hrt9,
               clb10, dia10, spd10, hrt10,
               clbJck, diaJck, spdJck, hrtJck,
               clbQue, diaQue, spdQue, hrtQue,
               clbKng, diaKng, spdKng, hrtKng]

deckOfCardsWithJokers = [clbAce, diaAce, spdAce, hrtAce,
                         clb2, dia2, spd2, hrt2,
                         clb3, dia3, spd3, hrt3,
                         clb4, dia4, spd4, hrt4,
                         clb5, dia5, spd5, hrt5,
                         clb6, dia6, spd6, hrt6,
                         clb7, dia7, spd7, hrt7,
                         clb8, dia8, spd8, hrt8,
                         clb9, dia9, spd9, hrt9,
                         clb10, dia10, spd10, hrt10,
                         clbJck, diaJck, spdJck, hrtJck,
                         clbQue, diaQue, spdQue, hrtQue,
                         clbKng, diaKng, spdKng, hrtKng,
                         blkJok, redJok]

print("go")
myDeck = Deck(deckOfCards)
