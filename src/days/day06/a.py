from src.shared.controller import Controller
from src.days.day06.solver import AnswerType, Day06Solver
from src.shared.file_result import FileResult


class Day06PartASolver(Day06Solver):
    @property
    def window_size(self) -> int:
        return 4


class Day06PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(6, "a")

    def _new_solver(self):
        return Day06PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [
            FileResult("sample01.txt", 7),
            FileResult("sample02.txt", 5),
            FileResult("sample03.txt", 6),
            FileResult("sample04.txt", 10),
            FileResult("sample05.txt", 11),
        ]


if __name__ == "__main__":
    controller = Day06PartAController()
    controller.run()
