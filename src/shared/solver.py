from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

_TSolution = TypeVar("_TSolution")


class Solver(ABC, Generic[_TSolution]):
    @abstractmethod
    def initialize(self, file_path: str, extra_params: dict[str, Any]) -> None:
        pass

    @abstractmethod
    def solve(self) -> _TSolution:
        pass
