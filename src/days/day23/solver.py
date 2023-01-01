from abc import abstractmethod
from collections import deque, namedtuple
from enum import Enum
from typing import Any, Optional
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines


AnswerType = int


Point = namedtuple("Point", ["x", "y"])


class Direction(Enum):
    North = 0
    South = 1
    West = 2
    East = 3


class Day23Solver(Solver[AnswerType]):
    elves: set[Point]

    def initialize(self, file_path: str, extra_params: dict[str, Any]):
        input = load_text_file_lines(file_path)
        self.elves = {
            Point(x, y)
            for y, line in enumerate(input)
            for x, char in enumerate(line)
            if char == "#"
        }
        self.check_direction = deque[Direction]()
        self.check_direction.extend(
            [Direction.East, Direction.West, Direction.South, Direction.North]
        )

    @abstractmethod
    def solve(self) -> AnswerType:
        ...

    def _turn(self) -> bool:
        blocked_locations = set[Point]()
        proposed_moves = dict[Point, Point]()

        # propose
        for elf in self.elves:
            if not self.__any_adjacent(elf):
                continue
            self.__propose_movement(elf, blocked_locations, proposed_moves)

        # move
        for new_loc in proposed_moves:
            self.__move(proposed_moves[new_loc], new_loc)

        # cycle direction sequence
        self.check_direction.appendleft(self.check_direction.pop())

        # did we do anything?
        return len(proposed_moves) > 0

    def __any_adjacent(self, elf: Point) -> bool:
        for x in range(elf.x - 1, elf.x + 2):
            for y in range(elf.y - 1, elf.y + 2):
                if (x, y) != elf and (x, y) in self.elves:
                    return True
        return False

    def __propose_movement(
        self,
        elf: Point,
        blocked_locations: set[Point],
        proposed_moves: dict[Point, Point],
    ):
        move_loc: Optional[Point] = None
        for dir in reversed(self.check_direction):
            can_move = True
            match dir:
                case Direction.North:
                    for x in range(elf.x - 1, elf.x + 2):
                        if Point(x, elf.y - 1) in self.elves:
                            can_move = False
                            break
                    if can_move:
                        move_loc = Point(elf.x, elf.y - 1)
                case Direction.South:
                    for x in range(elf.x - 1, elf.x + 2):
                        if Point(x, elf.y + 1) in self.elves:
                            can_move = False
                            break
                    if can_move:
                        move_loc = Point(elf.x, elf.y + 1)
                case Direction.West:
                    for y in range(elf.y - 1, elf.y + 2):
                        if Point(elf.x - 1, y) in self.elves:
                            can_move = False
                            break
                    if can_move:
                        move_loc = Point(elf.x - 1, elf.y)
                case Direction.East:
                    for y in range(elf.y - 1, elf.y + 2):
                        if Point(elf.x + 1, y) in self.elves:
                            can_move = False
                            break
                    if can_move:
                        move_loc = Point(elf.x + 1, elf.y)
            if move_loc is not None:
                break
        if move_loc is not None:
            if move_loc in blocked_locations:
                ...
            elif move_loc in proposed_moves:
                del proposed_moves[move_loc]
                blocked_locations.add(move_loc)
            else:
                proposed_moves[move_loc] = elf

    def __move(self, elf: Point, new_loc: Point):
        self.elves.remove(elf)
        self.elves.add(new_loc)
