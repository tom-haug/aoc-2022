from __future__ import annotations


class Node:
    value: int
    next: Node
    prev: Node

    def __init__(self, value: int):
        self.value = value
        self.next = self
        self.prev = self


class CircularLinkedList:
    head: Node
    node_execution: list[Node]

    @property
    def tail(self) -> Node:
        return self.head.prev

    def __init__(self, head_value: int):
        self.head = Node(head_value)
        self.node_execution = [self.head]

    def add(self, value: int):
        node = Node(value)
        self.node_execution.append(node)
        self.__insert(node, self.tail)

    def move(self, node: Node, amount: int):
        if amount == 0:
            return

        # what way are we going?
        forward = amount > 0

        # walk the first step before the item is removed
        # as we loose the spot the current node is at
        new_prev = node.next if forward else node.prev.prev

        # take it out of the current spot
        self.__remove(node)

        # get step remainer after circling the list and account for
        # the current node being removed
        amount = (abs(amount) % (len(self.node_execution) - 1)) - 1

        # step the remainder
        for _ in range(amount):
            new_prev = new_prev.next if forward else new_prev.prev

        # insert the node back in the new spot
        self.__insert(node, new_prev)

    def __remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = node
        node.prev = node

    def __insert(self, node: Node, after: Node):
        node.next = after.next
        node.prev = after
        after_next = after.next
        after.next = node
        after_next.prev = node
