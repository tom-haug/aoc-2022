from src.days.day02.a import Day02PartAController
from src.days.day02.b import Day02PartBController
from src.shared.base_test import BaseTest
from src.shared.controller import Controller


class TestDay02(BaseTest):
    def get_controller_a(self) -> Controller:
        return Day02PartAController()

    def get_controller_b(self) -> Controller:
        return Day02PartBController()
