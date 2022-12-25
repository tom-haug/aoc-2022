from src.days.day19.a import Day19PartAController
from src.days.day19.b import Day19PartBController
from src.days.day19.solver import AnswerType
from src.shared.base_test import BaseTest
from src.shared.controller import Controller


class TestDay19(BaseTest[AnswerType]):
    def _get_controller_a(self) -> Controller[AnswerType]:
        return Day19PartAController()

    def _get_controller_b(self) -> Controller[AnswerType]:
        return Day19PartBController()
