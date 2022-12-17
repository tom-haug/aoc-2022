from typing import Any
from src.shared.controller import Controller
from src.days.day15.solver import (
    AnswerType,
    Day15Solver,
    Range,
)
from src.shared.file_result import FileResult


def calculate_tuning_frequency(y: int, range: Range) -> int:
    if range[0] >= 1:
        x = range[0] - 1
    else:
        x = range[1] + 1

    result = x * 4000000 + y
    return result


class Day15PartBSolver(Day15Solver):
    def solve(self) -> AnswerType:
        max_bounds = int(self.extra_params["max_bounds"])

        for y in range(0, max_bounds + 1):
            ranges = self._dead_zone_ranges(
                y, lambda x: (max(x[0], 0), min(x[1], max_bounds))
            )
            # more than one range here means there is a gap where
            # they were not able to be merged. This is where the
            # hidden distress beacon must be
            if len(ranges) > 1:
                return calculate_tuning_frequency(y, ranges[0])
        return -1


class Day15PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(15, "b")

    def _new_solver(self):
        return Day15PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 56000011, {"max_bounds": 20})]

    def _main_input_extra_params(self) -> dict[str, Any]:
        return {"max_bounds": 4000000, "result_override": 12543202766584}


if __name__ == "__main__":
    controller = Day15PartBController()
    controller.run()
