""" class Player:
    
    max_hp = 4000

player1 = Player()
print(player1.max_hp)

player2 = Player()
print(player2.max_hp)

Player.max_hp = 5000
print(player1.max_hp)
print(player2.max_hp) """

class Player:

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.score = 0

    testing = 13

player1 = Player("Aaron", 1200)
player2 = Player("Irene", 1300)

print(player1.name, " ", player1.hp, " ", player1.score, player1.testing)
print(player2.name, " ", player2.hp, " ", player2.score, player2.testing)

Player.testing = 15
player1.hp += 500
player1.score = 10

print(player1.name, " ", player1.hp, " ", player1.score, player1.testing)
print(player2.name, " ", player2.hp, " ", player2.score, player2.testing)

player1.testing = 20

print(player1.name, " ", player1.hp, " ", player1.score, player1.testing)
print(player2.name, " ", player2.hp, " ", player2.score, player2.testing)

