from typing import Iterator
from src.shared.controller import Controller
from src.days.day03.solver import AnswerType, Day03Solver
from src.shared.file_result import FileResult


class Day03PartASolver(Day03Solver):
    def _get_shared_items(self) -> Iterator[str]:
        for compartments in self.rucksacks:
            yield from compartments[0].intersection(compartments[1])


class Day03PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(3, "a")

    def _new_solver(self):
        return Day03PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 157)]


if __name__ == "__main__":
    controller = Day03PartAController()
    controller.run()
