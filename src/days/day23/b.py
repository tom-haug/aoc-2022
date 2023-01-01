from src.shared.controller import Controller
from src.days.day23.solver import AnswerType, Day23Solver
from src.shared.file_result import FileResult


class Day23PartBSolver(Day23Solver):
    def solve(self) -> AnswerType:
        round_count = 1
        while self._turn():
            round_count += 1
        return round_count


class Day23PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(23, "b")

    def _new_solver(self):
        return Day23PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 4), FileResult("sample02.txt", 20)]


if __name__ == "__main__":
    controller = Day23PartBController()
    controller.run()
