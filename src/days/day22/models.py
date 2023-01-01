from __future__ import annotations
from collections import namedtuple
from enum import Enum, IntEnum, StrEnum

from attr import dataclass


Point = namedtuple("Point", ["x", "y"])


class TurnDirection(Enum):
    Left = 0
    Right = 1

    @classmethod
    def parse(cls, value: str) -> TurnDirection:
        if value == "L":
            return cls.Left
        else:
            return cls.Right


class FacingDirection(IntEnum):
    Right = 0
    Down = 1
    Left = 2
    Up = 3


class MapObject(StrEnum):
    Empty = " "
    Ground = "."
    Wall = "#"
    Path = "!"
    Edge = "%"


@dataclass
class MoveInstruction:
    amount: int


@dataclass
class TurnInstruction:
    direction: TurnDirection


Instruction = MoveInstruction | TurnInstruction
