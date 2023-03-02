from fizzbuzz.fizz_buzz import FizzBuzz
import unittest


class TestFizzBuzz(unittest.TestCase):

    fizzbuzz: FizzBuzz

    def test_fizzbuzz(self) -> None:
        self.fizzbuzz = FizzBuzz()
        self.fizzbuzz.print_sequence(number=37)

