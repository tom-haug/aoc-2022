from abc import ABC, abstractmethod, abstractproperty
from typing import Iterator

from attr import dataclass


@dataclass
class Rock(ABC):
    type: int
    x: int
    y: int
    falling: bool

    @abstractmethod
    def produce_points(self) -> Iterator[tuple[int, int]]:
        ...

    @abstractproperty
    def width(self) -> int:
        ...


@dataclass
class HorizontalRock(Rock):
    @property
    def width(self) -> int:
        return 4

    def produce_points(self) -> Iterator[tuple[int, int]]:
        for x in range(0, 4):
            yield (self.x + x, self.y)


@dataclass
class PlusRock(Rock):
    @property
    def width(self) -> int:
        return 3

    def produce_points(self) -> Iterator[tuple[int, int]]:
        yield (self.x, self.y + 1)
        yield (self.x + 1, self.y)
        yield (self.x + 1, self.y + 1)
        yield (self.x + 1, self.y + 2)
        yield (self.x + 2, self.y + 1)


@dataclass
class CornerRock(Rock):
    @property
    def width(self) -> int:
        return 3

    def produce_points(self) -> Iterator[tuple[int, int]]:
        yield (self.x, self.y)
        yield (self.x + 1, self.y)
        yield (self.x + 2, self.y)
        yield (self.x + 2, self.y + 1)
        yield (self.x + 2, self.y + 2)


@dataclass
class VerticalRock(Rock):
    @property
    def width(self) -> int:
        return 1

    def produce_points(self) -> Iterator[tuple[int, int]]:
        for y in range(0, 4):
            yield (self.x, self.y + y)


@dataclass
class SquareRock(Rock):
    @property
    def width(self) -> int:
        return 2

    def produce_points(self) -> Iterator[tuple[int, int]]:
        for x in range(0, 2):
            for y in range(0, 2):
                yield (self.x + x, self.y + y)


def rock_factory(type, y: int) -> Rock:
    match type:
        case 0:
            return HorizontalRock(type, 2, y, True)
        case 1:
            return PlusRock(type, 2, y, True)
        case 2:
            return CornerRock(type, 2, y, True)
        case 3:
            return VerticalRock(type, 2, y, True)
        case _:
            return SquareRock(type, 2, y, True)
