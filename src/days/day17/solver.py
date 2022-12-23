from abc import abstractmethod
import itertools
from typing import Any
from src.days.day17.rocks import rock_factory
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines


AnswerType = int


class Day17Solver(Solver[AnswerType]):
    CHAMBER_WIDTH = 7
    wind_pattern: list[str]
    history: list[int]

    def initialize(self, file_path: str, extra_params: dict[str, Any]):
        input = load_text_file_lines(file_path)
        self.wind_pattern = [char for char in input[0]]

    def solve(self) -> AnswerType:
        highest = -1
        chamber = set[tuple[int, int]]()
        rock_selector = itertools.cycle(range(5))

        wind_index = 0

        self.history = list[int]()

        # initial floor
        for x in range(self.CHAMBER_WIDTH):
            chamber.add((x, -1))

        while not self._should_stop():
            rock = rock_factory(next(rock_selector), highest + 5)
            while True:
                # move down
                rock.y -= 1
                assimilate = False
                for point in rock.produce_points():
                    if (point[0], point[1]) in chamber:
                        rock.y += 1
                        assimilate = True
                        break

                if assimilate:
                    for point in rock.produce_points():
                        if point[1] > highest:
                            highest = point[1]
                        chamber.add(point)
                    self.history.append(highest)
                    break

                # move over
                wind = self.wind_pattern[wind_index]
                wind_index += 1
                if wind_index > len(self.wind_pattern) - 1:
                    wind_index = 0

                if wind == "<":
                    rock.x -= 1
                    if rock.x < 0:
                        rock.x += 1
                        continue
                    for point in rock.produce_points():
                        if point in chamber:
                            rock.x += 1
                            break
                else:
                    rock.x += 1
                    if rock.x + rock.width - 1 > 6:
                        rock.x -= 1
                        continue
                    for point in rock.produce_points():
                        if point in chamber:
                            rock.x -= 1
                            break

        return self._calculate_height()

    @abstractmethod
    def _should_stop(self) -> bool:
        ...

    @abstractmethod
    def _calculate_height(self) -> int:
        ...
