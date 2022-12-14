from typing import Optional
from src.shared.controller import Controller
from src.days.day14.solver import AnswerType, Day14Solver
from src.shared.file_result import FileResult


class Day14PartASolver(Day14Solver):
    @property
    def floor_y(self) -> Optional[int]:
        return None


class Day14PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(14, "a")

    def _new_solver(self):
        return Day14PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 24)]


if __name__ == "__main__":
    controller = Day14PartAController()
    controller.run()
