from abc import abstractproperty
from typing import Any
from src.days.day09.movable_linked_list import MovableLinkedList
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines


AnswerType = int
Instruction = tuple[str, int]


class Day09Solver(Solver[AnswerType]):
    instructions: list[Instruction]

    @abstractproperty
    def rope_length(self) -> int:
        ...

    def initialize(self, file_path: str, extra_params: dict[str, Any]):
        input = load_text_file_lines(file_path)
        self.instructions = [
            (line[0], int(line[1])) for line in [line.split(" ") for line in input]
        ]

    def solve(self) -> AnswerType:
        rope = MovableLinkedList(self.rope_length)
        for instr in self.instructions:
            match instr[0]:
                case "L":
                    rope.move(rope.x - instr[1], rope.y)
                case "R":
                    rope.move(rope.x + instr[1], rope.y)
                case "U":
                    rope.move(rope.x, rope.y - instr[1])
                case "D":
                    rope.move(rope.x, rope.y + instr[1])
        return len(rope.tail.history)
