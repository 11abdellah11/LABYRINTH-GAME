# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 17:38:36 2023

@author: elmen
"""

import os
from jeu import *


def display_map(map, joueurA, joueurB):
    draw = ''
    for x, row in enumerate(map.map):
        for y, item in enumerate(row):
            if x == joueurA.x and y == joueurA.y:
                item = "A"
            elif x == joueurB.x and y == joueurB.y:
                item = "B"
            else:
                item = item.replace('A', '█')
                item = item.replace('B', '█')
                item = item.replace('1', '█')
                item = item.replace('0', ' ')
            draw += item
        draw += '\n'

    os.system('cls' if os.name == 'nt' else 'clear')
    print(draw)


def main():
    map = Map('map.csv')
    joueurA = JoueurManuel(map, "A", "zxqd")
    joueurB = JoueurManuel(map, "B", "ybgj")

    display_map(map, joueurA, joueurB)

    while True:
        print('Solution non encore trouvée il faut avancer encore...')

        direction = input('Choisissez une direction Joueur1(q,z,d,x) Joueur2(g,y,j,b)')

        joueurA.move(direction)
        joueurB.move(direction)

        display_map(map, joueurA, joueurB)

        if joueurA.has_won():
            input('Joueur1 a gagné! Press enter to finish')
            break
        elif joueurB.has_won():
            input('Joueur2 a gagné! Press enter to finish')
            break


main()

























