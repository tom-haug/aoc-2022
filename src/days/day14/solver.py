from abc import abstractproperty
from typing import Any, Iterator, Optional

from numpy import sign
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines
from more_itertools import sliding_window

AnswerType = int
SAND_SOURCE = (500, 0)


class Day14Solver(Solver[AnswerType]):
    occupied: set[tuple[int, int]]
    max_y: int

    def initialize(self, file_path: str, extra_params: dict[str, Any]):
        input = load_text_file_lines(file_path)
        self.max_y = 0
        self.occupied = set(
            point for line in input for point in self.__parse_line(line)
        )

    def __parse_line(self, line: str) -> Iterator[tuple[int, int]]:
        coords = self.__parse_coords(line)
        return self.__generate_points(coords)

    def __parse_coords(self, line: str) -> list[tuple[int, int]]:
        return [
            (int(coord[0]), int(coord[1]))
            for coord in [
                point.split(",") for point in [points for points in line.split(" -> ")]
            ]
        ]

    def __generate_points(
        self, coords: list[tuple[int, int]]
    ) -> Iterator[tuple[int, int]]:
        for (a, b) in sliding_window(coords, 2):
            x_sign = sign(b[0] - a[0])
            y_sign = sign(b[1] - a[1])
            if x_sign != 0:
                for x in range(a[0], b[0] + x_sign, x_sign):
                    yield (x, a[1])
            if y_sign != 0:
                for y in range(a[1], b[1] + y_sign, y_sign):
                    if y > self.max_y:
                        self.max_y = y
                    yield (a[0], y)

    def solve(self) -> AnswerType:
        sand_count = 0
        done = False
        while not done:
            sand_count += 1
            x, y = SAND_SOURCE
            while True:
                if self.floor_y is None and y > self.max_y:
                    done = True
                    sand_count -= 1
                    break
                elif self.floor_y is not None and y + 1 == self.floor_y:
                    self.occupied.add((x, y))
                    break
                elif (x, y + 1) not in self.occupied:
                    y = y + 1
                elif (x - 1, y + 1) not in self.occupied:
                    x = x - 1
                    y = y + 1
                elif (x + 1, y + 1) not in self.occupied:
                    x = x + 1
                    y = y + 1
                else:
                    self.occupied.add((x, y))
                    if (x, y) == SAND_SOURCE:
                        done = True
                    break
        return sand_count

    @abstractproperty
    def floor_y(self) -> Optional[int]:
        ...
