from src.shared.controller import Controller
from src.days.day04.solver import AnswerType, Bounds, BoundsPair, Day04Solver
from src.shared.file_result import FileResult


class Day04PartASolver(Day04Solver):
    def _compare(self, pair: BoundsPair) -> bool:
        return fully_contained(pair[0], pair[1]) or fully_contained(pair[1], pair[0])


def fully_contained(a: Bounds, b: Bounds):
    return a[0] <= b[0] and a[1] >= b[1]


class Day04PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(4, "a")

    def _new_solver(self):
        return Day04PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 2)]


if __name__ == "__main__":
    controller = Day04PartAController()
    controller.run()
