from src.shared.controller import Controller
from src.days.day17.solver import AnswerType, Day17Solver
from src.shared.file_result import FileResult


class Day17PartASolver(Day17Solver):
    ROCK_COUNT = 2022

    def _should_stop(self) -> bool:
        return len(self.history) == self.ROCK_COUNT

    def _calculate_height(self) -> int:
        return self.history[-1] + 1


class Day17PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(17, "a")

    def _new_solver(self):
        return Day17PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 3068)]


if __name__ == "__main__":
    controller = Day17PartAController()
    controller.run()
