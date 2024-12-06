from dxx.superDailyPuzzle import SuperDailyPuzzle
import copy

UP    = ( 0, -1)
DOWN  = ( 0,  1)
LEFT  = (-1,  0)
RIGHT = ( 1,  0)

TURN = { UP:RIGHT, RIGHT:DOWN, DOWN:LEFT, LEFT:UP }

class Guard:
    pos = [0,0]
    direction = UP

# advent of code 2023 day 6 as template
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self, **kwargs):
        tmp = [list(line) for line in self.data.splitlines()]
        
        dim = (len(tmp[0]), len(tmp))
        grid = {}

        guard = Guard()
        for x in range(dim[0]):
            for y in range(dim[1]):
                if tmp[y][x] == '#': grid[(x,y)] = 1
                elif tmp[y][x] == '^': guard.pos = [x, y]; guard.direction = UP
                elif tmp[y][x] == '>': guard.pos = [x, y]; guard.direction = RIGHT
                elif tmp[y][x] == 'v': guard.pos = [x, y]; guard.direction = DOWN
                elif tmp[y][x] == '<': guard.pos = [x, y]; guard.direction = LEFT

        self.parsed = [grid, guard, dim]

    def part_one(self, **kwargs):
        grid, guard, dim = self.parsed

        tmp_grid = grid.copy()
        tmp_guard = copy.deepcopy(guard)

        res_grid = {}
        while 0 <= tmp_guard.pos[0] < dim[0] and 0 <= tmp_guard.pos[1] < dim[1]:
            res_grid[tuple(tmp_guard.pos)] = 1

            # turning OR moving
            if (tmp_guard.pos[0] + tmp_guard.direction[0], tmp_guard.pos[1] + tmp_guard.direction[1]) in tmp_grid:
                tmp_guard.direction = TURN[tmp_guard.direction]
            else:
                tmp_guard.pos[0] += tmp_guard.direction[0]
                tmp_guard.pos[1] += tmp_guard.direction[1]

        self.temp = res_grid
        self.part_one_result = len(res_grid)

    def part_two(self, **kwargs):
        grid, guard, dim = self.parsed

        res2 = 0
        for (x,y) in set(self.temp.keys()).difference(tuple(guard.pos)): # iterate only over positions that are on the original path
            tmp_grid = grid.copy()
            tmp_grid[(x,y)] = 1
            tmp_guard = copy.deepcopy(guard)

            res_grid = {}
            while 0 <= tmp_guard.pos[0] < dim[0] and 0 <= tmp_guard.pos[1] < dim[1]:

                if tuple(tmp_guard.pos) in res_grid: 
                    if tmp_guard.direction in res_grid[tuple(tmp_guard.pos)]:
                        res2 += 1
                        break
                    else: res_grid[tuple(tmp_guard.pos)].add(tmp_guard.direction)
                else: res_grid[tuple(tmp_guard.pos)] = {tmp_guard.direction}

                # turning OR moving
                if (tmp_guard.pos[0] + tmp_guard.direction[0], tmp_guard.pos[1] + tmp_guard.direction[1]) in tmp_grid:
                    tmp_guard.direction = TURN[tmp_guard.direction]
                else:
                    tmp_guard.pos[0] += tmp_guard.direction[0]
                    tmp_guard.pos[1] += tmp_guard.direction[1]
                    
        self.part_two_result = res2