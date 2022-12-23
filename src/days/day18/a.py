from src.shared.controller import Controller
from src.days.day18.solver import AnswerType, Day18Solver, get_free_adjacent
from src.shared.file_result import FileResult


class Day18PartASolver(Day18Solver):
    def solve(self) -> AnswerType:
        return sum([len(get_free_adjacent(point, self.cubes)) for point in self.cubes])


class Day18PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(18, "a")

    def _new_solver(self):
        return Day18PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 64)]


if __name__ == "__main__":
    controller = Day18PartAController()
    controller.run()
