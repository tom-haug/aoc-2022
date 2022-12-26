from src.days.day21.a import Day21PartAController
from src.days.day21.b import Day21PartBController
from src.days.day21.solver import AnswerType
from src.shared.base_test import BaseTest
from src.shared.controller import Controller


class TestDay21(BaseTest[AnswerType]):
    def _get_controller_a(self) -> Controller[AnswerType]:
        return Day21PartAController()

    def _get_controller_b(self) -> Controller[AnswerType]:
        return Day21PartBController()
