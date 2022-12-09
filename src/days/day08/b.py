from __future__ import annotations
from nptyping import NDArray
from math import prod
from src.shared.controller import Controller
from src.days.day08.solver import AnswerType, Day08Solver
from src.shared.file_result import FileResult


class Day08PartBSolver(Day08Solver):
    def solve(self) -> AnswerType:
        height, width = self.tree_matrix.shape
        max_scenic_score = 0

        for y in range(1, height - 1):
            for x in range(1, width - 1):
                cur = self.tree_matrix[y, x]
                left, right, up, down = self._tree_lines(x, y)

                trees_per_direction = [
                    line_of_sight_count(direction, cur)
                    for direction in [left, right, up, down]
                ]
                max_scenic_score = max(max_scenic_score, prod(trees_per_direction))
        return max_scenic_score


def line_of_sight_count(trees: NDArray, max_height: int) -> int:
    count = 0
    for tree in trees:
        count += 1
        if tree >= max_height:
            break
    return count


class Day08PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(8, "b")

    def _new_solver(self):
        return Day08PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 8)]


if __name__ == "__main__":
    controller = Day08PartBController()
    controller.run()
