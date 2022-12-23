from src.shared.controller import Controller
from src.days.day18.solver import AnswerType, Day18Solver, Point3D, get_free_adjacent
from src.shared.file_result import FileResult

Bound = tuple[int, int]


class Day18PartBSolver(Day18Solver):
    def solve(self) -> AnswerType:
        finder = ExteriorFinder(self.cubes)
        exterior_surface_area = list[Point3D]()
        for cube in self.cubes:
            for adjacent in get_free_adjacent(cube, self.cubes):
                if finder.is_exterior(adjacent):
                    exterior_surface_area.append(adjacent)
        return len(exterior_surface_area)


class ExteriorFinder:
    bounds: tuple[Bound, Bound, Bound]
    collected_points: set[Point3D]
    closed_points: set[Point3D]
    open_points: set[Point3D]
    all_points: set[Point3D]

    def __init__(self, all_points: set[Point3D]):
        self.all_points = all_points
        self.closed_points = set()
        self.open_points = set()
        x_bounds = get_bounds(all_points, 0)
        y_bounds = get_bounds(all_points, 1)
        z_bounds = get_bounds(all_points, 2)
        self.bounds = (x_bounds, y_bounds, z_bounds)

    def is_exterior(self, origin: Point3D) -> bool:
        self.collected_points = set()
        enclosed = self.__expand(origin)
        if enclosed:
            self.closed_points.update(self.collected_points)
            return False
        else:
            self.open_points.update(self.collected_points)
            return True

    def __expand(self, point: Point3D) -> bool:
        if not point_in_bounds(point, self.bounds):
            return False
        if point in self.closed_points:
            return True
        if point in self.open_points:
            return False
        free_adjacent = get_free_adjacent(point, self.all_points)
        uncollected_free_adjacent = {
            point for point in free_adjacent if point not in self.collected_points
        }

        self.collected_points.update(uncollected_free_adjacent)

        for point in uncollected_free_adjacent:
            result = self.__expand(point)
            if not result:
                return False

        return True


def get_bounds(points: set[Point3D], dim: int) -> Bound:
    dim_values = [point[dim] for point in points]
    return (min(dim_values), max(dim_values))


def point_in_bounds(point: Point3D, bounds: tuple[Bound, Bound, Bound]) -> bool:
    return (
        bounds[0][0] <= point[0] <= bounds[0][1]
        and bounds[1][0] <= point[1] <= bounds[1][1]
        and bounds[2][0] <= point[2] <= bounds[2][1]
    )


class Day18PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(18, "b")

    def _new_solver(self):
        return Day18PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 58)]


if __name__ == "__main__":
    controller = Day18PartBController()
    controller.run()
