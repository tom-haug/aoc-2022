import numpy as np
import numpy.ma as ma
from src.shared.controller import Controller
from src.days.day08.solver import AnswerType, Day08Solver
from src.shared.file_result import FileResult


class Day08PartASolver(Day08Solver):
    def solve(self) -> AnswerType:
        height, width = self.tree_matrix.shape
        mask = np.full(self.tree_matrix.shape, False)

        for y in range(1, height - 1):
            for x in range(1, width - 1):
                cur = self.tree_matrix[y, x]
                left, right, up, down = self._tree_lines(x, y)

                # if all four directions have tree at least as tall, this one is masked
                if all(
                    height >= cur
                    for height in [left.max(), right.max(), up.max(), down.max()]
                ):
                    mask[y, x] = True
        return ma.masked_array(self.tree_matrix, mask).count()


class Day08PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(8, "a")

    def _new_solver(self):
        return Day08PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 21)]


if __name__ == "__main__":
    controller = Day08PartAController()
    controller.run()
