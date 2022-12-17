from abc import abstractproperty
from typing import Any
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines
from more_itertools import sliding_window


AnswerType = int


class Day06Solver(Solver[AnswerType]):
    signal: list[str]

    def initialize(self, file_path: str, extra_params: dict[str, Any]):
        input = load_text_file_lines(file_path)[0]
        self.signal = [*input]

    def solve(self) -> AnswerType:
        for idx, seq in enumerate(sliding_window(self.signal, self.window_size)):
            if len(set(seq)) == self.window_size:
                return idx + self.window_size
        return -1

    @abstractproperty
    def window_size(self) -> int:
        ...
