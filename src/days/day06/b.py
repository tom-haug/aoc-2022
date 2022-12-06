from src.shared.controller import Controller
from src.days.day06.solver import AnswerType, Day06Solver
from src.shared.file_result import FileResult


class Day06PartBSolver(Day06Solver):
    @property
    def window_size(self) -> int:
        return 14


class Day06PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(6, "b")

    def _new_solver(self):
        return Day06PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [
            FileResult("sample01.txt", 19),
            FileResult("sample02.txt", 23),
            FileResult("sample03.txt", 23),
            FileResult("sample04.txt", 29),
            FileResult("sample05.txt", 26),
        ]


if __name__ == "__main__":
    controller = Day06PartBController()
    controller.run()
