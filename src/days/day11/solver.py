from abc import abstractmethod, abstractproperty
import operator
from queue import Queue
from typing import Callable
from attr import dataclass
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file


AnswerType = int


@dataclass
class Monkey:
    items: Queue[int]
    operator: Callable[[int, int], int]
    operation_value: str
    test_divisible_by: int
    test_true_monkey: int
    test_false_monkey: int
    inspection_count: int

    def produce_item(self) -> int:
        item = self.items.get()
        operation_value = (
            item if self.operation_value == "old" else int(self.operation_value)
        )
        self.inspection_count += 1
        return self.operator(item, operation_value)

    def get_throw_target(self, item: int) -> int:
        return (
            self.test_true_monkey
            if item % self.test_divisible_by == 0
            else self.test_false_monkey
        )


class Day11Solver(Solver[AnswerType]):
    monkeys: dict[int, Monkey]

    def initialize(self, file_path: str):
        input = load_text_file(file_path) or ""
        self._pre_parse(input)
        monkey_sections = input.split("\n\n")
        self.monkeys = {}
        for idx, section in enumerate(monkey_sections):
            self.monkeys[idx] = self.__parse_monkey(section)

    def __parse_monkey(self, section: str) -> Monkey:
        lines = section.split("\n")
        items = Queue[int]()
        for item in lines[1][18:].split(", "):
            items.put(int(item))
        op: Callable
        match lines[2][23:24]:
            case "+":
                op = operator.add
            case "-":
                op = operator.sub
            case "*":
                op = operator.mul
            case _:
                op = operator.floordiv
        operation_value = lines[2][25:]
        test_divisible_by = int(lines[3][21:])
        test_true_monkey = int(lines[4][29:])
        test_false_monkey = int(lines[5][30:])
        return Monkey(
            items,
            self._monkey_operation(op),
            operation_value,
            test_divisible_by,
            test_true_monkey,
            test_false_monkey,
            0,
        )

    def solve(self) -> AnswerType:
        for _ in range(self._num_rounds):
            for monkey_idx in range(len(self.monkeys)):
                monkey = self.monkeys[monkey_idx]
                while not monkey.items.empty():
                    item = monkey.produce_item()
                    target_monkey = monkey.get_throw_target(item)
                    self.monkeys[target_monkey].items.put(item)
        return self.__calculate_result()

    def __calculate_result(self):
        first, second, *_ = sorted(
            list(self.monkeys.items()),
            key=lambda x: x[1].inspection_count,
            reverse=True,
        )
        result = first[1].inspection_count * second[1].inspection_count
        return result

    @abstractproperty
    def _num_rounds(self) -> int:
        ...

    def _pre_parse(self, input: str) -> None:
        ...

    @abstractmethod
    def _monkey_operation(
        self, operator: Callable[[int, int], int]
    ) -> Callable[[int, int], int]:
        ...
