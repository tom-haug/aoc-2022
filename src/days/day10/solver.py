from __future__ import annotations
from abc import abstractmethod
from copy import copy
from typing import Any
from src.shared.computer import Instruction, Processor, Registers
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines


AnswerType = int | str


class Day10Solver(Solver[AnswerType]):
    instructions: list[Instruction]
    processor: Processor
    history: dict[int, Registers]

    def initialize(self, file_path: str, extra_params: dict[str, Any]):
        input = load_text_file_lines(file_path)
        self.instructions = [Instruction(line) for line in input]
        self.processor = Processor("X")
        self.history = {}

    def solve(self) -> AnswerType:
        self._execute_program()
        return self._answer()

    def _execute_program(self):
        cycle = 1
        for instr in self.instructions:
            initial_registers = copy(self.processor.registers)
            instr_cycles = self.processor.execute(instr)
            for _ in range(instr_cycles):
                self.history[cycle] = initial_registers
                cycle += 1

    @abstractmethod
    def _answer(self) -> AnswerType:
        ...
