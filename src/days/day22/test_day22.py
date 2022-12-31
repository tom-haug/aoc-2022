from src.days.day22.a import Day22PartAController
from src.days.day22.b import Day22PartBController
from src.days.day22.solver import AnswerType
from src.shared.base_test import BaseTest
from src.shared.controller import Controller


class TestDay22(BaseTest[AnswerType]):
    def _get_controller_a(self) -> Controller[AnswerType]:
        return Day22PartAController()

    def _get_controller_b(self) -> Controller[AnswerType]:
        return Day22PartBController()
