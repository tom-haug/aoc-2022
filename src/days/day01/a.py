from src.shared.controller import Controller
from src.days.day01.solver import AnswerType, Day01Solver
from src.shared.file_result import FileResult


class Day01PartASolver(Day01Solver):
    def solve(self) -> AnswerType:
        return max(self.elf_calories)


class Day01PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(2022, 1, "a")

    def _new_solver(self):
        return Day01PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    @property
    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 24000)]


if __name__ == "__main__":
    controller = Day01PartAController()
    controller.run()
