from src.shared.controller import Controller
from src.days.day07.solver import AnswerType, Day07Solver, Directory
from src.shared.file_result import FileResult


class Day07PartBSolver(Day07Solver):
    max_root_size = 40000000

    def _compute_answer(self, root: Directory) -> AnswerType:
        target_size = root.size - self.max_root_size
        matches = root.recursive_search(lambda x: x.size >= target_size)
        return sorted(matches, key=lambda x: x.size)[0].size


class Day07PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(7, "b")

    def _new_solver(self):
        return Day07PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 24933642)]


if __name__ == "__main__":
    controller = Day07PartBController()
    controller.run()
