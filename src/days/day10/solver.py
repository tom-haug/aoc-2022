from __future__ import annotations
from abc import abstractmethod
from copy import copy
from enum import Enum
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines


AnswerType = int | str
Registers = dict[str, int]


class InstructionType(Enum):
    UNKNOWN = 0
    NOOP = 1
    ADDX = 2

    @classmethod
    def parse(cls, input: str) -> InstructionType:
        match input:
            case "noop":
                return cls.NOOP
            case "addx":
                return cls.ADDX
            case _:
                return cls.UNKNOWN


class Instruction:
    type: InstructionType
    value: int

    def __init__(self, input: str):
        parts = input.split(" ")
        self.type = InstructionType.parse(parts[0])
        self.value = int(parts[1]) if len(parts) > 1 else 0


class Processor:
    registers: Registers

    def __init__(self, *register_keys: str):
        self.registers = {}
        for key in register_keys:
            self.registers[key] = 1

    def execute(self, instr: Instruction) -> int:
        match instr.type:
            case InstructionType.NOOP:
                return 1
            case InstructionType.ADDX:
                self.registers["X"] += instr.value
                return 2
            case _:
                return 0


class Day10Solver(Solver[AnswerType]):
    instructions: list[Instruction]
    processor: Processor
    history: dict[int, Registers]

    def initialize(self, file_path: str):
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
