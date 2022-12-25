from typing import Any
from src.days.day19.models import Blueprint
from src.shared.controller import Controller
from src.days.day19.solver import (
    AnswerType,
    Day19Solver,
)
from src.shared.file_result import FileResult


class Day19PartASolver(Day19Solver):
    @property
    def _desired_blueprints(self) -> list[Blueprint]:
        return self.all_blueprints

    @property
    def _num_turns(self) -> int:
        return 24

    @property
    def _resource_buffer(self) -> float:
        return 1.1

    def _calc_answer(self, results: list[tuple[Blueprint, int]]) -> int:
        return sum([result[0].id * result[1] for result in results])


class Day19PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(19, "a")

    def _new_solver(self):
        return Day19PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 33, {"result_override": 33})]

    def _main_input_extra_params(self) -> dict[str, Any]:
        return {"result_override": 1389}


if __name__ == "__main__":
    controller = Day19PartAController()
    controller.run()
