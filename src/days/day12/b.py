from src.shared.controller import Controller
from src.days.day12.solver import AnswerType, Day12Solver, PathFinder
from src.shared.file_result import FileResult
import numpy as np


class Day12PartBSolver(Day12Solver):
    def solve(self) -> AnswerType:
        path_finder = PathFinder(self.matrix)
        steps = [
            path_finder.step_count((point[1], point[0]), self.goal)
            for point in zip(*np.where(self.matrix == 0))
            if len(point) == 2
        ]
        return min([step for step in steps if step > 0])


class Day12PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(12, "b")

    def _new_solver(self):
        return Day12PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 29)]


if __name__ == "__main__":
    controller = Day12PartBController()
    controller.run()
