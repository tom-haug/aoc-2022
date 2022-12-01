from src.shared.controller import Controller
from src.days.day01.solver import Day01Solver


AnswerType = int


class Day01PartBSolver(Day01Solver):
    def solve(self) -> AnswerType:
        sorted_elf_calories = sorted(self.elf_calories, reverse=True)
        top_three = sorted_elf_calories[:3]
        return sum(top_three)


class Day01PartBController(Controller):
    def __init__(self):
        super().__init__(2022, 1, "b")

    def new_solver(self):
        return Day01PartBSolver()

    def sample_files(self) -> list[tuple[str, AnswerType]]:
        return [("src/days/day01/inputs/sample01.txt", 45000)]

    def file_path(self) -> str:
        return "src/days/day01/inputs/main.txt"


if __name__ == "__main__":
    controller = Day01PartBController()
    controller.run()
