# advent of code website: https://adventofcode.com/2024
# github: https://github.com/mullen25312/aoc2024_python

import os
import importlib

dailyPuzzles = ["d00", "d01", "d02", "d03", "d04", "d05", "d06", "d07", "d08", "d09", "d10", "d11", "d13", "d14", "d16", "d18", "d19", "d20", "d22", "d23", "d25"]
# dailyPuzzles = ["d23"]

if __name__ == "__main__":

    for module in dailyPuzzles:
        # import daily module
        importedModule = importlib.import_module(f"{module}.dailyPuzzle")
        # puzzle = importedModule.DailyPuzzle(os.path.join(module, "demo.txt"))
        puzzle = importedModule.DailyPuzzle(os.path.join(module, "input.txt"))

        # solve puzzle
        puzzle.parse()
        puzzle.part_one()
        puzzle.part_two()

        # print results
        print(f"####### {module} - results #######")
        print(f"Result of part one: " + str(puzzle.part_one_result))
        print(f"Result of part two: " + str(puzzle.part_two_result))
        print()
