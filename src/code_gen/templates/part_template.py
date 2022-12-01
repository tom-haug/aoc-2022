PART_TEMPLATE = """
from src.shared.controller import Controller
from src.days.day{day_string}.solver import Day{day_string}Solver


AnswerType = int


class Day{day_string}Part{part_upper}Solver(Day{day_string}Solver):
    def solve(self) -> AnswerType:
        return -1


class Day{day_string}Part{part_upper}Controller(Controller):
    def __init__(self):
        super().__init__({year}, {day_int}, '{part}')

    def new_solver(self):
        return Day{day_string}Part{part_upper}Solver()

    def sample_files(self) -> list[tuple[str, AnswerType]]:
        return [('src/days/day{day_string}/inputs/sample01.txt', -1)]

    def file_path(self) -> str:
        return 'src/days/day{day_string}/inputs/main.txt'


if __name__ == "__main__":
    controller = Day{day_string}Part{part_upper}Controller()
    controller.run()
"""
