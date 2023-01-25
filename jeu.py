# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 17:04:55 2023

@author: elmen
"""


import csv


class Map:
    def __init__(self, map_file):
        self.load_map(map_file)

    def load_map(self, map_file):
        self.map = []
        with open(map_file, newline="", encoding="utf-8-sig") as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            for row in reader:
                self.map.append(row)

    def get_map(self):
        return self.map


class JoueurManuel:
    def __init__(self, map, name, keys):
        self.map = map.get_map()
        self.x, self.y = [(i, sublist.index(name)) for i, sublist in enumerate(self.map) if name in sublist][0]
        self.key_up = keys[0]
        self.key_down = keys[1]
        self.key_left = keys[2]
        self.key_right = keys[3]

    def move(self, direction):
        if direction == self.key_up:
            if self.map[self.x-1][self.y] == '1':
                return False
            else:
                self.x = self.x - 1
                return True
        elif direction == self.key_down:
            if self.map[self.x+1][self.y] == '1':
                return False
            else:
                self.x = self.x + 1
                return True
        elif direction == self.key_left:
            if self.map[self.x][self.y-1] == '1':
                return False
            else:
                self.y = self.y - 1
                return True
        elif direction == self.key_right:
            if self.map[self.x][self.y+1] == '1':
                return False
            else:
                self.y = self.y + 1
                return True

    def has_won(self):
        return self.map[self.x][self.y] == 'S'
