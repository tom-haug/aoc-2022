from abc import ABC, abstractmethod, abstractproperty
from functools import cached_property
import math
import re
from typing import Literal
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines


AnswerType = int
Operator = Literal["+", "-", "*", "/", "="]


class Monkey(ABC):
    id: str

    @abstractproperty
    def value(self) -> int:
        ...

    @abstractmethod
    def depends_on(self, id: str) -> bool:
        ...


class ValueMonkey(Monkey):
    _value: int

    def __init__(self, id: str, value: int):
        self.id = id
        self._value = value

    @property
    def value(self) -> int:
        return self._value

    def depends_on(self, id: str) -> bool:
        return self.id == id


class OperatorMonkey(Monkey):
    left_monkey: Monkey
    right_monkey: Monkey
    operator: Operator

    def __init__(
        self, id: str, left_monkey_id: str, right_monkey_id: str, operator: Operator
    ):
        self.id = id
        self.left_monkey = ValueMonkey(left_monkey_id, 0)
        self.right_monkey = ValueMonkey(right_monkey_id, 0)
        self.operator = operator

    @cached_property
    def value(self) -> int:
        left_value = self.left_monkey.value
        right_value = self.right_monkey.value
        return self.operate(left_value, right_value)

    def operate(self, a: int, b: int) -> int:
        match self.operator:
            case "+":
                return a + b
            case "-":
                return a - b
            case "*":
                return a * b
            case "/":
                return a // b
            case "=":
                return 1 if a == b else 0

    def solve_for_left(self, right: int, result: int) -> int:
        match self.operator:
            case "+":
                return result - right
            case "-":
                return result + right
            case "*":
                return result // right
            case "/":
                return result * right
            case "=":
                return right

    def solve_for_right(self, left: int, result: int) -> int:
        match self.operator:
            case "+":
                return result - left
            case "-":
                return -1 * (result - left)
            case "*":
                return result // left
            case "/":
                return math.floor(math.pow(result // left, -1))
            case "=":
                return left

    def depends_on(self, target_id: str) -> bool:
        return self.left_monkey.depends_on(target_id) or self.right_monkey.depends_on(
            target_id
        )

    def solve_for(self, target_id: str, outcome: int = -1) -> int:
        if self.left_monkey.depends_on(target_id):
            right_operand = self.right_monkey.value
            left_operand = self.solve_for_left(right_operand, outcome)
            if self.left_monkey.id == target_id:
                return left_operand
            else:
                if not isinstance(self.left_monkey, OperatorMonkey):
                    raise Exception("left monkey must be OperatorMonkey")
                return self.left_monkey.solve_for(target_id, left_operand)
        else:
            left_operand = self.left_monkey.value
            right_operand = self.solve_for_right(left_operand, outcome)
            if self.right_monkey.id == target_id:
                return right_operand
            else:
                if not isinstance(self.right_monkey, OperatorMonkey):
                    raise Exception("right monkey must be OperatorMonkey")
                return self.right_monkey.solve_for(target_id, right_operand)


class Day21Solver(Solver[AnswerType]):
    monkeys: list[Monkey]

    def initialize(self, file_path: str):
        input = load_text_file_lines(file_path)
        self.monkeys = [parse_monkey(line) for line in input]
        link_monkeys(self.monkeys)

    @abstractmethod
    def solve(self) -> AnswerType:
        ...


def parse_operator(input: str) -> Operator:
    match input:
        case "+":
            return "+"
        case "-":
            return "-"
        case "*":
            return "*"
        case "/":
            return "/"
        case "=":
            return "="
        case _:
            raise Exception(f"Unknown operator: {input}")


def parse_monkey(input: str) -> Monkey:
    value_match = re.search(r"(\w+):\s(\d+)", input)
    operator_match = re.search(r"(\w+):\s(\w+)\s([+\-\/*])\s(\w+)", input)

    if operator_match is not None:
        return OperatorMonkey(
            operator_match.group(1),
            operator_match.group(2),
            operator_match.group(4),
            parse_operator(operator_match.group(3)),
        )
    elif value_match is not None:
        return ValueMonkey(value_match.group(1), int(value_match.group(2)))

    raise Exception(f"Cannot parse: {input}")


def link_monkeys(monkeys: list[Monkey]) -> None:
    for monkey in monkeys:
        if isinstance(monkey, OperatorMonkey):
            monkey.left_monkey = next(
                x for x in monkeys if x.id == monkey.left_monkey.id
            )
            monkey.right_monkey = next(
                x for x in monkeys if x.id == monkey.right_monkey.id
            )
