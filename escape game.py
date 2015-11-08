import os
import random
import logging

cells = [(0, 2), (1, 2), (2, 2),
         (0, 1), (1, 1), (2, 1),
         (0, 0), (1, 0), (2, 0)]

logging.basicConfig(filename='game.log', level=logging.DEBUG)


def get_location():
    player = random.choice(cells)
    door = random.choice(cells)
    monster = random.choice(cells)

    if player == door or player == monster or door == monster:
        return get_location()

    return player, door, monster


def get_moves(player):

    moves = ["UP", "DOWN", "LEFT", "RIGHT"]

    if player[0] == 0:
        moves.remove("LEFT")
    if player[0] == 2:
        moves.remove("RIGHT")
    if player[1] == 0:
        moves.remove("DOWN")
    if player[1] == 2:
        moves.remove("UP")
    return moves


def move_player(player, move):
    x, y = player

    if move == "UP":
        y += 1
    elif move == "DOWN":
        y -= 1
    elif move == "LEFT":
        x -= 1
    elif move == "RIGHT":
        x += 1
    return x, y


def draw_map(player):
    print " _  _  _"
    tile = "|{}"

    for index, cell in enumerate(cells):
        if index in [0, 1, 3, 4, 6, 7]:
            if cell == player:
                print tile.format("X"),
            else:
                print tile.format("_"),
        else:
            if cell == player:
                print tile.format("X|")
            else:
                print tile.format("_|")


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


player, door, monster = get_location()

logging.info('monster: {}; door: {}; player: {}'.format(
    monster, door, player))

print "Welcome to the game!"
print "Find door to escape. Be careful of the monster."

words = ["UP", "DOWN", "LEFT", "RIGHT"]

while True:
    moves = get_moves(player)

    print "You're now in room{}".format(player)
    print "Enter HINT to know where the monster is."
    print "Enter QUIT to quit"

    draw_map(player)

    print "You can move {}".format(moves)

    move = raw_input('> ')
    move = move.upper()

    if move == "QUIT":
        break

    if move == "HINT":
        clear()
        print "-----------------------------------------------"
        print "You hear a voice...'Monster is in {}.".format(monster)
        print "-----------------------------------------------"
        continue

    if move in moves:
        player = move_player(player, move)
    elif move in words:
        clear()
        print "-----------------------------------------------"
        print " ** Walls are hard, stop walking into them! **"
        print "-----------------------------------------------"
        continue
    else:
        clear()
        print "-----------------------------------------------"
        print "** You can only move! **"
        print "-----------------------------------------------"
        continue

    if player == door:
        print "*************"
        print "You escaped!"
        print "*************"
        break

    elif player == monster:
        print "xxxxxxxxxxxxxxxxxxxxxxxxxxx"
        print "You were eaten by the grue!"
        print "xxxxxxxxxxxxxxxxxxxxxxxxxxx"
        break

    clear()
