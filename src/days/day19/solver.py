from abc import abstractmethod, abstractproperty
import copy
from functools import cache
import re
from typing import Any
from src.days.day19.models import Blueprint, GameState, ResourceType, Resources
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines


AnswerType = int


class Day19Solver(Solver[AnswerType]):
    all_blueprints: list[Blueprint]

    @abstractproperty
    def _desired_blueprints(self) -> list[Blueprint]:
        ...

    @abstractproperty
    def _num_turns(self) -> int:
        ...

    @abstractproperty
    def _resource_buffer(self) -> float:
        ...

    def initialize(self, file_path: str, extra_params: dict[str, Any]):
        input = load_text_file_lines(file_path)
        self.all_blueprints = [parse_blueprint(line) for line in input]

    def solve(self) -> AnswerType:
        results = list[tuple[Blueprint, int]]()
        for blueprint in self._desired_blueprints:
            initial_state = GameState(0, Resources(), Resources(1))
            most_geodes = self.__turn(blueprint, initial_state)
            print(f"ID: {blueprint.id}, geodes:{most_geodes}")
            print(self.__turn.cache_info())
            self.__turn.cache_clear()
            results.append((blueprint, most_geodes))

        answer = self._calc_answer(results)
        return answer

    @cache
    def __turn(self, blueprint: Blueprint, in_state: GameState) -> int:
        new_turn = in_state.turn + 1
        if new_turn > self._num_turns:
            return in_state.resources.geode

        possible_actions = get_possible_robots(
            blueprint,
            in_state.resources,
            in_state.robots,
            self._num_turns - new_turn,
            self._resource_buffer,
        )
        max_geodes = 0

        if len(possible_actions) == 0:
            raise Exception("len(possible_actions) == 0")

        for robot_type in possible_actions:
            new_state = copy.deepcopy(in_state)
            new_state.turn = new_turn
            new_state.consume(blueprint, robot_type)
            new_state.collect()
            new_state.robots[robot_type] += 1
            ending_geodes = self.__turn(blueprint, new_state)
            if ending_geodes > max_geodes:
                max_geodes = ending_geodes

        return max_geodes

    @abstractmethod
    def _calc_answer(self, results: list[tuple[Blueprint, int]]) -> int:
        ...


def have_robots_to_make(robots: Resources, desired_robot: ResourceType) -> bool:
    match desired_robot:
        case "obsidian":
            return robots.clay > 0
        case "geode":
            return robots.obsidian > 0
        case _:
            return False


def get_possible_robots(
    blueprint: Blueprint,
    resources: Resources,
    robots: Resources,
    turns_left: int,
    resource_buffer: float,
) -> list[ResourceType]:
    possible_robots = list[ResourceType]()

    ore_capped = False
    if resources["ore"] >= blueprint.ore_ore_cost:
        if turns_left <= 1 or resources.ore >= (
            resource_buffer
            * max(
                blueprint.ore_ore_cost,
                blueprint.clay_ore_cost,
                blueprint.obsidian_ore_cost,
                blueprint.geode_ore_cost,
            )
        ):
            ore_capped = True
        else:
            possible_robots.append("ore")

    clay_capped = False
    if resources["ore"] >= blueprint.clay_ore_cost:
        if turns_left <= 1 or resources.clay >= (
            resource_buffer * blueprint.obsidian_clay_cost
        ):
            clay_capped = True
        else:
            possible_robots.append("clay")

    obsidian_capped = False
    if (
        resources["ore"] >= blueprint.obsidian_ore_cost
        and resources["clay"] >= blueprint.obsidian_clay_cost
    ):
        if turns_left == 0 or resources.obsidian >= (
            resource_buffer * blueprint.geode_obsidian_cost
        ):
            obsidian_capped = True
        else:
            possible_robots.append("obsidian")

    if (
        resources["ore"] >= blueprint.geode_ore_cost
        and resources["obsidian"] >= blueprint.geode_obsidian_cost
    ):
        possible_robots.append("geode")

    # do nothing action if we could be saving up to make something else
    if (
        ("ore" not in possible_robots and not ore_capped)
        or ("clay" not in possible_robots and not clay_capped)
        or (
            "obsidian" not in possible_robots
            and not obsidian_capped
            and have_robots_to_make(robots, "obsidian")
        )
        or ("geode" not in possible_robots and have_robots_to_make(robots, "geode"))
    ):
        possible_robots.append("none")

    if len(possible_robots) == 0:
        possible_robots.append("none")

    return possible_robots


def parse_blueprint(line: str) -> Blueprint:
    match = next(
        re.finditer(
            r"Blueprint\s(\d+):.*?(\d+)\sore.*?(\d+)\sore.*?(\d+)\sore.*?(\d+)\sclay.*?(\d+)\sore.*?(\d+)\sobsidian",
            line,
        )
    )
    return Blueprint(
        int(match.group(1)),
        int(match.group(2)),
        int(match.group(3)),
        int(match.group(4)),
        int(match.group(5)),
        int(match.group(6)),
        int(match.group(7)),
    )
