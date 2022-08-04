import re
from collections import Counter
from string import ascii_lowercase


class Part1:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """
        Santa needs help figuring out which strings in his text file are naughty or nice.

        A nice string is one with all of the following properties:

        It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
        It contains at least one letter that appears twice in a row,
        like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
        It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

        How many strings are nice?
        Args:
            file_lines: List of lines from input file

        Returns: Amount of nice lines

        """
        vowels = 'aeiou'
        double_letters = [x + x for x in ascii_lowercase]
        naughty_substrings = ['ab', 'cd', 'pq', 'xy']
        nice_lines = 0

        for x in file_lines:
            naughty = False
            has_vowel_amount = False
            has_double_letters = False
            count = Counter(x)
            pairs = set(re.findall('..', x) + re.findall('..', f" {x}"))
            vowel_count = 0

            for x in naughty_substrings:
                if x in pairs:
                    naughty = True
                    break
            for x in double_letters:
                if x in pairs:
                    has_double_letters = True
                    break
            for x in vowels:
                vowel_count += count[x]
                if vowel_count >= 3:
                    has_vowel_amount = True

            if has_double_letters and has_vowel_amount and not naughty:
                nice_lines += 1

        return nice_lines


class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """
        Realizing the error of his ways, Santa has switched to a better model of determining whether a string is
         naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

        Now, a nice string is one with all of the following properties:

        It contains a pair of any two letters that appears at least twice in the string without overlapping,
        like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
        It contains at least one letter which repeats with exactly one letter between them,
        like xyx, abcdefeghi (efe), or even aaa.

        Args:
            file_lines: List of lines from input file

        Returns:

        """

        return 0


with open("input.txt", "r") as file:
    f = file.read().splitlines()

print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
