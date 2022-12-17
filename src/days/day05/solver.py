from abc import abstractmethod
from typing import Any
from attr import dataclass
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file
from collections import deque

AnswerType = str
Crate = str
CrateStack = deque[Crate]
GameSpace = list[CrateStack]


@dataclass
class Instruction:
    amount: int
    from_stack: int
    to_stack: int


class Day05Solver(Solver[AnswerType]):
    game_space: GameSpace
    instructions: list[Instruction]

    def initialize(self, file_path: str, extra_params: dict[str, Any]):
        input = load_text_file(file_path) or ""
        crates_section, instructions_section = input.split("\n\n")
        self.game_space = self.__load_game_space(crates_section)
        self.instructions = self.__load_instructions(instructions_section)

    def solve(self) -> AnswerType:
        for instr in self.instructions:
            self._perform_instr(instr)
        message = "".join([stack.pop() for stack in self.game_space])
        return message

    def __load_game_space(self, input: str) -> GameSpace:
        lines = list(reversed(input.split("\n")))[1:]
        num_stacks = (len(lines[0]) + 1) // 4
        stacks = [self.__load_stack(lines, stack) for stack in range(num_stacks)]
        return stacks

    def __load_stack(self, input: list[str], stack_idx: int) -> CrateStack:
        char_idx = (stack_idx * 4) + 1
        return deque([line[char_idx] for line in input if line[char_idx] != " "])

    def __load_instructions(self, input: str) -> list[Instruction]:
        return [self.__load_instruction(line) for line in input.strip().split("\n")]

    def __load_instruction(self, input: str) -> Instruction:
        parts = input.split(" ")
        return Instruction(int(parts[1]), int(parts[3]) - 1, int(parts[5]) - 1)

    @abstractmethod
    def _perform_instr(self, instr: Instruction):
        ...
