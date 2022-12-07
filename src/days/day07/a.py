from src.shared.controller import Controller
from src.days.day07.solver import AnswerType, Day07Solver, Directory
from src.shared.file_result import FileResult


class Day07PartASolver(Day07Solver):
    max_dir_size = 100000

    def _compute_answer(self, root: Directory) -> AnswerType:
        hits = root.recursive_search(lambda x: x.size <= self.max_dir_size)
        return sum([hit.size for hit in hits])


class Day07PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(7, "a")

    def _new_solver(self):
        return Day07PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 95437)]


if __name__ == "__main__":
    controller = Day07PartAController()
    controller.run()
