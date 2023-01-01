from abc import abstractmethod
from typing import Iterator
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines


AnswerType = int
Point3D = tuple[int, int, int]


class Day18Solver(Solver[AnswerType]):
    cubes: set[Point3D]

    def initialize(self, file_path: str):
        input = load_text_file_lines(file_path)
        self.cubes = {
            (int(coords[0]), int(coords[1]), int(coords[2]))
            for coords in [line.split(",") for line in input]
        }

    @abstractmethod
    def solve(self) -> AnswerType:
        ...


def get_adjacent_points(point: Point3D) -> Iterator[Point3D]:
    for dim in range(3):
        for check in [point[dim] - 1, point[dim] + 1]:
            result = point[:dim] + (check,) + point[dim + 1 :]
            yield (result[0], result[1], result[2])  # make mypy happy


def get_free_adjacent(point: Point3D, all_points: set[Point3D]) -> list[Point3D]:
    return [
        adjacent
        for adjacent in get_adjacent_points(point)
        if adjacent not in all_points
    ]
