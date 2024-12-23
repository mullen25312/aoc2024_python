from dxx.superDailyPuzzle import SuperDailyPuzzle

import itertools
from collections import defaultdict

from utils.dijkstra import AbstractDijkstraSPF

neighbors = [(1,0), (0,1), (-1,0), (0,-1)]

class DijkstraSPF(AbstractDijkstraSPF):

    @staticmethod
    def get_adjacent_nodes(G, u):
        grid = G
        (n, m) = (len(grid), len(grid[0]))
        (x,y) = u

        adjacent = []
        for neighbor in neighbors:
            x1 = x+neighbor[0]; y1 = y+neighbor[1] 
            if 0 <= x1 < n and 0 <= y1 < m:
                if grid[y1][x1] == grid[y][x] + 1: adjacent.append((x1,y1))
        return adjacent

    @staticmethod
    def get_edge_weight(G, u, v):
        return 1

# advent of code 2023 day 10
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self, **kwargs):
        self.parsed = [[int(num) for num in line] for line in self.data.splitlines()]
           
    def part_one(self, **kwargs): 
        grid = self.parsed
        (n, m) = (len(grid), len(grid[0]))

        starts = set()
        ends = defaultdict(int)
        for (x,y) in itertools.product(range(n), range(m)):
            if grid[y][x] == 0: starts.add((x,y))
            if grid[y][x] == 9: ends[(x,y)] = 0

        for start in starts:
            dijkstra = DijkstraSPF(grid, (start))
            for end in ends.keys():
                if dijkstra.get_distance(end) == 9: ends[end] += 1

        self.part_one_result = sum(ends.values())

    def part_two(self, **kwargs): 
        grid = self.parsed
        (n, m) = (len(grid), len(grid[0]))

        starts = set()
        ends = defaultdict(int)
        for (x,y) in itertools.product(range(n), range(m)):
            if grid[y][x] == 0: starts.add((x,y))
            if grid[y][x] == 9: ends[(x,y)] = 0

        for start in starts:
            dijkstra = DijkstraSPF(grid, (start))
            for end in ends.keys():
                if dijkstra.get_distance(end) == 9: ends[end] += dijkstra.get_number_of_paths(end)
        
          
        self.part_two_result = sum(ends.values())
