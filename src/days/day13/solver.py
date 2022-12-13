from __future__ import annotations
from abc import abstractmethod
from typing import Optional
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file


AnswerType = int


class Packet:
    children: list[Packet | int]

    def __init__(self, input: str):
        input = input[1:-1]
        self.children = list()
        if len(input) == 0:
            return

        open_count = 0
        start_idx = 0
        child_is_packet: bool = False
        for idx, char in enumerate(input):
            match char:
                case "[":
                    open_count += 1
                    if open_count == 1:
                        child_is_packet = True
                case "]":
                    open_count -= 1
                case ",":
                    if open_count == 0:
                        if child_is_packet:
                            self.children.append(Packet(input[start_idx:idx]))
                            child_is_packet = False
                        else:
                            self.children.append(int(input[start_idx:idx]))
                        start_idx = idx + 1
                case _:
                    ...

        if child_is_packet:
            self.children.append(Packet(input[start_idx:]))
        else:
            self.children.append(int(input[start_idx:]))

    @property
    def is_simple(self):
        return len(self.children) == 1 and isinstance(self.children[0], int)

    @property
    def is_list(self):
        return len(self.children) > 1

    def __lt__(self, other: Packet) -> Optional[bool]:
        if self.is_simple and other.is_simple:
            if isinstance(self.children[0], int) and isinstance(other.children[0], int):
                if self.children[0] < other.children[0]:
                    return True
                elif self.children[0] > other.children[0]:
                    return False
                else:
                    return None

        # at least one is a list
        for idx, this_child in enumerate(self.children):
            if len(other.children) - 1 < idx:
                return False
            other_child = other.children[idx]

            if isinstance(this_child, int):
                this_child = Packet(f"[{this_child}]")
            if isinstance(other_child, int):
                other_child = Packet(f"[{other_child}]")
            child_result = this_child < other_child

            if child_result is not None:
                return child_result

        if len(self.children) < len(other.children):
            return True

        return None


class Day13Solver(Solver[AnswerType]):
    packet_pairs: list[tuple[Packet, Packet]]

    def initialize(self, file_path: str):
        input = load_text_file(file_path) or ""
        pairs = input.split("\n\n")
        self.packet_pairs = [self.__parse_packet_pair(pair) for pair in pairs]
        return

    def __parse_packet_pair(self, input: str) -> tuple[Packet, Packet]:
        pair_input = input.split("\n")
        return Packet(pair_input[0]), Packet(pair_input[1])

    @abstractmethod
    def solve(self) -> AnswerType:
        ...
