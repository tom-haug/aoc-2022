from src.shared.controller import Controller
from src.days.day13.solver import AnswerType, Day13Solver, Packet
from src.shared.file_result import FileResult


class Day13PartBSolver(Day13Solver):
    def solve(self) -> AnswerType:
        packets = [packet for pair in self.packet_pairs for packet in pair]
        divider_a = Packet("[[2]]")
        divider_b = Packet("[[6]]")
        packets.append(divider_a)
        packets.append(divider_b)
        packets.sort()
        decoder_key = (packets.index(divider_a) + 1) * (packets.index(divider_b) + 1)
        return decoder_key


class Day13PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(13, "b")

    def _new_solver(self):
        return Day13PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 140)]


if __name__ == "__main__":
    controller = Day13PartBController()
    controller.run()
