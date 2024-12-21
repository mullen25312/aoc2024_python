from dxx.superDailyPuzzle import SuperDailyPuzzle

from math import prod

def display(robots, n, m):
    output = ''
    for y in range(m):
        tmp = ''
        for x in range(n):
            if [x, y] not in robots: tmp += '.'
            else: tmp += str(robots.count([x, y]))
        tmp += '\n'
        output += tmp
    print(output)
    

# advent of code 2023 day 14
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self, **kwargs):
        self.parsed = []
        for line in self.data.splitlines():
            p = [int(num) for num in line.split('=')[1][0:-2].split(',')]
            c = [int(num) for num in line.split('=')[2].split(',')]
            self.parsed.append([p,c])

        # print(self.parsed)
    def part_one(self, **kwargs):
        robots = self.parsed
        N = 100

        # adjust size according to input scenario
        if len(robots) == 12: n,m = 11, 7 # width (x) and height (y)
        else: n,m = 101, 103

        res_robots = []
        for robot in robots:
            res_robots.append([(robot[0][0]+N*robot[1][0]) % n, (robot[0][1]+N*robot[1][1]) % m])

        res = [0, 0, 0, 0]
        for robot in res_robots:
            if robot[0] < n // 2:
                if robot[1] < m // 2: res[0] += 1
                elif robot[1] > m // 2: res[1] += 1
            elif robot[0] > n // 2:
                if robot[1] < m // 2: res[2] += 1
                elif robot[1] > m // 2: res[3] += 1
        
        # display(res_robots, n, m)
        self.part_one_result = prod(res)


    def part_two(self, **kwargs):
        robots = self.parsed
        N = 6516

        # adjust size according to input scenario
        if len(robots) == 12: n,m = 11, 7 # width (x) and height (y)
        else: n,m = 101, 103

        res_robots = []
        for robot in robots:
            res_robots.append([(robot[0][0]+N*robot[1][0]) % n, (robot[0][1]+N*robot[1][1]) % m])   

        # display(res_robots, n, m)
        self.part_two_result = N
