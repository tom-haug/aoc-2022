from math import prod
from typing import Any
from src.days.day19.models import Blueprint
from src.shared.controller import Controller, ExtraParams
from src.days.day19.solver import (
    AnswerType,
    Day19Solver,
)
from src.shared.file_result import FileResult


class Day19PartBSolver(Day19Solver):
    @property
    def _desired_blueprints(self) -> list[Blueprint]:
        return self.all_blueprints[:3]

    @property
    def _num_turns(self) -> int:
        return 32

    @property
    def _resource_buffer(self) -> float:
        return 1.5

    def _calc_answer(self, results: list[tuple[Blueprint, int]]) -> int:
        return prod(result[1] for result in results)


class Day19PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(19, "b")

    def _new_solver(self):
        return Day19PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 3472, {ExtraParams.LongRunning: True})]

    def _main_input_extra_params(self) -> dict[str, Any]:
        return {ExtraParams.LongRunning: True}


if __name__ == "__main__":
    controller = Day19PartBController()
    controller.run()
