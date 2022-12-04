from src.shared.controller import Controller
from src.days.day01.solver import AnswerType, Day01Solver
from src.shared.file_result import FileResult


class Day01PartBSolver(Day01Solver):
    def solve(self) -> AnswerType:
        sorted_elf_calories = sorted(self.elf_calories, reverse=True)
        top_three = sorted_elf_calories[:3]
        return sum(top_three)


class Day01PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(2022, 1, "b")

    def _new_solver(self):
        return Day01PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 45000)]


if __name__ == "__main__":
    controller = Day01PartBController()
    controller.run()
