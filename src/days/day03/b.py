from src.shared.controller import Controller
from src.days.day03.solver import AnswerType, Day03Solver
from src.shared.file_result import FileResult


class Day03PartBSolver(Day03Solver):
    def _get_shared_items(self) -> list[str]:
        shared_items: list[str] = []

        for group_num in range(0, len(self.rucksacks), 3):
            group = self.rucksacks[group_num : group_num + 3]
            a_items = group[0][0] + group[0][1]
            b_items = group[1][0] + group[1][1]
            c_items = group[2][0] + group[2][1]

            for item in a_items:
                if item in b_items and item in c_items:
                    shared_items.append(item)
                    break
        return shared_items


class Day03PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(2022, 3, "b")

    def _new_solver(self):
        return Day03PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 70)]


if __name__ == "__main__":
    controller = Day03PartBController()
    controller.run()
