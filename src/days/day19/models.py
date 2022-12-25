from typing import Literal
from attr import dataclass


ResourceType = Literal["ore", "clay", "obsidian", "geode", "none"]


@dataclass(hash=True)
class Blueprint:
    id: int
    ore_ore_cost: int
    clay_ore_cost: int
    obsidian_ore_cost: int
    obsidian_clay_cost: int
    geode_ore_cost: int
    geode_obsidian_cost: int


@dataclass(hash=True)
class Resources:
    ore: int = 0
    clay: int = 0
    obsidian: int = 0
    geode: int = 0

    def __getitem__(self, key: ResourceType):
        match key:
            case "ore":
                return self.ore
            case "clay":
                return self.clay
            case "obsidian":
                return self.obsidian
            case "geode":
                return self.geode
            case _:
                return 0

    def __setitem__(self, key: ResourceType, value: int):
        match key:
            case "ore":
                self.ore = value
            case "clay":
                self.clay = value
            case "obsidian":
                self.obsidian = value
            case "geode":
                self.geode = value
            case _:
                ...


@dataclass(hash=True)
class GameState:
    turn: int
    resources: Resources
    robots: Resources

    def collect(self):
        self.resources.ore += self.robots.ore
        self.resources.clay += self.robots.clay
        self.resources.obsidian += self.robots.obsidian
        self.resources.geode += self.robots.geode

    def consume(self, blueprint: Blueprint, robot_type: ResourceType):
        match robot_type:
            case "ore":
                self.resources.ore -= blueprint.ore_ore_cost
            case "clay":
                self.resources.ore -= blueprint.clay_ore_cost
            case "obsidian":
                self.resources.ore -= blueprint.obsidian_ore_cost
                self.resources.clay -= blueprint.obsidian_clay_cost
            case "geode":
                self.resources.ore -= blueprint.geode_ore_cost
                self.resources.obsidian -= blueprint.geode_obsidian_cost
            case _:
                ...
