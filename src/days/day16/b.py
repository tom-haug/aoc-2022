from typing import Any
from src.shared.controller import Controller
from src.days.day16.solver import AnswerType, Day16Solver, Player, StartingLocation
from src.shared.extra_params import ExtraParams
from src.shared.file_result import FileResult


class Day16PartBSolver(Day16Solver):
    @property
    def _players(self) -> list[Player]:
        return [Player(StartingLocation.AA, 26), Player(StartingLocation.AAA, 26)]


class Day16PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(16, "b")

    def _new_solver(self):
        return Day16PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 1707)]

    def _main_input_extra_params(self) -> dict[str, Any]:
        return {ExtraParams.LongRunning: True}


if __name__ == "__main__":
    controller = Day16PartBController()
    controller.run()
