import hashlib


class Part1:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """
        --- Day 4: The Ideal Stocking Stuffer ---
        Santa needs help mining some AdventCoins (very similar to bitcoins) to use as
        gifts for all the economically forward-thinking little girls and boys.

        To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes.
        The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal.
        To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that
        produces such a hash.
        Args:
            file_lines: List of lines from input file

        Returns: Number needed to add to str input to create an MD5 hash that starts with 5 zeroes

        """
        input_code = file_lines[0]

        def mine(in_code, i):
            while True:
                print(i)
                hashed = hashlib.md5(f"{in_code}{str(i)}".encode('utf-8')).hexdigest()
                if hashed[0:5] == '00000':
                    return i
                i += 1

        return mine(input_code, 0)


class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """
        Now find one that starts with six zeroes.

        Args:
            file_lines: List of lines from input file

        Returns: Number needed to add to str input to create an MD5 hash that starts with 6 zeroes

        """
        input_code = file_lines[0]

        def mine(in_code, i):
            while True:
                print(i)
                hashed = hashlib.md5(f"{in_code}{str(i)}".encode('utf-8')).hexdigest()
                if hashed[0:6] == '000000':
                    return i
                i += 1

        return mine(input_code, 0)


with open("input.txt", "r") as file:
    f = file.read().splitlines()

print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
