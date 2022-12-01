from abc import ABC, abstractmethod
from src.shared.controller import Controller


class BaseTest(ABC):
    @abstractmethod
    def get_controller_a(self) -> Controller:
        ...

    @abstractmethod
    def get_controller_b(self) -> Controller:
        ...

    def test_part_a(self):
        controller = self.get_controller_a()
        tests = controller.sample_files()

        assert len(tests) > 0

        for (file, expected_result) in tests:
            result = controller.solve(file)
            assert result == expected_result

    def test_part_b(self):
        controller = self.get_controller_b()
        tests = controller.sample_files()

        assert len(tests) > 0

        for (file, expected_result) in tests:
            result = controller.solve(file)
            assert result == expected_result
