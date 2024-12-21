from dxx.superDailyPuzzle import SuperDailyPuzzle

from collections import defaultdict
import itertools

# advent of code 2023 day 8
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self, **kwargs):
        self.parsed = [list(line) for line in self.data.splitlines()]

    def part_one(self, **kwargs):
        grid = self.parsed

        frequencies = defaultdict(list)
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                if grid[y][x] != '.': frequencies[grid[y][x]].append((x,y))
        
        res_grid = defaultdict(int)
        for frequency in frequencies:
            for ant0, ant1 in itertools.product(frequencies[frequency], repeat=2):
                if ant0 == ant1: continue
                diff = (ant0[0]-ant1[0], ant0[1]-ant1[1])
                if 0 <= ant0[0]+diff[0] < len(grid[0]) and 0 <= ant0[1]+diff[1] < len(grid) and grid[ant0[1]+diff[1]][ant0[0]+diff[0]] != frequency:
                    res_grid[(ant0[0]+diff[0], ant0[1]+diff[1])] = 1
                if 0 <= ant0[0]-diff[0] < len(grid[0]) and 0 <= ant0[1]-diff[1] < len(grid) and grid[ant0[1]-diff[1]][ant0[0]-diff[0]] != frequency:
                    res_grid[(ant0[0]-diff[0], ant0[1]-diff[1])] = 1
                if 0 <= ant1[0]+diff[0] < len(grid[0]) and 0 <= ant1[1]+diff[1] < len(grid) and grid[ant1[1]+diff[1]][ant1[0]+diff[0]] != frequency:
                    res_grid[(ant1[0]+diff[0], ant1[1]+diff[1])] = 1
                if 0 <= ant1[0]-diff[0] < len(grid[0]) and 0 <= ant1[1]-diff[1] < len(grid) and grid[ant1[1]-diff[1]][ant1[0]-diff[0]] != frequency:
                    res_grid[(ant1[0]-diff[0], ant1[1]-diff[1])] = 1

        # res1 = 0
        # for antinode in res_grid:
        #     if 0 <= antinode[0] < len(grid[0]) and 0 <= antinode[1] < len(grid): res1 += 1

        # debug = ''
        # for y in range(len(grid)):
        #     for x in range(len(grid[0])):
        #         if grid[y][x] == '.' and res_grid[(x,y)] == 1: debug += '#'
        #         else: debug += grid[y][x]
        #     debug += '\n'
        # print(debug)

        self.part_one_result = len(res_grid)

    def part_two(self, **kwargs):        
        grid = self.parsed

        frequencies = defaultdict(list)
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                if grid[y][x] != '.': frequencies[grid[y][x]].append((x,y))

        res_grid = defaultdict(int)
        for frequency in frequencies:
            for ant0, ant1 in itertools.product(frequencies[frequency], repeat=2):
                if ant0 == ant1: continue
                for idx in range(1, len(grid[0])):
                    diff = (idx*(ant0[0]-ant1[0]), idx*(ant0[1]-ant1[1]))
                    if 0 <= ant0[0]+diff[0] < len(grid[0]) and 0 <= ant0[1]+diff[1] < len(grid):
                        res_grid[(ant0[0]+diff[0], ant0[1]+diff[1])] = 1
                    if 0 <= ant0[0]-diff[0] < len(grid[0]) and 0 <= ant0[1]-diff[1] < len(grid):
                        res_grid[(ant0[0]-diff[0], ant0[1]-diff[1])] = 1
                    if 0 <= ant1[0]+diff[0] < len(grid[0]) and 0 <= ant1[1]+diff[1] < len(grid):
                        res_grid[(ant1[0]+diff[0], ant1[1]+diff[1])] = 1
                    if 0 <= ant1[0]-diff[0] < len(grid[0]) and 0 <= ant1[1]-diff[1] < len(grid):
                        res_grid[(ant1[0]-diff[0], ant1[1]-diff[1])] = 1


        self.part_two_result = len(res_grid)