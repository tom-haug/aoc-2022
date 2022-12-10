from src.shared.controller import Controller
from src.days.day10.solver import AnswerType, Day10Solver
from src.shared.file_result import FileResult


class Day10PartASolver(Day10Solver):
    def _answer(self) -> AnswerType:
        return sum(
            [
                cycle_num * self.history[cycle_num]["X"]
                for cycle_num in range(20, 260, 40)
            ]
        )


class Day10PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(10, "a")

    def _new_solver(self):
        return Day10PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return int(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 13140)]


if __name__ == "__main__":
    controller = Day10PartAController()
    controller.run()
