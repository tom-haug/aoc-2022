from __future__ import annotations
from src.shared.controller import Controller
from src.days.day09.solver import AnswerType, Day09Solver
from src.shared.file_result import FileResult


class Day09PartASolver(Day09Solver):
    @property
    def rope_length(self):
        return 2


class Day09PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(9, "a")

    def _new_solver(self):
        return Day09PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 13)]


if __name__ == "__main__":
    controller = Day09PartAController()
    controller.run()
