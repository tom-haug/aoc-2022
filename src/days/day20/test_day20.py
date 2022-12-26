from src.days.day20.a import Day20PartAController
from src.days.day20.b import Day20PartBController
from src.days.day20.solver import AnswerType
from src.shared.base_test import BaseTest
from src.shared.controller import Controller


class TestDay20(BaseTest[AnswerType]):
    def _get_controller_a(self) -> Controller[AnswerType]:
        return Day20PartAController()

    def _get_controller_b(self) -> Controller[AnswerType]:
        return Day20PartBController()
