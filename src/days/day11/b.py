import math
import re
from typing import Callable
from src.shared.controller import Controller
from src.days.day11.solver import AnswerType, Day11Solver
from src.shared.file_result import FileResult


class Day11PartBSolver(Day11Solver):
    """
    - Calculate least common multiple from all the monkeys' divisors
    - After applying the monkey's operator, modulo on the lcm to keep worry level at the minimum possible
    """

    lcm: int

    def _pre_parse(self, input: str) -> None:
        divisors = [
            int(divisor.group())
            for divisor in re.finditer(r"(?<=divisible\sby\s)\d+", input)
        ]
        self.lcm = math.lcm(*divisors)

    def _monkey_operation(
        self, operator: Callable[[int, int], int]
    ) -> Callable[[int, int], int]:
        return lambda x, y: operator(x, y) % self.lcm

    @property
    def _num_rounds(self) -> int:
        return 10000


class Day11PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(11, "b")

    def _new_solver(self):
        return Day11PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 2713310158)]


if __name__ == "__main__":
    controller = Day11PartBController()
    controller.run()
