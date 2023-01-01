from src.days.day23.a import Day23PartAController
from src.days.day23.b import Day23PartBController
from src.days.day23.solver import AnswerType
from src.shared.base_test import BaseTest
from src.shared.controller import Controller


class TestDay23(BaseTest[AnswerType]):
    def _get_controller_a(self) -> Controller[AnswerType]:
        return Day23PartAController()

    def _get_controller_b(self) -> Controller[AnswerType]:
        return Day23PartBController()
