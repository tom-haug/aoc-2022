from __future__ import annotations
from abc import abstractmethod
from enum import IntEnum
from typing import NamedTuple
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines


AnswerType = int


class Orientation(IntEnum):
    Horizontal = 0
    Vertical = 1


class Point(NamedTuple):
    x: int
    y: int


class BlizzardKey(NamedTuple):
    orientation: Orientation
    const_coord: int


class LinearEquation(NamedTuple):
    slope: int
    intercept: int


BlizzardDict = dict[BlizzardKey, list[LinearEquation]]


class Day24Solver(Solver[AnswerType]):
    blizzards: BlizzardDict
    map_width: int
    map_height: int

    def initialize(self, file_path: str):
        input = load_text_file_lines(file_path)
        self.blizzards = {}
        self.map_height = len(input) - 2
        self.map_width = len(input[0]) - 2
        for y, line in enumerate(input[1:-1]):
            for x, char in enumerate(line[1:-1]):
                match char:
                    case "<":
                        orientation = Orientation.Horizontal
                        const_coord = y
                        intercept = x
                        slope = -1
                    case ">":
                        orientation = Orientation.Horizontal
                        const_coord = y
                        intercept = x
                        slope = 1
                    case "^":
                        orientation = Orientation.Vertical
                        const_coord = x
                        intercept = y
                        slope = -1
                    case "v":
                        orientation = Orientation.Vertical
                        const_coord = x
                        intercept = y
                        slope = 1
                    case _:
                        continue
                key = BlizzardKey(orientation, const_coord)
                equation = LinearEquation(slope, intercept)
                if key in self.blizzards:
                    self.blizzards[key].append(equation)
                else:
                    self.blizzards[key] = [equation]

    @abstractmethod
    def solve(self) -> AnswerType:
        ...

    def _move_to_goal(self, turn_num: int, starting_loc: Point, goal: Point) -> int:
        blizzards = self.blizzards
        player_locations = {starting_loc}

        while True:
            for loc in player_locations:
                if (loc.x, loc.y) == (goal.x, goal.y):
                    # goal is one square away from the exit
                    return turn_num + 1

            ending_locations = set[Point]()
            for location in player_locations:
                possible_moves = moveable_locations(
                    turn_num + 1, blizzards, location, self.map_width, self.map_height
                )
                ending_locations = ending_locations | possible_moves
            player_locations = ending_locations
            turn_num += 1


def moveable_locations(
    turn_num: int,
    blizzards: BlizzardDict,
    player_loc: Point,
    map_width: int,
    map_height: int,
) -> set[Point]:
    possible_moves = set[Point]()
    # do nothing
    if not blizzard_check(turn_num, blizzards, player_loc, map_width, map_height):
        possible_moves.add(player_loc)

    # left
    check = Point(player_loc.x - 1, player_loc.y)
    if (
        player_loc.x > 0
        and 0 <= player_loc.y <= map_height - 1
        and not blizzard_check(turn_num, blizzards, check, map_width, map_height)
    ):
        possible_moves.add(check)

    # right
    check = Point(player_loc.x + 1, player_loc.y)
    if (
        player_loc.x < map_width - 1
        and 0 <= player_loc.y <= map_height - 1
        and not blizzard_check(turn_num, blizzards, check, map_width, map_height)
    ):
        possible_moves.add(check)

    # up
    check = Point(player_loc.x, player_loc.y - 1)
    if player_loc.y > 0 and not blizzard_check(
        turn_num, blizzards, check, map_width, map_height
    ):
        possible_moves.add(check)

    # down
    check = Point(player_loc.x, player_loc.y + 1)
    if player_loc.y < map_height - 1 and not blizzard_check(
        turn_num, blizzards, check, map_width, map_height
    ):
        possible_moves.add(check)

    return possible_moves


def blizzard_check(
    turn_num: int,
    blizzards: BlizzardDict,
    location: Point,
    map_width: int,
    map_height: int,
) -> bool:
    horizontal_blizzards = blizzards.get(
        BlizzardKey(Orientation.Horizontal, location.y), []
    )
    for equation in horizontal_blizzards:
        x = (equation.slope * turn_num + equation.intercept) % map_width
        if (x, location.y) == (location.x, location.y):
            return True

    vertical_blizzards = blizzards.get(
        BlizzardKey(Orientation.Vertical, location.x), []
    )
    for equation in vertical_blizzards:
        y = (equation.slope * turn_num + equation.intercept) % map_height
        if (location.x, y) == (location.x, location.y):
            return True

    return False
