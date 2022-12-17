from __future__ import annotations
from abc import abstractmethod
from typing import Any, Callable, Optional
from attr import dataclass
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file


AnswerType = int


@dataclass
class File:
    name: str
    size: int


class Directory:
    name: str
    files: list[File]
    directories: list[Directory]
    parent: Optional[Directory]

    def __init__(self, name: str, parent: Optional[Directory] = None):
        self.name = name
        self.parent = parent
        self.files = []
        self.directories = []

    @property
    def size(self) -> int:
        files_size = sum(child.size for child in self.files)
        directories_size = sum(child.size for child in self.directories)
        return files_size + directories_size

    def recursive_search(self, compare: Callable[[Directory], bool]) -> list[Directory]:
        hits = [
            hit for child in self.directories for hit in child.recursive_search(compare)
        ]
        if compare(self):
            hits.append(self)
        return hits


class Shell:
    root: Directory
    pwd: Directory

    def __init__(self, root: Directory):
        self.root = root
        self.pwd = root

    def execute(self, command: str):
        command_lines = command.strip().split("\n")
        command_type, *args = command_lines[0].split(" ")
        match command_type:
            case "cd":
                self.cd(args[0])
            case "ls":
                self.ls(command_lines[1:])

    def cd(self, dir: str):
        match dir:
            case "/":
                self.pwd = self.root
            case "..":
                self.pwd = self.pwd.parent if self.pwd.parent is not None else self.pwd
            case _:
                self.pwd = next(x for x in self.pwd.directories if x.name == dir)

    def ls(self, results: list[str]) -> None:
        for result in results:
            parts = result.split(" ")
            match parts[0]:
                case "dir":
                    self.pwd.directories.append(Directory(parts[1], self.pwd))
                case _:
                    self.pwd.files.append(File(parts[1], int(parts[0])))


class Day07Solver(Solver[AnswerType]):
    commands: list[str]

    def initialize(self, file_path: str, extra_params: dict[str, Any]):
        input = load_text_file(file_path) or ""
        self.commands = input.split("$ ")

    def solve(self) -> AnswerType:
        root = Directory("/", None)
        shell = Shell(root)
        for command in self.commands:
            shell.execute(command)
        return self._compute_answer(root)

    @abstractmethod
    def _compute_answer(self, root: Directory) -> AnswerType:
        ...
