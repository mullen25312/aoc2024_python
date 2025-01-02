from dxx.superDailyPuzzle import SuperDailyPuzzle

from utils.dijkstra import AbstractDijkstraSPF
from copy import deepcopy
from collections import defaultdict

def get_neighbors(center, n=1):
    ret = []
    for dx in range(-n, n + 1):
        ydiff = n - abs(dx)
        for dy in range(-ydiff, ydiff + 1):
            ret.append((center[0] + dx, center[1] + dy))
    return ret

class DijkstraSPF(AbstractDijkstraSPF):

    @staticmethod
    def get_adjacent_nodes(G, u):
        grid = G
        (n, m) = (len(grid), len(grid[0]))
        (x,y) = u

        adjacent = []

        if 0 <= x-1 < n and 0 <= y < m: 
            if grid[y][x-1] == 0: adjacent.append((x-1,y))
        if 0 <= x+1 < n and 0 <= y < m: 
            if grid[y][x+1] == 0: adjacent.append((x+1,y))
        if 0 <= x < n and 0 <= y-1 < m: 
            if grid[y-1][x] == 0:adjacent.append((x,y-1))
        if 0 <= x < n and 0 <= y+1 < m: 
            if grid[y+1][x] == 0: adjacent.append((x,y+1))
        
        return adjacent

    @staticmethod
    def get_edge_weight(G, u, v):
        return 1

# advent of code 2023 day 20
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self, **kwargs):
        n, m = len(self.data.splitlines()[0]), len(self.data.splitlines())

        grid = [[0 for _ in range(n)] for _ in range(m)]
        start, end = (0,0), (0,0)
        for y, line in enumerate(self.data.splitlines()):
            for x, pos in enumerate(line): 
                if pos == "#": grid[y][x] = 1
                elif pos == "S": start = (x,y)
                elif pos == "E": end = (x,y)

        self.parsed = grid, start, end
           
    def part_one(self, **kwargs):
        grid, start, end = self.parsed
        n, m = len(grid[0]), len(grid)
        threshold = 2 if n == 15 else 100

        path = DijkstraSPF(grid, start).get_path(end)
        path_dict = {pos:idx for idx, pos in enumerate(path)}
        neighbors =  [(2,0), (-2,0), (0,2), (0,-2)]

        res1 = 0
        for idx, pos in enumerate(path):
            for cheat in neighbors:
                tmpx = pos[0] + cheat[0]; tmpy = pos[1] + cheat[1]
                if 0 <= tmpx< n and 0 <= tmpy < m:
                    if (tmpx, tmpy) in path_dict.keys():
                        if path_dict[(tmpx, tmpy)] - idx - 2 >= threshold: res1+= 1

        self.part_one_result = res1

    def part_two(self, **kwargs): 
        grid, start, end = self.parsed
        n, m = len(grid[0]), len(grid)
        threshold = 50 if n == 15 else 100

        path = DijkstraSPF(grid, start).get_path(end)
        path_dict = {pos:idx for idx,pos in enumerate(path)}
        neighbors = get_neighbors((0,0), 20)
        
        res2 = 0
        test = defaultdict(int)
        for idx, pos in enumerate(path):
            for cheat in neighbors:
                tmpx = pos[0] + cheat[0]; tmpy = pos[1] + cheat[1]
                if 0 <= tmpx < n and 0 <= tmpy < m:
                    if (tmpx, tmpy) in path_dict.keys():
                        if path_dict[(tmpx, tmpy)] - idx - abs(cheat[0]) - abs(cheat[1]) >= threshold: res2+= 1

        self.part_two_result = res2
