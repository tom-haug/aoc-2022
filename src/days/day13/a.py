from src.shared.controller import Controller
from src.days.day13.solver import AnswerType, Day13Solver
from src.shared.file_result import FileResult


class Day13PartASolver(Day13Solver):
    def solve(self) -> AnswerType:
        hits = [idx + 1 for idx, (a, b) in enumerate(self.packet_pairs) if a < b]
        return sum(hits)


class Day13PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(13, "a")

    def _new_solver(self):
        return Day13PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 13)]


if __name__ == "__main__":
    controller = Day13PartAController()
    controller.run()
