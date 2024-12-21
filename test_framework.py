import pytest
import yaml
import importlib
import os

from itertools import product

# tests to run
days_to_be_tested = ["d00", "d01", "d02", "d03", "d04", "d05", "d06", "d07", "d08"]

scenarios = ["demo", "input"]
ids = tuple(f"{id[1]} -> {id[0]}" for id in product(days_to_be_tested, scenarios))


class TestConfig:
    __test__ = False

    def __init__(self, config):
        if config == None:
            config = {}

        self.parse_args = config.get("parse_args") or {}
        self.part_one_args = config.get("part_one_args") or {}
        self.part_two_args = config.get("part_two_args") or {}

        self.parse_result = config.get("parse_result") or ""
        self.part_one_result = config.get("part_one_result") or ""
        self.part_two_result = config.get("part_two_result") or ""


@pytest.fixture(scope="class", params=product(days_to_be_tested, scenarios), ids=ids)
def prepare_test(request):
    with open(os.path.join(request.param[0], f"test_{request.param[1]}.yaml"), "r") as file:
        request.cls.test_config = TestConfig(yaml.load(file, Loader=yaml.FullLoader))

    importedModule = importlib.import_module(f"{request.param[0]}.dailyPuzzle")
    request.cls.puzzle = importedModule.DailyPuzzle(os.path.join(request.param[0], f"{request.param[1]}.txt"))


@pytest.mark.usefixtures("prepare_test")
class Tests_dxx:
    # def test_parse(self):
    #     self.puzzle.parse()
    #     if self.test_config.parse_result == "":
    #         pytest.skip("expected input not provided")
    #     else:
    #         assert self.puzzle.parsed == self.test_config.parse_result

    def test_part_one(self):
        if self.test_config.part_one_result == "":
            pytest.skip("expected result not provided")
        else:
            self.puzzle.parse()
            self.puzzle.part_one()
            assert self.puzzle.part_one_result == self.test_config.part_one_result

    def test_part_two(self):
        if self.test_config.part_two_result == "":
            pytest.skip("expected result not provided")
        else:
            self.puzzle.parse()
            self.puzzle.part_two()
            assert self.puzzle.part_two_result == self.test_config.part_two_result
