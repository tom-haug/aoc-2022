from __future__ import annotations
from abc import abstractmethod
from src.days.day13.packet import Packet
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file


AnswerType = int


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
