from src.shared.controller import Controller
from src.days.day01.solver import Day01Solver


AnswerType = int


class Day01PartASolver(Day01Solver):
    def solve(self) -> AnswerType:
        return max(self.elf_calories)


class Day01PartAController(Controller):
    def __init__(self):
        super().__init__(2022, 1, "a")

    def new_solver(self):
        return Day01PartASolver()

    def sample_files(self) -> list[tuple[str, AnswerType]]:
        return [("src/days/day01/inputs/sample01.txt", 24000)]

    def file_path(self) -> str:
        return "src/days/day01/inputs/main.txt"


if __name__ == "__main__":
    controller = Day01PartAController()
    controller.run()
