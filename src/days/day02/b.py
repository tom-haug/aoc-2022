from src.shared.controller import Controller
from src.days.day02.solver import AnswerType, Day02Solver, Shape, RoundResult


class Day02PartBSolver(Day02Solver):
    my_shape_mapper: dict[tuple[Shape, RoundResult], Shape] = {
        (Shape.ROCK, RoundResult.WIN): Shape.PAPER,
        (Shape.ROCK, RoundResult.LOSE): Shape.SCISSOR,
        (Shape.ROCK, RoundResult.DRAW): Shape.ROCK,
        (Shape.PAPER, RoundResult.WIN): Shape.SCISSOR,
        (Shape.PAPER, RoundResult.LOSE): Shape.ROCK,
        (Shape.PAPER, RoundResult.DRAW): Shape.PAPER,
        (Shape.SCISSOR, RoundResult.WIN): Shape.ROCK,
        (Shape.SCISSOR, RoundResult.LOSE): Shape.PAPER,
        (Shape.SCISSOR, RoundResult.DRAW): Shape.SCISSOR,
    }

    def get_my_shape(self, their_shape: Shape, second_value: str) -> Shape:
        return self.my_shape_mapper[(their_shape, RoundResult.from_str(second_value))]


class Day02PartBController(Controller):
    def __init__(self):
        super().__init__(2022, 2, "b")

    def new_solver(self):
        return Day02PartBSolver()

    def sample_files(self) -> list[tuple[str, AnswerType]]:
        return [("src/days/day02/inputs/sample01.txt", 12)]

    def file_path(self) -> str:
        return "src/days/day02/inputs/main.txt"


if __name__ == "__main__":
    controller = Day02PartBController()
    controller.run()
