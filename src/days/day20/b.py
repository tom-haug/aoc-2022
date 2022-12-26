from src.shared.controller import Controller
from src.days.day20.solver import AnswerType, Day20Solver
from src.shared.file_result import FileResult


class Day20PartBSolver(Day20Solver):
    @property
    def _decryption_key(self) -> int:
        return 811589153

    @property
    def _mix_count(self) -> int:
        return 10


class Day20PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(20, "b")

    def _new_solver(self):
        return Day20PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 1623178306)]


if __name__ == "__main__":
    controller = Day20PartBController()
    controller.run()
