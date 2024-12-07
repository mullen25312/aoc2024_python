from dxx.superDailyPuzzle import SuperDailyPuzzle

from collections import defaultdict
import copy

UP    = ( 0, -1)
DOWN  = ( 0,  1)
LEFT  = (-1,  0)
RIGHT = ( 1,  0)

TURN = { UP:RIGHT, RIGHT:DOWN, DOWN:LEFT, LEFT:UP }
TURN2BIN = { UP: 1, DOWN: 2, LEFT: 4, RIGHT: 8 }

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
        grid = [[0] * dim[0] for _ in range(dim[1])]

        guard = Guard()
        for x in range(dim[0]):
            for y in range(dim[1]):
                # if tmp[y][x] == '#': grid[(x,y)] = 1
                if tmp[y][x] == '#': grid[y][x] = 1
                elif tmp[y][x] == '^': guard.pos = [x, y]; guard.direction = UP
                elif tmp[y][x] == '>': guard.pos = [x, y]; guard.direction = RIGHT
                elif tmp[y][x] == 'v': guard.pos = [x, y]; guard.direction = DOWN
                elif tmp[y][x] == '<': guard.pos = [x, y]; guard.direction = LEFT

        self.parsed = [grid, guard, dim]

    def part_one(self, **kwargs):
        grid, guard, dim = self.parsed
        tmp_guard = copy.deepcopy(guard)

        res_grid = {}
        while True:
            res_grid[tuple(tmp_guard.pos)] = 1

            # turning OR 
            tmp0 = tmp_guard.pos[0] + tmp_guard.direction[0]
            tmp1 = tmp_guard.pos[1] + tmp_guard.direction[1]
            # if (tmp_guard.pos[0] + tmp_guard.direction[0], tmp_guard.pos[1] + tmp_guard.direction[1]) in tmp_grid:
            if 0 <= tmp0 < dim[0] and 0 <= tmp1 < dim[1]:
                if grid[tmp1][tmp0] == 1:
                    tmp_guard.direction = TURN[tmp_guard.direction]
                else:
                    tmp_guard.pos[0] += tmp_guard.direction[0]
                    tmp_guard.pos[1] += tmp_guard.direction[1]
            else: break

        self.temp = res_grid
        self.part_one_result = len(res_grid)

    def part_two(self, **kwargs):
        grid, guard, dim = self.parsed

        res2 = 0
        # res_grid = defaultdict(int)
        
        for (x,y) in set(self.temp.keys()).difference(tuple(guard.pos)): # iterate only over positions that are on the original path

            pos = [guard.pos[0], guard.pos[1]]
            direction = guard.direction
            # res_grid.clear()

            cnt = 0
            res_grid = [[0] * dim[0] for _ in range(dim[1])]
            while cnt < 10000:
                cnt += 1

                # res_grid[tuple(pos)] = res_grid[tuple(pos)] | TURN2BIN[direction]
                res_grid[pos[1]][pos[0]] = res_grid[pos[1]][pos[0]] | TURN2BIN[direction]

                # turning OR moving
                tmp0 = pos[0] + direction[0]
                tmp1 = pos[1] + direction[1]
                
                if 0 <= tmp0 < dim[0] and 0 <= tmp1 < dim[1]:
                    if (tmp0, tmp1) == (x,y) or grid[tmp1][tmp0] == 1:
                        direction = TURN[direction]
                        if res_grid[pos[1]][pos[0]] & TURN2BIN[direction] != 0: res2 += 1; break
                    else:
                        pos[0] = tmp0
                        pos[1] = tmp1
                else: break
                    
        self.part_two_result = res2