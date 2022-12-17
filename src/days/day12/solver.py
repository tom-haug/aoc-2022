from abc import abstractmethod
import math
from typing import Any
from astar import AStar
from nptyping import NDArray, Int32

import numpy as np
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines


AnswerType = int
Point = tuple[int, int]


class PathFinder(AStar):
    matrix: NDArray[Any, Int32]
    width: int
    height: int

    def __init__(self, matrix: NDArray):
        self.matrix = matrix
        self.height, self.width = matrix.shape

    def heuristic_cost_estimate(self, current: Point, goal: Point) -> float:
        (x1, y1) = current
        (x2, y2) = goal
        return math.hypot(x2 - x1, y2 - y1)

    def distance_between(self, n1, n2) -> float:
        return 1

    def neighbors(self, node: Point) -> list[Point]:
        x, y = node
        return [
            (x2, y2)
            for x2, y2 in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
            if 0 <= x2 < self.width
            and 0 <= y2 < self.height
            and self.matrix[y2, x2] <= self.matrix[y, x] + 1
        ]

    def step_count(self, start: Point, end: Point) -> int:
        solution = self.astar(start, end)
        points = [] if solution is None else list(solution)
        return len(points) - 1


class Day12Solver(Solver[AnswerType]):
    matrix: NDArray
    start: Point
    goal: Point

    def initialize(self, file_path: str, extra_params: dict[str, Any]):
        input = load_text_file_lines(file_path)
        self.matrix = np.array(
            [
                [self.__location_height(char, x, y) for x, char in enumerate(line)]
                for y, line in enumerate(input)
            ]
        )

    def __location_height(self, char: str, x, y) -> int:
        if char == "S":
            char = "a"
            self.start = (x, y)
        elif char == "E":
            char = "z"
            self.goal = (x, y)
        return ord(char) - ord("a")

    @abstractmethod
    def solve(self) -> AnswerType:
        ...
