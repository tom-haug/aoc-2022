SOLVER_TEMPLATE = """
from abc import abstractmethod
from typing import Any
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines


AnswerType = int


class Day{day_string}Solver(Solver[AnswerType]):
    data: list[str]

    def initialize(self, file_path: str, extra_params: dict[str, Any]):
        input = load_text_file_lines(file_path)
        self.data = input

    @abstractmethod
    def solve(self) -> AnswerType:
        ...
"""
