from __future__ import annotations
from abc import abstractproperty
from typing import Any
from src.days.day20.circular_linked_list import CircularLinkedList
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines


AnswerType = int


class Day20Solver(Solver[AnswerType]):
    working_list: CircularLinkedList

    def initialize(self, file_path: str, extra_params: dict[str, Any]):
        input = load_text_file_lines(file_path)
        values = [int(value) for value in input]
        self.working_list = CircularLinkedList(values[0])
        for value in values[1:]:
            self.working_list.add(value)

    def solve(self) -> AnswerType:
        for node in self.working_list.node_execution:
            node.value *= self._decryption_key
        for _ in range(self._mix_count):
            for node in self.working_list.node_execution:
                self.working_list.move(node, node.value)
        return self._calculate_answer()

    @abstractproperty
    def _decryption_key(self) -> int:
        ...

    @abstractproperty
    def _mix_count(self) -> int:
        ...

    def _calculate_answer(self) -> int:
        target_node = next(
            node for node in self.working_list.node_execution if node.value == 0
        )
        answer_parts = list[int]()
        for _ in range(3):
            for _ in range(1000):
                target_node = target_node.next
            answer_parts.append(target_node.value)
        return sum(answer_parts)
