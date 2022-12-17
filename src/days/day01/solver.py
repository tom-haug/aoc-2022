from abc import abstractmethod
from typing import Any
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file


AnswerType = int


class Day01Solver(Solver[AnswerType]):
    elf_calories: list[int]

    def initialize(self, file_path: str, extra_params: dict[str, Any]):
        self.elf_calories = self.__load_data_structures(file_path)

    def __load_data_structures(self, file_path: str) -> list[int]:
        input = load_text_file(file_path)
        elf_calories = [] if input is None else input.split("\n\n")
        elf_calorie_sum = [
            sum([int(calorie) for calorie in elf.strip().split("\n")])
            for elf in elf_calories
        ]
        return elf_calorie_sum

    @abstractmethod
    def solve(self) -> int:
        ...
