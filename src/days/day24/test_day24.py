from src.days.day24.a import Day24PartAController
from src.days.day24.b import Day24PartBController
from src.days.day24.solver import AnswerType
from src.shared.base_test import BaseTest
from src.shared.controller import Controller


class TestDay24(BaseTest[AnswerType]):
    def _get_controller_a(self) -> Controller[AnswerType]:
        return Day24PartAController()

    def _get_controller_b(self) -> Controller[AnswerType]:
        return Day24PartBController()
