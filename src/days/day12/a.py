from src.shared.controller import Controller
from src.days.day12.solver import AnswerType, Day12Solver, PathFinder
from src.shared.file_result import FileResult


class Day12PartASolver(Day12Solver):
    def solve(self) -> AnswerType:
        path_finder = PathFinder(self.matrix)
        return path_finder.step_count(self.start, self.goal)


class Day12PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(12, "a")

    def _new_solver(self):
        return Day12PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 31)]


if __name__ == "__main__":
    controller = Day12PartAController()
    controller.run()
