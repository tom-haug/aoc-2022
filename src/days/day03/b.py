from typing import Iterator
from src.shared.controller import Controller
from src.days.day03.solver import AnswerType, Day03Solver, Rucksack
from src.shared.file_result import FileResult


class Day03PartBSolver(Day03Solver):
    def _get_shared_items(self) -> Iterator[str]:
        for group_num in range(0, len(self.rucksacks), 3):
            group = [
                all_items(elf) for elf in self.rucksacks[group_num : group_num + 3]
            ]
            yield from group[0].intersection(group[1]).intersection(group[2])


def all_items(rucksack: Rucksack) -> set[str]:
    return rucksack[0].union(rucksack[1])


class Day03PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(3, "b")

    def _new_solver(self):
        return Day03PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 70)]


if __name__ == "__main__":
    controller = Day03PartBController()
    controller.run()
