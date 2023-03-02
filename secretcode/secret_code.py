from typing import List

"""
Your neighbor Bob and you are good friends and he has sibling Alice who happens to
live across the other end of the globe. Alice and Bob usually communicate using plain-text
messages. Off lately, Bob suspects that his computer has been hacked as the ads he
sees in his web page are related to his browsing history in e-commerce site.

Alice and Bob used to communicate in cipher text in childhood to avoid suspicion from
their parents. They used to encode the following way,
a) Each vowel are replaced by the next occuring vowel in alphabetical order. The last vowel is
circular rotated. So, 'a' will be replaced by 'e'. 'u' will be replaced by 'a' of vowel
sequence (aeiou)
b) All the consonants are rotated by 8 letters in the alphabet sequence without vowels
(bcdfghjklmnpqrstvwxyz).
c) Case is preserved as it is.
c) All other characters are kept as it is.

Example 1: 'abcD1234'
'a' -> 'e'
'b' -> 'k'
'c' -> 'l'
'D' -> 'M'
and digits same as it is.
So 'abcD1234' becomes 'eklM1234'


Bob is unsure about the program he wrote and needs your expertise in writing it.

He also wants to test sample strings, so he requests you to add tests.

"""


class SecretCode:

    VOWEL_SEQUENCE = ['a', 'e', 'i', 'o', 'u']
    CONSONANTS_SEQUENCE = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                           'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

    def cipher(self, plain_text: str) -> str:
        if plain_text == "" or plain_text.isspace():
            return plain_text
        cipher_char_arr = []
        for char in plain_text:
            if char.isalpha():
                lower_case_char = char.lower()
                if lower_case_char in self.VOWEL_SEQUENCE:
                    new_char = self._cipher_char(char=char, sequence=self.VOWEL_SEQUENCE,
                                                 offset=1)
                    cipher_char_arr.append(new_char)
                else:
                    new_char = self._cipher_char(char=char, sequence=self.CONSONANTS_SEQUENCE,
                                                 offset=8)
                    cipher_char_arr.append(new_char)
            else:
                cipher_char_arr.append(char)
        return "".join(cipher_char_arr)

    @staticmethod
    def _cipher_char(char: str, sequence: List[str], offset: int) -> str:
        lower_case_char = char.lower()
        i = sequence.index(lower_case_char)
        new_char = sequence[(i+offset) % len(sequence)]
        if char.isupper():
            new_char = new_char.upper()
        return new_char

