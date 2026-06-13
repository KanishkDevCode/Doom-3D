import pygame as pg

class Map:
    def __init__(self, game, filepath='resources/maps/level1.txt'):
        self.game = game    
        self.mini_map = []
        self.world_map = {}
        self.load_map_from_file(filepath)
        self.rows = len(self.mini_map)
        self.cols = len(self.mini_map[0]) if self.rows > 0 else 0
        self.get_map()

    def load_map_from_file(self, filepath):
        try:
            with open(filepath, 'r') as f:
                for line in f:
                    row = []
                    for char in line.strip().split():
                        if char == '.':
                            row.append(False)
                        else:
                            row.append(int(char))
                    self.mini_map.append(row)
        except FileNotFoundError:
            print(f"Error: Map file '{filepath}' not found.")
            self.mini_map = [[1,1,1],[1,False,1],[1,1,1]]

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgrey', (pos[0] * 100, pos[1] * 100, 100, 100), 2)
         for pos in self.world_map]