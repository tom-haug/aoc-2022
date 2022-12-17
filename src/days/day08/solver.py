from abc import abstractmethod
from typing import Any
import numpy as np

from nptyping import NDArray
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines


AnswerType = int


class Day08Solver(Solver[AnswerType]):
    tree_matrix: NDArray

    def initialize(self, file_path: str, extra_params: dict[str, Any]):
        input = load_text_file_lines(file_path)
        self.tree_matrix = np.array([[int(char) for char in line] for line in input])

    @abstractmethod
    def solve(self) -> AnswerType:
        ...

    def _tree_lines(self, x: int, y: int) -> tuple[NDArray, NDArray, NDArray, NDArray]:
        left = np.flip(self.tree_matrix[y, :x])
        right = self.tree_matrix[y, x + 1 :]
        up = np.flip(self.tree_matrix[:y, x])
        down = self.tree_matrix[y + 1 :, x]
        return left, right, up, down
