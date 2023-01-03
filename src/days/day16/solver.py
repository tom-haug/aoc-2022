from __future__ import annotations
from abc import abstractproperty
from enum import StrEnum
from dataclasses import dataclass
from functools import cached_property
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines
from astar import AStar


AnswerType = int


class StartingLocation(StrEnum):
    AA = "AA"
    AAA = "AAA"


@dataclass(frozen=True, eq=True)
class Player:
    dest_valve_id: str
    arrival: int


@dataclass(frozen=True, eq=True)
class StateKey:
    players: frozenset[Player]
    remaining: frozenset[str]


@dataclass(frozen=True, eq=True)
class Valve:
    id: str
    flow_rate: int
    connection_ids: list[str]
    connections: list[Valve]

    def __hash__(self):
        return hash(self.id)


class ValvePathFinder(AStar):
    width: int
    height: int

    def heuristic_cost_estimate(self, current: Valve, goal: Valve) -> float:
        return 1

    def distance_between(self, n1, n2) -> float:
        return 1

    def neighbors(self, node: Valve) -> list[Valve]:
        return node.connections


class Day16Solver(Solver[AnswerType]):
    data: list[str]
    valves: dict[str, Valve]
    visited: dict[StateKey, int]
    distance_between_valves: dict[tuple[str, str], int]
    current_best: int

    @cached_property
    def flowing_valves(self):
        return [valve[1] for valve in self.valves.items() if valve[1].flow_rate > 0]

    @abstractproperty
    def _players(self) -> list[Player]:
        ...

    def initialize(self, file_path: str):
        input = load_text_file_lines(file_path)
        self.valves = {
            valve.id: valve for valve in [parse_valve(line) for line in input]
        }
        self.__add_second_starting_valve()
        self.__wire_up_connections()
        self.__find_distance_between_valves()

    def __add_second_starting_valve(self):
        """
        players cannot occupy the same location (stored in a frozenset),
        so this allows them to start at different spots
        """
        orig = self.valves[StartingLocation.AA]
        valve = Valve(
            StartingLocation.AAA, orig.flow_rate, orig.connection_ids, orig.connections
        )
        self.valves[StartingLocation.AAA] = valve

    def __wire_up_connections(self):
        for valve_id in self.valves:
            valve = self.valves[valve_id]
            for connection_id in valve.connection_ids:
                connection = next(
                    filter(lambda x: x[1].id == connection_id, self.valves.items())
                )
                valve.connections.append(connection[1])

    def __find_distance_between_valves(self):
        self.distance_between_valves = dict()
        path_finder = ValvePathFinder()
        starting = [
            valve[1]
            for valve in self.valves.items()
            if valve[0] in [StartingLocation.AA, StartingLocation.AAA]
        ]
        valves_to_connect = starting + self.flowing_valves
        for a_idx, a in enumerate(valves_to_connect):
            for b in valves_to_connect[a_idx + 1 :]:
                path = path_finder.astar(a, b)
                if path is not None:
                    dist = len(list(path)) - 1
                    self.distance_between_valves[(b.id, a.id)] = dist
                    self.distance_between_valves[(a.id, b.id)] = dist

    def solve(self) -> AnswerType:
        self.visited = dict()
        self.current_best = 0
        remaining = frozenset(valve.id for valve in self.flowing_valves)
        max_flow = self._max_downstream_flow(
            StateKey(frozenset(self._players), remaining), 0
        )
        return max_flow

    def _max_downstream_flow(self, state: StateKey, prev_flow: int) -> int:
        players = state.players
        remaining = state.remaining

        # Performance Optimization - cache states we've already visited
        if state in self.visited:
            return self.visited[state]

        # Keep track of the best outcome to short-circuit other paths
        if len(players) == 0 or all(player.arrival <= 1 for player in players):
            if prev_flow > self.current_best:
                self.current_best = prev_flow
            return 0

        # find player(s) that need to act next
        max_arrival = max(player.arrival for player in players)
        next_acting_players = [
            player for player in players if player.arrival == max_arrival
        ]

        max_downstream = 0
        for next_acting_player in next_acting_players:
            # generate all future flow now for the valve that is opening
            cur_flow = (
                next_acting_player.arrival
                * self.valves[next_acting_player.dest_valve_id].flow_rate
            )
            total_flow = prev_flow + cur_flow

            # Performance Optimization - short cirtuit if opening all remaining valves this turn would not even be enough
            best_possible = total_flow
            for valve in remaining:
                best_possible += self.valves[valve].flow_rate * (
                    next_acting_player.arrival
                )
            for other_player in players:
                if other_player != next_acting_player:
                    best_possible += self.valves[
                        other_player.dest_valve_id
                    ].flow_rate * (next_acting_player.arrival)
            if best_possible < self.current_best:
                return 0

            # no more valves left to open, but remaining players need to finish out their actions
            if len(remaining) == 0:
                next_players = [
                    other for other in players if other != next_acting_player
                ]
                downstream_flow = self._max_downstream_flow(
                    StateKey(
                        frozenset({player for player in next_players}), frozenset()
                    ),
                    total_flow,
                )
                downstream_flow += cur_flow
                if downstream_flow > max_downstream:
                    max_downstream = downstream_flow

            # try visiting each remaining valve
            for next_target in remaining:
                dist = self.distance_between_valves[
                    next_acting_player.dest_valve_id, next_target
                ]
                next_arrival = next_acting_player.arrival - dist - 1
                check_remaining = frozenset(
                    target for target in remaining if target != next_target
                )
                next_players = [
                    other for other in players if other != next_acting_player
                ]
                next_players.append(Player(next_target, next_arrival))
                downstream_flow = self._max_downstream_flow(
                    StateKey(
                        frozenset({player for player in next_players}), check_remaining
                    ),
                    total_flow,
                )
                downstream_flow += cur_flow
                if downstream_flow > max_downstream:
                    max_downstream = downstream_flow

        self.visited[state] = max_downstream
        return max_downstream


def parse_valve(input: str) -> Valve:
    parts = input.split("; ")
    id = parts[0][6:8]
    flow_rate = parts[0][23:]
    connections = parts[1][22:].strip().split(", ")
    return Valve(id, int(flow_rate), connections, [])
