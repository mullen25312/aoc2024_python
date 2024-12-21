from dxx.superDailyPuzzle import SuperDailyPuzzle

import numpy as np

def find_block(disk, pos):
    tmp = disk[pos]
    while disk[pos] == tmp:
        pos -= 1
        if pos == 0: return 0
    return pos+1

def find_empty_block(disk, size, pos):
    for idx in range(pos-size-1):
        if (np.array(disk[idx:idx+size]) == None).all(): return idx
        else:
            if None not in disk[idx:idx+size]: idx += size 
            else: idx += disk[idx:idx+size].index(None)
    return False

# advent of code 2023 day 9
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self, **kwargs):
        self.parsed = [int(num) for num in list(self.data)]

    def part_one(self, **kwargs):
        disk_map = self.parsed

        # de-compress disk
        disk = []
        identifier = 0
        for idx, entry in enumerate(disk_map):
            if idx % 2 == 0:
                disk.extend([identifier]*entry)
                identifier += 1
            else: disk.extend([None]*entry)

        # compact disk
        pos = len(disk)-1
        for idx in range(len(disk)):
            if disk[idx] == None:
                while disk[pos] == None: pos -= 1
                if pos <= idx: break
                disk[idx], disk[pos] = disk[pos], disk[idx]

        self.part_one_result = sum([idx*entry if entry != None else 0 for idx, entry in enumerate(disk)])

    def part_two(self, **kwargs):
        disk_map = self.parsed

        # de-compress disk
        disk = []
        identifier = 0
        for idx, entry in enumerate(disk_map):
            if idx % 2 == 0:
                disk.extend([identifier]*entry)
                identifier += 1
            else: disk.extend([None]*entry)

        # compact disk
        idx = len(disk)-1
        while idx > 0:
            # find block
            tmp = find_block(disk, idx)

            # try to move block
            if disk[tmp] != None:
                size = idx+1-tmp
                tmp2 = find_empty_block(disk, size, idx)
                if tmp2 != False:
                    disk[tmp2:tmp2+size] = [disk[tmp]]*size
                    disk[tmp:tmp+size] = [None]*size
                    
            # continue with next block
            idx = tmp - 1

        self.part_two_result = sum([idx*entry if entry != None else 0 for idx, entry in enumerate(disk)])
