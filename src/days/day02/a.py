from src.shared.controller import Controller
from src.days.day02.solver import AnswerType, Day02Solver, Shape
from src.shared.file_result import FileResult


class Day02PartASolver(Day02Solver):
    def _get_my_shape(self, their_shape: Shape, second_value: str) -> Shape:
        return Shape.parse(second_value)


class Day02PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(2022, 2, "a")

    def _new_solver(self):
        return Day02PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 15)]


if __name__ == "__main__":
    controller = Day02PartAController()
    controller.run()
