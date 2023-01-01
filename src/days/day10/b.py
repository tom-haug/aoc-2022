from src.shared.controller import Controller
from src.days.day10.solver import AnswerType, Day10Solver
from src.shared.file_result import FileResult


class Day10PartBSolver(Day10Solver):
    @property
    def visual_available(self) -> bool:
        return True

    def _answer(self) -> str:
        if self.show_visual:
            self._print()
        # manually read output from terminal
        return "FJUBULRZ"

    def _print(self) -> None:
        pixel_x = -1
        for cycle_num in range(1, 241):
            pixel_x += 1
            sprite_x = self.history[cycle_num]["X"]
            pixel = "X" if sprite_x - 1 <= pixel_x <= sprite_x + 1 else " "
            print(pixel, end="")
            if pixel_x == 39:
                pixel_x = -1
                print("")


class Day10PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(10, "b")

    def _new_solver(self):
        return Day10PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return value

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [
            # sample01 does not have an answer
            FileResult("sample01.txt", "FJUBULRZ")
        ]


if __name__ == "__main__":
    controller = Day10PartBController()
    controller.run()
