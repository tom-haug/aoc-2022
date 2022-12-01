from abc import ABC, abstractmethod
from typing import Any


class Solver(ABC):
    @abstractmethod
    def initialize(self, file_path: str) -> None:
        pass

    @abstractmethod
    def solve(self) -> Any:
        pass
