from abc import abstractmethod
from typing import Any
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines


AnswerType = int
Bounds = tuple[int, int]
BoundsPair = tuple[Bounds, Bounds]


class Day04Solver(Solver[AnswerType]):
    pairs: list[BoundsPair]

    def initialize(self, file_path: str, extra_params: dict[str, Any]):
        input = load_text_file_lines(file_path)
        self.pairs = [split_pairs(line) for line in input]

    def solve(self) -> AnswerType:
        return sum(1 for pair in self.pairs if self._compare(pair))

    @abstractmethod
    def _compare(self, pair: BoundsPair) -> bool:
        ...


def split_pairs(pairs: str) -> BoundsPair:
    a, b = pairs.split(",")
    return split_bounds(a), split_bounds(b)


def split_bounds(pair: str) -> Bounds:
    start, end = pair.split("-")
    return int(start), int(end)
