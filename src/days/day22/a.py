import numpy as np
from src.days.day22.models import (
    FacingDirection,
    MoveInstruction,
    Point,
    TurnInstruction,
)
from src.shared.controller import Controller
from src.days.day22.solver import (
    AnswerType,
    Day22Solver,
    calc_password,
)
from src.shared.file_result import FileResult


class Day22PartASolver(Day22Solver):
    def solve(self) -> AnswerType:
        location = self.starting_loc
        facing_dir = FacingDirection.Right

        for instruction in self.instructions:
            match instruction:
                case MoveInstruction(amount=amount):
                    for _ in range(amount):
                        location = self.move_2d(self.map, location, facing_dir)
                case TurnInstruction(direction=turn_dir):
                    facing_dir = self.turn(facing_dir, turn_dir)
        return calc_password(location, facing_dir)

    def _wrap_location(self, location: Point, facing: FacingDirection) -> Point:
        match facing:
            case FacingDirection.Left:
                map_slice = self.map[0:, location.y]
                x = np.where(map_slice != " ")[0][-1]
                return Point(x, location.y)
            case FacingDirection.Right:
                map_slice = self.map[0:, location.y]
                x = np.where(map_slice != " ")[0][0]
                return Point(x, location.y)
            case FacingDirection.Up:
                map_slice = self.map[location[0], 0:]
                y = np.where(map_slice != " ")[0][-1]
                return Point(location[0], y)
            case FacingDirection.Down:
                map_slice = self.map[location[0], 0:]
                y = np.where(map_slice != " ")[0][0]
                return Point(location[0], y)


class Day22PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(22, "a")

    def _new_solver(self):
        return Day22PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 6032)]


if __name__ == "__main__":
    controller = Day22PartAController()
    controller.run()
