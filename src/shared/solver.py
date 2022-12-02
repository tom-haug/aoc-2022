from abc import ABC, abstractmethod
from typing import Generic, TypeVar

_TSolution = TypeVar("_TSolution")


class Solver(ABC, Generic[_TSolution]):
    @abstractmethod
    def initialize(self, file_path: str) -> None:
        pass

    @abstractmethod
    def solve(self) -> _TSolution:
        pass
