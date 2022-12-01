from abc import ABC, abstractmethod
import argparse
from typing import Any
from aocd import submit

from src.shared.solver import Solver


class Controller(ABC):
    def __init__(self, year: int, day: int, part: str):
        self.year = year
        self.day = day
        self.part = part

    @abstractmethod
    def new_solver(self) -> Solver:
        ...

    @abstractmethod
    def sample_files(self) -> list[tuple[str, Any]]:
        ...

    @abstractmethod
    def file_path(self) -> str:
        ...

    def __run_test_inputs(self) -> None:
        samples = self.sample_files()

        if len(samples) == 0:
            raise Exception(
                f"No sample files setup. Add these to: {self.__class__.__name__}"
            )

        for (file_path, expected_result) in samples:
            result = self.solve(file_path)
            if result != expected_result:
                raise Exception(
                    f"Test Fail: Sample {file_path}, expecting: {expected_result}, actual: {result}"
                )
            print(f"Test Pass: File: {file_path}, result: {result}")

    def run(self) -> None:
        self.__run_test_inputs()

        result = self.solve(self.file_path())
        print(f"Result: {result}")
        self.try_submit(result)

    def solve(self, file_path: str) -> Any:
        solver = self.new_solver()
        solver.initialize(file_path)
        result = solver.solve()
        return result

    def try_submit(self, result: Any):
        args = create_parser().parse_args()
        do_submit = args.submit
        if do_submit:
            submit(result, part=self.part, day=self.day, year=self.year)


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Helper to bootstrap files for problems"
    )
    parser.add_argument(
        "-s", "--submit", action="store_true", help="Submit result if tests pass"
    )

    return parser
