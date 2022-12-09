from abc import abstractmethod
import numpy as np

from nptyping import NDArray
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines


AnswerType = int


class Day08Solver(Solver[AnswerType]):
    tree_matrix: NDArray

    def initialize(self, file_path: str):
        input = load_text_file_lines(file_path)
        self.tree_matrix = np.array([[int(char) for char in line] for line in input])

    @abstractmethod
    def solve(self) -> AnswerType:
        ...
