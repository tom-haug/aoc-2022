PART_TEMPLATE = """
from src.shared.controller import Controller
from src.days.day{day_string}.solver import AnswerType, Day{day_string}Solver


class Day{day_string}Part{part_upper}Solver(Day{day_string}Solver):
    def solve(self) -> AnswerType:
        return -1


class Day{day_string}Part{part_upper}Controller(Controller):
    def __init__(self):
        super().__init__({year}, {day_int}, '{part}')

    def _new_solver(self):
        return Day{day_string}Part{part_upper}Solver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    @property
    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", -1)]


if __name__ == "__main__":
    controller = Day{day_string}Part{part_upper}Controller()
    controller.run()
"""
