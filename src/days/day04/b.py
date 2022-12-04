from src.shared.controller import Controller
from src.days.day04.solver import AnswerType, BoundsPair, Day04Solver
from src.shared.file_result import FileResult


class Day04PartBSolver(Day04Solver):
    def _compare(self, pair: BoundsPair) -> bool:
        return max(pair[0][0], pair[1][0]) <= min(pair[0][1], pair[1][1])


class Day04PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(2022, 4, "b")

    def _new_solver(self):
        return Day04PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 4)]


if __name__ == "__main__":
    controller = Day04PartBController()
    controller.run()
