from enum import IntEnum
from typing import Any
from nptyping import NDArray
import numpy as np
from src.days.day22.visualization import Plot
from src.days.day22.models import (
    FacingDirection,
    MoveInstruction,
    Point,
    TurnInstruction,
)
from src.shared.controller import Controller
from src.days.day22.solver import AnswerType, Day22Solver, MapObject, calc_password
from src.shared.file_result import FileResult


class SpecialZLayers(IntEnum):
    Path = 0
    Ground = 1


class DataAxisLayer(IntEnum):
    Map = 0
    MetaData = 1


class CubeAxis(IntEnum):
    X = 0
    Y = 1
    Z = 2
    Data = 3


XY_OFFSET = 2


class Day22PartBSolver(Day22Solver):
    def solve(self) -> AnswerType:
        self.side_length = self.extra_params["side_length"]
        self.show_visual = self.extra_params["show_visual"]

        original_cube = np.full(
            tuple(self.side_length + (XY_OFFSET * 2) for _ in range(3))
            + (len(DataAxisLayer),),
            fill_value=(MapObject.Empty),
            dtype=object,
        )

        location = Point(
            self.starting_loc[0] % self.side_length + XY_OFFSET,
            self.starting_loc[1] % self.side_length + XY_OFFSET,
        )

        self.__populate_cube(original_cube, self.starting_loc)

        working_cube = original_cube
        working_cube[(location + (SpecialZLayers.Path,))] = MapObject.Path
        cube_face = get_cube_face(working_cube)

        facing_dir = FacingDirection.Right
        for instruction in self.instructions:
            match instruction:
                case MoveInstruction(amount=amount):
                    for _ in range(amount):
                        working_cube, cube_face, new_location = self.move_3d(
                            working_cube, cube_face, location, facing_dir
                        )
                        if new_location == location:
                            break
                        location = new_location
                        working_cube[
                            (location + (SpecialZLayers.Path,))
                        ] = MapObject.Path

                case TurnInstruction(direction=turn_dir):
                    facing_dir = self.turn(facing_dir, turn_dir)

        if self.show_visual:
            plot = Plot()
            plot.plot_cube(original_cube[:, :, :, DataAxisLayer.Map])
            plot.show()

        orig_loc, orig_facing = self._calc_original_placement(
            working_cube, location, facing_dir
        )

        return calc_password(orig_loc, orig_facing)

    def __populate_cube(self, cube: NDArray, origin: Point):
        # copy map square at origin to top cube face
        for x_offset in range(self.side_length):
            for y_offset in range(self.side_length):
                flat_loc = Point(origin[0] + x_offset, origin[1] + y_offset)
                cube_loc = (
                    x_offset + XY_OFFSET,
                    y_offset + XY_OFFSET,
                    SpecialZLayers.Ground,
                )
                cube[cube_loc + (DataAxisLayer.Map,)] = self.map[flat_loc]
                cube[cube_loc + (DataAxisLayer.MetaData,)] = flat_loc
                self.map[flat_loc] = MapObject.Empty

        # now based on what direction contains data on flat map
        # rotate cube and populate next side
        # left
        width, height = self.map.shape

        check_x = origin[0] - self.side_length
        check_y = origin[1]
        if check_x >= 0 and self.map[check_x, check_y] in (
            MapObject.Ground,
            MapObject.Wall,
        ):
            rotated = np.rot90(cube, k=-1, axes=(CubeAxis.Z, CubeAxis.X))
            self.__populate_cube(rotated, Point(check_x, check_y))

        # right
        check_x = origin[0] + self.side_length
        check_y = origin[1]
        if check_x < width and self.map[check_x, check_y] in (
            MapObject.Ground,
            MapObject.Wall,
        ):
            rotated = np.rot90(cube, axes=(CubeAxis.Z, CubeAxis.X))
            self.__populate_cube(rotated, Point(check_x, check_y))

        # down
        check_x = origin[0]
        check_y = origin[1] + self.side_length
        if check_y < height and self.map[check_x, check_y] in (
            MapObject.Ground,
            MapObject.Wall,
        ):
            rotated = np.rot90(cube, axes=(CubeAxis.Z, CubeAxis.Y))
            self.__populate_cube(rotated, Point(check_x, check_y))

        # up
        check_x = origin[0]
        check_y = origin[1] - self.side_length
        if check_y >= 0 and self.map[check_x, check_y] in (
            MapObject.Ground,
            MapObject.Wall,
        ):
            rotated = np.rot90(cube, k=-1, axes=(CubeAxis.Z, CubeAxis.Y))
            self.__populate_cube(rotated, Point(check_x, check_y))

    def move_3d(
        self,
        cube: NDArray,
        cube_face: NDArray,
        location: Point,
        facing: FacingDirection,
    ) -> tuple[NDArray, NDArray, Point]:
        location = self.move_2d(cube_face, location, facing)

        # when we reach an edge, rotate cube
        width, height = cube_face.shape
        if location[0] < XY_OFFSET:
            # left edge
            cube = np.rot90(cube, k=-1, axes=(CubeAxis.Z, CubeAxis.X))
            cube_face = get_cube_face(cube)
            location = Point(width - XY_OFFSET - 1, location[1])
        elif location[0] >= width - XY_OFFSET:
            # right edge
            cube = np.rot90(cube, axes=(CubeAxis.Z, CubeAxis.X))
            cube_face = get_cube_face(cube)
            location = Point(XY_OFFSET, location[1])
        elif location[1] < XY_OFFSET:
            # top edge
            cube = np.rot90(cube, k=-1, axes=(CubeAxis.Z, CubeAxis.Y))
            cube_face = get_cube_face(cube)
            location = Point(location[0], height - XY_OFFSET - 1)
        elif location[1] >= height - XY_OFFSET:
            # bottom edge
            cube = np.rot90(cube, axes=(CubeAxis.Z, CubeAxis.Y))
            cube_face = get_cube_face(cube)
            location = Point(location[0], XY_OFFSET)
        return cube, cube_face, location

    def _calc_original_placement(
        self, cube: NDArray, location: Point, facing: FacingDirection
    ) -> tuple[Point, FacingDirection]:
        cube_face = cube[
            XY_OFFSET:-XY_OFFSET, XY_OFFSET:-XY_OFFSET, SpecialZLayers.Ground
        ]
        adj_location = Point(location[0] - XY_OFFSET, location[1] - XY_OFFSET)
        width, height, *_ = cube_face.shape
        match facing:
            case FacingDirection.Left:
                if adj_location[0] == 0:
                    from_loc = Point(1, adj_location[1])
                    to_loc = adj_location
                else:
                    from_loc = adj_location
                    to_loc = Point(adj_location[0] - 1, adj_location[1])
            case FacingDirection.Right:
                if adj_location[0] == width - 1:
                    from_loc = Point(width - 2, adj_location[1])
                    to_loc = adj_location
                else:
                    from_loc = adj_location
                    to_loc = Point(adj_location[0] - 1, adj_location[1])
            case FacingDirection.Up:
                if adj_location[1] == 0:
                    from_loc = Point(adj_location[0], 1)
                    to_loc = adj_location
                else:
                    from_loc = adj_location
                    to_loc = Point(adj_location[0], adj_location[1] - 1)
            case FacingDirection.Down:
                if adj_location[1] == height - 1:
                    from_loc = Point(adj_location[0], height - 1)
                    to_loc = adj_location
                else:
                    from_loc = adj_location
                    to_loc = Point(adj_location[0], adj_location[1] + 1)

        orig_loc = cube_face[adj_location + (DataAxisLayer.MetaData,)]
        orig_from_loc = cube_face[from_loc + (DataAxisLayer.MetaData,)]
        orig_to_loc = cube_face[to_loc + (DataAxisLayer.MetaData,)]

        if orig_from_loc[0] < orig_to_loc[0]:
            orig_direction = FacingDirection.Right
        elif orig_from_loc[0] > orig_to_loc[0]:
            orig_direction = FacingDirection.Left
        elif orig_from_loc[1] < orig_to_loc[1]:
            orig_direction = FacingDirection.Down
        else:
            orig_direction = FacingDirection.Up

        return Point(orig_loc, orig_direction)


def get_cube_face(cube: NDArray) -> NDArray:
    return merge_map_slices(
        cube[:, :, SpecialZLayers.Ground, DataAxisLayer.Map],
        cube[:, :, SpecialZLayers.Ground + 1, DataAxisLayer.Map],
    )


def merge_map_slices(a: NDArray, b: NDArray) -> NDArray:
    width, height = a.shape
    result = np.empty(a.shape, dtype=str)
    for x in range(width):
        for y in range(height):
            result[x, y] = (
                a[x, y] if a[x, y] in [MapObject.Ground, MapObject.Wall] else b[x, y]
            )
    return result


class Day22PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(22, "b")

    def _new_solver(self):
        return Day22PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 5031, {"side_length": 4})]

    def _main_input_extra_params(self) -> dict[str, Any]:
        return {"side_length": 50}


if __name__ == "__main__":
    controller = Day22PartBController()
    controller.run()
