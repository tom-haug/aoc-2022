from abc import abstractmethod
import re
from typing import Any, Callable, Iterator, Optional
from attr import dataclass
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file


AnswerType = int
Point = tuple[int, int]
Range = tuple[int, int]


def manhattan_distance(a: Point, b: Point) -> int:
    return abs((a[0] - b[0])) + abs((a[1] - b[1]))


def ranges_adjacent_or_overlap(a: Range, b: Range) -> bool:
    return max(a[0], b[0]) - 1 <= min(a[1], b[1])


def combine_ranges(a: Range, b: Range) -> Range:
    return (min(a[0], b[0]), max(a[1], b[1]))


def reduce_ranges(ranges: list[Range]) -> list[Range]:
    result = list[Range]()
    for a in sorted(ranges, key=lambda r: r[0]):
        combined = False
        for idx, b in enumerate(result):
            if ranges_adjacent_or_overlap(a, b):
                combined = True
                result[idx] = combine_ranges(a, b)
                break
        if not combined:
            result.append(a)
    return result


@dataclass
class Sensor:
    location: Point
    beacon: Point

    def dead_zone_range(self, y) -> Optional[Range]:
        dist = manhattan_distance(self.beacon, self.location)
        if not self.location[1] - dist <= y <= self.location[1] + dist:
            return None
        x_offset = dist - abs(self.location[1] - y)
        min_x = self.location[0] - x_offset
        max_x = self.location[0] + x_offset
        return (min_x, max_x)


class Day15Solver(Solver[AnswerType]):
    sensors: list[Sensor]
    extra_params: dict[str, Any]

    def initialize(self, file_path: str, extra_params: dict[str, Any]):
        input = load_text_file(file_path) or ""
        self.extra_params = extra_params
        self.sensors = [sensor for sensor in self.__parse_sensor(input)]

    def __parse_sensor(self, input: str) -> Iterator[Sensor]:
        for match in re.finditer(
            r"Sensor\sat\sx=(-?\d+),\sy=(-?\d+):\sclosest\sbeacon\sis\sat\sx=(-?\d+),\sy=(-?\d+)",
            input,
        ):
            yield Sensor(
                (int(match.group(1)), int(match.group(2))),
                (int(match.group(3)), int(match.group(4))),
            )

    def _dead_zone_ranges(
        self, y: int, transform: Callable[[Range], Range] = lambda x: x
    ) -> list[Range]:
        ranges = [
            transform(range)
            for range in [sensor.dead_zone_range(y) for sensor in self.sensors]
            if range is not None
        ]
        return reduce_ranges(ranges)

    @abstractmethod
    def solve(self) -> AnswerType:
        ...
