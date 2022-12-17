from typing import Any
from src.shared.controller import Controller
from src.days.day15.solver import (
    AnswerType,
    Day15Solver,
    Range,
)
from src.shared.file_result import FileResult


def in_ranges(val: int, ranges: list[Range]) -> int:
    for range in ranges:
        if range[0] <= val <= range[1]:
            return True
    return False


class Day15PartASolver(Day15Solver):
    def solve(self) -> AnswerType:
        target_y = int(self.extra_params["target_y"])
        ranges = self._dead_zone_ranges(target_y)
        objects = {
            object
            for sensor in self.sensors
            for object in [sensor.location, sensor.beacon]
            if object[1] == target_y and in_ranges(object[0], ranges)
        }
        dead_zone_count = sum(x[1] - x[0] + 1 for x in ranges) - len(objects)
        return dead_zone_count


class Day15PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(15, "a")

    def _new_solver(self):
        return Day15PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 26, {"target_y": 10})]

    def _main_input_extra_params(self) -> dict[str, Any]:
        return {"target_y": 2000000}


if __name__ == "__main__":
    controller = Day15PartAController()
    controller.run()
