from abc import abstractmethod
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines


AnswerType = int


class Day03Solver(Solver[AnswerType]):
    rucksacks: list[tuple[str, str]]

    def initialize(self, file_path: str):
        input = load_text_file_lines(file_path)
        self.rucksacks = [
            (line[: int(len(line) / 2)], line[int(len(line) / 2) :]) for line in input
        ]

    @abstractmethod
    def _get_shared_items(self) -> list[str]:
        ...

    def solve(self) -> AnswerType:
        shared_items = self._get_shared_items()
        item_priorities = [self._calc_item_priority(item) for item in shared_items]
        return sum(item_priorities)

    def _calc_item_priority(self, item: str):
        if item.isupper():
            return ord(item) - ord("A") + 27
        else:
            return ord(item) - ord("a") + 1
