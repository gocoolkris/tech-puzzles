from luhncheck.luhn_checker import LuhnChecker
import unittest


class LuhnCheckerTest(unittest.TestCase):

    luhn_checker: LuhnChecker

    def setUp(self) -> None:
        self.luhn_checker = LuhnChecker()

    def test_edge_cases(self) -> None:
        assert not self.luhn_checker.is_valid("")
        assert not self.luhn_checker.is_valid("        ")

    def test_luhn_check_visa1(self) -> None:
        cc = "4222222222222"
        assert self.luhn_checker.is_valid(cc)

    def test_luhn_check_visa2(self) -> None:
        cc = "4111111111111111"
        assert self.luhn_checker.is_valid(cc)

    def test_luhn_check_visa3(self) -> None:
        cc = "4111113423411"
        assert not self.luhn_checker.is_valid(cc)

    def test_luhn_check_mastercard1(self) -> None:
        cc = "5555555555554444"
        assert self.luhn_checker.is_valid(cc)

    def test_luhn_check_mastercard2(self) -> None:
        cc = "5105105105105100"
        assert self.luhn_checker.is_valid(cc)

    def test_luhn_check_mastercard3(self) -> None:
        cc = "5105105103245100"
        assert not self.luhn_checker.is_valid(cc)

    def test_luhn_check_amex1(self) -> None:
        cc = "378282246310005"
        assert self.luhn_checker.is_valid(cc)

    def test_luhn_check_amex2(self) -> None:
        cc = "371449635398431"
        assert self.luhn_checker.is_valid(cc)

    def test_luhn_check_amex3(self) -> None:
        cc = "371876289831005"
        assert not self.luhn_checker.is_valid(cc)