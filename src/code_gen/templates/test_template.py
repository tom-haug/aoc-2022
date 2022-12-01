TEST_TEMPLATE = """
from src.days.day{day_string}.a import Day{day_string}PartAController
from src.days.day{day_string}.b import Day{day_string}PartBController
from src.shared.base_test import BaseTest
from src.shared.controller import Controller


class TestDay{day_string}(BaseTest):
    def get_controller_a(self) -> Controller:
        return Day{day_string}PartAController()

    def get_controller_b(self) -> Controller:
        return Day{day_string}PartBController()
"""
