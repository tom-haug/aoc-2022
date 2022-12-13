from __future__ import annotations
from typing import Optional


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
