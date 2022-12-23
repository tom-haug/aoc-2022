from src.days.day18.a import Day18PartAController
from src.days.day18.b import Day18PartBController
from src.days.day18.solver import AnswerType
from src.shared.base_test import BaseTest
from src.shared.controller import Controller


class TestDay18(BaseTest[AnswerType]):
    def _get_controller_a(self) -> Controller[AnswerType]:
        return Day18PartAController()

    def _get_controller_b(self) -> Controller[AnswerType]:
        return Day18PartBController()
