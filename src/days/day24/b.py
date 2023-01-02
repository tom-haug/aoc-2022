from typing import Any
from src.shared.controller import Controller
from src.days.day24.solver import (
    AnswerType,
    Day24Solver,
    Point,
)
from src.shared.extra_params import ExtraParams
from src.shared.file_result import FileResult


class Day24PartBSolver(Day24Solver):
    def solve(self) -> AnswerType:
        turn_num = 0

        starting = Point(0, -1)
        goal = Point(self.map_width - 1, self.map_height - 1)
        turn_num = self._move_to_goal(turn_num, starting, goal)

        starting = Point(self.map_width - 1, self.map_height)
        goal = Point(0, 0)
        turn_num = self._move_to_goal(turn_num, starting, goal)

        starting = Point(0, -1)
        goal = Point(self.map_width - 1, self.map_height - 1)
        turn_num = self._move_to_goal(turn_num, starting, goal)

        return turn_num


class Day24PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(24, "b")

    def _new_solver(self):
        return Day24PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 54)]

    def _main_input_extra_params(self) -> dict[str, Any]:
        return {ExtraParams.LongRunning: True}


if __name__ == "__main__":
    controller = Day24PartBController()
    controller.run()
