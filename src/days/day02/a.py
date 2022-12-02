from src.shared.controller import Controller
from src.days.day02.solver import AnswerType, Day02Solver, Shape


class Day02PartASolver(Day02Solver):
    def get_my_shape(self, their_shape: Shape, second_value: str) -> Shape:
        return Shape.from_str(second_value)


class Day02PartAController(Controller):
    def __init__(self):
        super().__init__(2022, 2, "a")

    def new_solver(self):
        return Day02PartASolver()

    def sample_files(self) -> list[tuple[str, AnswerType]]:
        return [("src/days/day02/inputs/sample01.txt", 15)]

    def file_path(self) -> str:
        return "src/days/day02/inputs/main.txt"


if __name__ == "__main__":
    controller = Day02PartAController()
    controller.run()
