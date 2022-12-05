from src.shared.controller import Controller
from src.days.day05.solver import AnswerType, Day05Solver, Instruction
from src.shared.file_result import FileResult


class Day05PartASolver(Day05Solver):
    def _perform_instr(self, instr: Instruction):
        for _ in range(instr.amount):
            self.game_space[instr.to_stack].append(
                self.game_space[instr.from_stack].pop()
            )


class Day05PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(5, "a")

    def _new_solver(self):
        return Day05PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", "CMZ")]


if __name__ == "__main__":
    controller = Day05PartAController()
    controller.run()
