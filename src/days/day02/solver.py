from __future__ import annotations
from abc import abstractmethod
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines
from enum import Enum

AnswerType = int


class RoundResult(Enum):
    WIN = 1
    LOSE = 2
    DRAW = 3

    @classmethod
    def from_str(cls, value: str) -> RoundResult:
        match value:
            case "X":
                return cls.LOSE
            case "Y":
                return cls.DRAW
            case _:
                return cls.WIN


class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

    @classmethod
    def from_str(cls, value: str) -> Shape:
        match value:
            case "A" | "X":
                return cls.ROCK
            case "B" | "Y":
                return cls.PAPER
            case _:
                return cls.SCISSOR


class Day02Solver(Solver[AnswerType]):
    rounds: list[tuple[Shape, Shape]]

    def initialize(self, file_path: str):
        self.rounds = self.__load_data_structures(file_path)

    def __load_data_structures(self, file_path: str) -> list[tuple[Shape, Shape]]:
        input = load_text_file_lines(file_path)
        result: list[tuple[Shape, Shape]] = []
        for round in input:
            value_1, value_2 = round.split(" ")
            their_shape = Shape.from_str(value_1)
            my_shape = self.get_my_shape(their_shape, value_2)
            result.append((their_shape, my_shape))
        return result

    def _calc_round_score(self, their_shape: Shape, my_shape: Shape) -> int:
        round_outcome = self._round_outcome(my_shape, their_shape)
        shape_score = (
            1 if my_shape == Shape.ROCK else 2 if my_shape == Shape.PAPER else 3
        )
        round_outcome_score = (
            0
            if round_outcome == RoundResult.LOSE
            else 6
            if round_outcome == RoundResult.WIN
            else 3
        )
        return shape_score + round_outcome_score

    def _round_outcome(self, my_shape: Shape, their_shape: Shape) -> RoundResult:
        if my_shape == their_shape:
            return RoundResult.DRAW

        match (my_shape, their_shape):
            case (Shape.ROCK, Shape.SCISSOR):
                return RoundResult.WIN
            case (Shape.PAPER, Shape.ROCK):
                return RoundResult.WIN
            case (Shape.SCISSOR, Shape.PAPER):
                return RoundResult.WIN
            case _:
                return RoundResult.LOSE

    @abstractmethod
    def get_my_shape(self, their_shape: Shape, second_value: str) -> Shape:
        ...

    def solve(self) -> AnswerType:
        return sum([self._calc_round_score(*round) for round in self.rounds])
