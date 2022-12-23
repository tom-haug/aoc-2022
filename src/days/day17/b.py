from src.shared.controller import Controller
from src.days.day17.solver import AnswerType, Day17Solver
from src.shared.file_result import FileResult


class Day17PartBSolver(Day17Solver):
    ROCK_COUNT = 1000000000000

    def _should_stop(self) -> bool:
        return cycle_interval(self.history) > 0

    def _calculate_height(self) -> int:
        return extrapolate_height(
            self.history, cycle_interval(self.history), self.ROCK_COUNT
        )


def cycle_interval(history: list[int]) -> int:
    # arbitrarily chosen threshold that seems about right...
    minimum_cycle_size = 20

    # need at least twice the number of data points to check for repeating
    if len(history) < minimum_cycle_size * 2:
        return -1

    # loop through possible cycle sizes
    for check_cycle_size in range(minimum_cycle_size + 1, len(history) // 2):
        found = True

        # loop through positions in the cycle
        for check_offset in range(1, check_cycle_size + 1):

            # make sure the rock height different matches for the previous two intervals
            prev_interval_diff = (
                history[-1 * check_offset] - history[-1 * (check_offset + 1)]
            )
            prev_prev_interval_diff = (
                history[-1 * (check_cycle_size + check_offset)]
                - history[-1 * (check_cycle_size + check_offset + 1)]
            )
            if prev_interval_diff != prev_prev_interval_diff:
                found = False
                break
        if found:
            return check_cycle_size
    return -1


def extrapolate_height(
    history: list[int], cycle_interval: int, target_cycle_num: int
) -> int:
    current_height = history[-1]
    cur_cycle_num = len(history)
    cycle_height_diff = current_height - history[-1 * cycle_interval - 1]
    num_intervals = (target_cycle_num - cur_cycle_num) // cycle_interval
    full_interval_height = num_intervals * cycle_height_diff
    remainder_rock_count = (target_cycle_num - cur_cycle_num) % cycle_interval

    target_height = current_height + full_interval_height + 1
    for idx in range(remainder_rock_count):
        target_height += (
            history[-1 * (cycle_interval - idx)]
            - history[-1 * (cycle_interval - idx + 1)]
        )
    return target_height


class Day17PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(17, "b")

    def _new_solver(self):
        return Day17PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 1514285714288)]


if __name__ == "__main__":
    controller = Day17PartBController()
    controller.run()
