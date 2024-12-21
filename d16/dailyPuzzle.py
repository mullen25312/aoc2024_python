from dxx.superDailyPuzzle import SuperDailyPuzzle

from utils.dijkstra import AbstractDijkstraSPF

direction_dic = {0: (1,0), 1: (0,1), 2:(-1,0), 3:(0,-1)} # every direction clockwise order (E, S, W, N)

class DijkstraSPF(AbstractDijkstraSPF):

    @staticmethod
    def get_adjacent_nodes(G, u):
        grid = G
        (n, m) = (len(grid), len(grid[0]))
        (x,y, direction) = u

        adjacent = []

        # rotations
        adjacent.append((x,y, (direction+1) % 4)) # turn right
        adjacent.append((x,y, (direction+3) % 4)) # turn left

        # move forward
        x1, y1 = x + direction_dic[direction][0], y + direction_dic[direction][1]
        if grid[y1][x1] == 0: adjacent.append((x1, y1, direction))

        return adjacent

    @staticmethod
    def get_edge_weight(G, u, v):
        if u[2] == v[2]: return 1
        else: return 1000

# advent of code 2023 day 16
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

        self.parsed = start, end, grid
           
    def part_one(self, **kwargs): 
        start, end, grid = self.parsed

        dijkstra = DijkstraSPF(grid, (*start, 0))
        self.part_one_result = min([dijkstra.get_distance((*end, direction)) for direction in range(4)])

    def part_two(self, **kwargs):  
        start, end, grid = self.parsed

        dijkstra = DijkstraSPF(grid, (*start, 0))
        scores = [dijkstra.get_distance((*end, direction)) for direction in range(4)]
        direction = scores.index(min(scores))

        tmp = dijkstra.get_all_visited((*end, direction), set())
        tmp = set([(pos[0], pos[1]) for pos in tmp])
        
        self.part_two_result = len(tmp) + 1 
