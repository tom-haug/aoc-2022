from abc import abstractmethod
from typing import Iterator
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines


AnswerType = int
Rucksack = tuple[set[str], set[str]]


class Day03Solver(Solver[AnswerType]):
    rucksacks: list[Rucksack]

    def initialize(self, file_path: str):
        input = load_text_file_lines(file_path)
        self.rucksacks = [parse_rucksack(line) for line in input]

    def solve(self) -> AnswerType:
        shared_items = self._get_shared_items()
        item_priorities = [calc_item_priority(item) for item in shared_items]
        return sum(item_priorities)

    @abstractmethod
    def _get_shared_items(self) -> Iterator[str]:
        ...


def parse_rucksack(input: str) -> Rucksack:
    separator = len(input) // 2
    return set(input[:separator]), set(input[separator:])


def calc_item_priority(item: str):
    if item.isupper():
        return ord(item) - ord("A") + 27
    else:
        return ord(item) - ord("a") + 1
