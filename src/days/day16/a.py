from src.shared.controller import Controller
from src.days.day16.solver import (
    AnswerType,
    Day16Solver,
    Player,
    StartingLocation,
)
from src.shared.file_result import FileResult


class Day16PartASolver(Day16Solver):
    @property
    def _players(self) -> list[Player]:
        return [Player(StartingLocation.AA, 30)]


class Day16PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(16, "a")

    def _new_solver(self):
        return Day16PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 1651)]


if __name__ == "__main__":
    controller = Day16PartAController()
    controller.run()
