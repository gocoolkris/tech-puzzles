from typing import Optional

"""
What is the Luhn Algorithm? (Definition)
Luhn's algorithm calculates, from a number (or a sequence of digits), a check key (called checksum), this key is a digit
which is dependent on the others.

What is the Luhn Algorithm for?
Luhn makes it possible to check numbers (credit card, SIRET, etc.) thanks to its control key (a digit which makes
it possible to check the others digits). If a character is misread or badly written, then Luhn's algorithm will detect
this error.

Luhn is known because MasterCard, American Express (AMEX), Visa and all credit cards use it.

Example: 12345674 is a valid card number, 1234567 is the initial number and 4 is the checksum.

Example: If a user enter 13245674 (2 and 3 are switched), then the program calculates the luhn checksum for 1324567
and finds 5 instead of 4 expected, the number is invalid and so the code has been badly typed.

How to verify a number with Luhn? (Validity check)
The Luhn algorithm starts by the end of the number, from the last right digit to the first left digit. Multiplying by
2 all digits of even rank. If the double of a digit is equal or superior to 10, replace it by the sum of its digits.
Realize the sum
s of all digits found. The control digit
c is equal to c = ( 10 − ( s mod 10 )) mod 10.

Example 1: The number 853X, with X=0, the digit to calculate.
Take the digit 3, doubled, 3*2 = 6.
Takes the digit 5, not multiplied by 2
Take the 8, multiplies it by 2: 8*2=16 and 1+6=7 to get 7.
The sum is 6+5+7 = 18. As 18 modulo 10 = 8, one calculated (10 - 8) %10 = 2, 2 is the digit checksum control.
So 8532 is valid according to Luhn.

Example 2: The number 12345674
Going from right to left and ignoring control digit (4),
Double the digit 7 = 14, taking the value 5 (1+4)
Take the digit 6
Double the digit 5 = 10, taking 1 (1+0)
Take the digit 4
Double the digit 3 = 6
Take the digit 2
Double the digit 1 = 2
s = 26 (5+6+1+4+6+2+2)
c = (10 - (26 mod 10)) mod 10 = 4
"""


class LuhnChecker:
    """
    Class that represents the validation of a credit card for Luhn check.
    """

    @staticmethod
    def is_valid(credit_card_number: str) -> bool:
        """
        :param credit_card_number: the number to validate.
        :return: returns True if it passes Luhn check, False otherwise.
        """
        check_key = credit_card_number[-1]
        check_sum = LuhnChecker._check_sum(credit_card_number=credit_card_number)
        return int(check_key) == (10 - (check_sum % 10))

    @staticmethod
    def _check_sum(credit_card_number: str) -> int:
        cc_length = len(credit_card_number)
        check_sum = 0
        for index in range(cc_length):
            if (index) % 2 == 0:
                digit_value = int(credit_card_number[index]) * 2
                if digit_value >= 10:
                    digit_value = int(digit_value/10) + int(digit_value % 10)
            else:
                digit_value = int(credit_card_number[index])
            check_sum += digit_value


