from src.shared.controller import Controller
from src.days.day23.solver import AnswerType, Day23Solver
from src.shared.file_result import FileResult


class Day23PartASolver(Day23Solver):
    def solve(self) -> AnswerType:
        for _ in range(10):
            self._turn()
        return self.__empty_area_count()

    def __empty_area_count(self) -> int:
        x_min = min(elf.x for elf in self.elves)
        x_max = max(elf.x for elf in self.elves)
        y_min = min(elf.y for elf in self.elves)
        y_max = max(elf.y for elf in self.elves)
        area = (x_max - x_min + 1) * (y_max - y_min + 1)
        return area - len(self.elves)


class Day23PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(23, "a")

    def _new_solver(self):
        return Day23PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 25), FileResult("sample02.txt", 110)]


if __name__ == "__main__":
    controller = Day23PartAController()
    controller.run()
