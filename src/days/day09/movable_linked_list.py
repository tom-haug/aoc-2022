from __future__ import annotations
from typing import Optional

from src.shared.point import Point


class MovableLinkedList(Point):
    history: set[tuple[int, int]]
    next: Optional[MovableLinkedList]
    stop_adjactent: bool

    def __init__(
        self, num_segments: int, x: int = 0, y: int = 0, stop_adjactent: bool = False
    ):
        self.stop_adjactent = stop_adjactent
        self.history = set()
        if num_segments > 1:
            self.next = MovableLinkedList(num_segments - 1, x, y, True)
        else:
            self.next = None
        self.__update_location(x, y)

    @property
    def tail(self) -> MovableLinkedList:
        return self if self.next is None else self.next.tail

    def move(self, target_x: int, target_y: int):
        while (self.x, self.y) != (target_x, target_y):
            x_increment = move_increment(target_x - self.x)
            y_increment = move_increment(target_y - self.y)
            if self.stop_adjactent and (self.x + x_increment, self.y + y_increment) == (
                target_x,
                target_y,
            ):
                break
            self.__update_location(self.x + x_increment, self.y + y_increment)

    def __update_location(self, x: int, y: int):
        self.x = x
        self.y = y
        self.__log_history()
        self.__propigate()

    def __propigate(self):
        if self.next is not None:
            self.next.move(self.x, self.y)

    def __log_history(self):
        self.history.add((self.x, self.y))


def move_increment(value: int) -> int:
    return 1 if value >= 1 else -1 if value <= -1 else 0
