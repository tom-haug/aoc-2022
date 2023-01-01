from __future__ import annotations
from abc import abstractmethod
from typing import Optional
from nptyping import NDArray
import numpy as np
from src.days.day22.models import (
    FacingDirection,
    Instruction,
    MapObject,
    MoveInstruction,
    Point,
    TurnDirection,
    TurnInstruction,
)
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file


AnswerType = int
Map = NDArray


class Day22Solver(Solver[AnswerType]):
    map: NDArray
    starting_loc: Point
    side_length: int
    show_visual: bool

    def initialize(self, file_path: str):
        input = load_text_file(file_path) or ""
        parts = input.split("\n\n")
        self.map, self.starting_loc = parse_map(parts[0])
        self.instructions = parse_instructions(parts[1])

    @abstractmethod
    def solve(self) -> AnswerType:
        ...

    def move_2d(self, map: NDArray, location: Point, facing: FacingDirection) -> Point:
        width, height = map.shape
        check_loc = location
        match facing:
            case FacingDirection.Left:
                check_loc = Point(location.x - 1, location.y)
            case FacingDirection.Right:
                check_loc = Point(location.x + 1, location.y)
            case FacingDirection.Up:
                check_loc = Point(location.x, location.y - 1)
            case FacingDirection.Down:
                check_loc = Point(location.x, location.y + 1)

        in_bounds = (0 <= check_loc.x < width) and (0 <= check_loc.y < height)

        if not in_bounds or map[check_loc] == " ":
            check_loc = self._wrap_location(check_loc, facing)

        return check_loc if map[check_loc] == MapObject.Ground else location

    def turn(self, facing: FacingDirection, turn: TurnDirection) -> FacingDirection:
        match turn:
            case TurnDirection.Left:
                if facing == FacingDirection.Right:
                    return FacingDirection.Up
                return FacingDirection(facing - 1)
            case TurnDirection.Right:
                if facing == FacingDirection.Up:
                    return FacingDirection.Right
                return FacingDirection(facing + 1)

    def _wrap_location(self, location: Point, facing: FacingDirection) -> Point:
        return location


def parse_map(input: str) -> tuple[NDArray, Point]:
    lines = input.split("\n")
    width = max(len(line) for line in lines)
    height = len(lines)
    map = np.full((width, height), " ")
    starting_loc: Optional[Point] = None

    for y, line in enumerate(input.split("\n")):
        for x, char in enumerate(line):
            map[x, y] = char
            if char == "." and starting_loc is None:
                starting_loc = Point(x, y)

    if starting_loc is None:
        raise Exception("Starting location not found")
    return (map, starting_loc)


def parse_instructions(input: str) -> list[Instruction]:
    cur_value = ""
    instructions = list[Instruction]()
    for char in input:
        if char == "L":
            instructions.append(MoveInstruction(int(cur_value)))
            instructions.append(TurnInstruction(TurnDirection.Left))
            cur_value = ""
        elif char == "R":
            instructions.append(MoveInstruction(int(cur_value)))
            instructions.append(TurnInstruction(TurnDirection.Right))
            cur_value = ""
        else:
            cur_value += char

    if len(cur_value) > 0:
        instructions.append(MoveInstruction(int(cur_value)))

    return instructions


def calc_password(location: Point, facing: FacingDirection):
    return int((1000 * (location.y + 1)) + (4 * (location.x + 1)) + int(facing))
