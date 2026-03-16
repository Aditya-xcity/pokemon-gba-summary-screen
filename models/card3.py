# Question: Card3 class
# Name - ADITYA BHARDWAJ
# Section - D2
# Roll No - 08
# Course – B TECH
# Branch – CSE

from models.attack import Attack

class Card3:
    def __init__(self, a1: Attack, a2: Attack, a3: Attack, a4: Attack):
        self.attacks = [a1, a2, a3, a4]
