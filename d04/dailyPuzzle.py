from dxx.superDailyPuzzle import SuperDailyPuzzle

def check_for_xmas(grid, y, x, dx, dy):
    m = len(grid) # y length
    n = len(grid[0]) # x length

    if (0<=y+3*dy<m) and (0<=(x+3*dx) < n):
        if (grid[y+dy][x+dx] == "M") and (grid[y+2*dy][x+2*dx] == "A") and (grid[y+3*dy][x+3*dx] == "S"): return 1
        else: return 0
    else: return 0

def check_for_mas(grid, y, x):
    m = len(grid) # y length
    n = len(grid[0]) # x length

    if (1<=y<m-1) and (1<=x<n-1):
        if (grid[y-1][x-1] == "M") and (grid[y+1][x+1] == "S") and (grid[y+1][x-1] == "M") and (grid[y-1][x+1] == "S"): return 1
        elif (grid[y-1][x-1] == "S") and (grid[y+1][x+1] == "M") and (grid[y+1][x-1] == "M") and (grid[y-1][x+1] == "S"): return 1
        elif (grid[y-1][x-1] == "M") and (grid[y+1][x+1] == "S") and (grid[y+1][x-1] == "S") and (grid[y-1][x+1] == "M"): return 1
        elif (grid[y-1][x-1] == "S") and (grid[y+1][x+1] == "M") and (grid[y+1][x-1] == "S") and (grid[y-1][x+1] == "M"): return 1
        else: return 0
    else: return 0 

# advent of code 2023 day 4 as template
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self, **kwargs):
        self.parsed = [[char for char in line] for line in self.data.splitlines()]

    def part_one(self, **kwargs):

        res1 = 0
        for y in range(0,len(self.parsed)):
            for x in range(0, len(self.parsed[0])):
                if self.parsed[y][x] == "X": 
                    res1 += check_for_xmas(self.parsed,y,x,0,1)
                    res1 += check_for_xmas(self.parsed,y,x,0,-1)
                    res1 += check_for_xmas(self.parsed,y,x,1,1)
                    res1 += check_for_xmas(self.parsed,y,x,-1,-1)
                    res1 += check_for_xmas(self.parsed,y,x,1,0)
                    res1 += check_for_xmas(self.parsed,y,x,-1,0)
                    res1 += check_for_xmas(self.parsed,y,x,1,-1)
                    res1 += check_for_xmas(self.parsed,y,x,-1,1)

        self.part_one_result = res1

    def part_two(self, **kwargs):

        res2 = 0
        for y in range(0,len(self.parsed)):
            for x in range(0, len(self.parsed[0])):
                if self.parsed[y][x] == "A": 
                    res2 += check_for_mas(self.parsed,y,x)
        self.part_two_result = res2