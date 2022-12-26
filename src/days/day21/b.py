from src.shared.controller import Controller
from src.days.day21.solver import AnswerType, Day21Solver, OperatorMonkey
from src.shared.file_result import FileResult


class Day21PartBSolver(Day21Solver):
    def solve(self) -> AnswerType:
        root = next(x for x in self.monkeys if x.id == "root")
        if not isinstance(root, OperatorMonkey):
            raise Exception("root must be an OperatorMonkey")
        root.operator = "="
        return root.solve_for("humn")


class Day21PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(21, "b")

    def _new_solver(self):
        return Day21PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 301)]


if __name__ == "__main__":
    controller = Day21PartBController()
    controller.run()
