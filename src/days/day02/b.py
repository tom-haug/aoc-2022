from src.shared.controller import Controller
from src.days.day02.solver import AnswerType, Day02Solver, Shape, RoundResult
from src.shared.file_result import FileResult


class Day02PartBSolver(Day02Solver):
    def _get_my_shape(self, their_shape: Shape, second_value: str) -> Shape:
        result = RoundResult.parse(second_value)
        return Shape((int(their_shape) + int(result)) % 3)


class Day02PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(2022, 2, "b")

    def _new_solver(self):
        return Day02PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 12)]


if __name__ == "__main__":
    controller = Day02PartBController()
    controller.run()
