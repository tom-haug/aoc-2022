from __future__ import annotations
from abc import abstractmethod
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines
from enum import IntEnum


class RoundResult(IntEnum):
    WIN = 1
    LOSE = -1
    DRAW = 0

    @classmethod
    def parse(cls, value: str) -> RoundResult:
        match value:
            case "X":
                return cls.LOSE
            case "Y":
                return cls.DRAW
            case _:
                return cls.WIN


class Shape(IntEnum):
    ROCK = 0
    PAPER = 1
    SCISSOR = 2

    @classmethod
    def parse(cls, value: str) -> Shape:
        match value:
            case "A" | "X":
                return cls.ROCK
            case "B" | "Y":
                return cls.PAPER
            case _:
                return cls.SCISSOR


AnswerType = int
Round = tuple[Shape, Shape]


class Day02Solver(Solver[AnswerType]):
    rounds: list[Round]

    def initialize(self, file_path: str):
        input = load_text_file_lines(file_path)
        self.rounds = [self.__parse_round(line) for line in input]

    def solve(self) -> AnswerType:
        return sum([calc_score(*round) for round in self.rounds])

    def __parse_round(self, input: str) -> Round:
        value_1, value_2 = input.split(" ")
        their_shape = Shape.parse(value_1)
        my_shape = self._get_my_shape(their_shape, value_2)
        return (their_shape, my_shape)

    @abstractmethod
    def _get_my_shape(self, their_shape: Shape, second_value: str) -> Shape:
        ...


def calc_score(their_shape: Shape, my_shape: Shape) -> int:
    return battle_score(my_shape, their_shape) + shape_score(my_shape)


def shape_score(my_shape: Shape) -> int:
    return int(my_shape) + 1


def battle_score(my_shape: Shape, their_shape: Shape) -> int:
    if my_shape == their_shape:
        return 3
    elif my_shape == wins_against(their_shape):
        return 6
    return 0


def wins_against(loser: Shape) -> Shape:
    return Shape((int(loser) + 1) % 3)
