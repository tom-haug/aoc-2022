from src.shared.controller import Controller
from src.days.day21.solver import AnswerType, Day21Solver
from src.shared.file_result import FileResult


class Day21PartASolver(Day21Solver):
    def solve(self) -> AnswerType:
        root = next(x for x in self.monkeys if x.id == "root")
        return root.value


class Day21PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(21, "a")

    def _new_solver(self):
        return Day21PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 152)]


if __name__ == "__main__":
    controller = Day21PartAController()
    controller.run()
