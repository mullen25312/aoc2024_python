from dxx.superDailyPuzzle import SuperDailyPuzzle

from utils.dijkstra import AbstractDijkstraSPF
import math

def display_grid(grid, n):
    output = ''
    for y in range(n):
        tmp = ''
        for x in range(n):
             if grid[y][x] == 1: tmp += '#' 
             else: tmp += '.' 
        tmp += '\n'
        output += tmp
    print(output)

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

# advent of code 2023 day 18
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self, **kwargs):
        self.parsed = [[int(line.split(',')[0]), int(line.split(',')[1])] for line in self.data.splitlines()]

    def part_one(self, **kwargs): 
        obstacles = self.parsed

        if len(obstacles) == 25: n = 7; l = 12
        else: n = 71; l = 1024

        # construct grid
        grid = [[0 for x in range(n)] for y in range(n)]
        for idx, obstacle in enumerate(obstacles):
            if idx == l: break
            grid[obstacle[1]][obstacle[0]] = 1

        self.part_one_result = DijkstraSPF(grid, (0,0)).get_distance((n-1, n-1))

    def part_two(self, **kwargs): 
        obstacles = self.parsed

        if len(obstacles) == 25: n = 7; l = 12 
        else: n = 71; l = 1024

        grid = [[0 for x in range(n)] for y in range(n)]
        dijkstra = DijkstraSPF(grid, (0,0))

        for idx in range(0, len(obstacles)):
            # update grid
            grid[obstacles[idx][1]][obstacles[idx][0]] = 1

            # search for new path only if new byte/block is on old path
            if tuple(obstacles[idx]) in dijkstra.get_path((n-1, n-1)): 
                dijkstra = DijkstraSPF(grid, (0,0))
                if dijkstra.get_distance((n-1, n-1)) == math.inf: break

        self.part_two_result = str(obstacles[idx][0]) + ',' + str(obstacles[idx][1])
