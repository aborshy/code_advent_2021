class Part1:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """
        You avoid the ropes, plunge into the river, and swim to shore.

        The Elves yell something about meeting back up with them upriver,
        but the river is too loud to tell exactly what they're saying.
        They finish crossing the bridge and disappear from view.

        Situations like this must be why the Elves prioritized getting the communication system on your handheld device
        working. You pull it out of your pack, but the amount of water slowly draining from a big crack in its screen
        tells you it probably won't be of much immediate use.

        Unless, that is, you can design a replacement for the device's video system!
        It seems to be some kind of cathode-ray tube screen and simple CPU that are both driven
        by a precise clock circuit. The clock circuit ticks at a constant rate; each tick is called a cycle.

        The interesting signal strengths can be determined as follows:

        During the 20th cycle, register X has the value 21, so the signal strength is 20 * 21 = 420.
        (The 20th cycle occurs in the middle of the second addx -1, so the value of register X is the
        starting value, 1, plus all the other addx values up to that point:
        1 + 15 - 11 + 6 - 3 + 5 - 1 - 8 + 13 + 4 = 21.)
        During the 60th cycle, register X has the value 19, so the signal strength is 60 * 19 = 1140.
        During the 100th cycle, register X has the value 18, so the signal strength is 100 * 18 = 1800.
        During the 140th cycle, register X has the value 21, so the signal strength is 140 * 21 = 2940.
        During the 180th cycle, register X has the value 16, so the signal strength is 180 * 16 = 2880.
        During the 220th cycle, register X has the value 18, so the signal strength is 220 * 18 = 3960.
        The sum of these signal strengths is


        Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles.
        What is the sum of these six signal strengths?
        Args:
            file_lines: List of lines from input file

        Returns:

        """
        clock_cycle = 1
        counter = 1
        output = 0
        for x in file_lines:
            line = x.split()

            try:
                val = int(line[1])
                adding = True
            except:
                # noop
                clock_cycle += 1
                continue

            if adding:
                addx_cycle = 0
                while addx_cycle < 2:
                    if clock_cycle in (20, 60, 100, 140, 180, 220):
                        output += val * clock_cycle
                        clock_cycle += 1
                        continue
                    clock_cycle += 1
                counter += val

                if clock_cycle in {20, 60, 100, 140, 180, 220}:
                    output += val * clock_cycle
                    clock_cycle += 2
                    continue

        return output


class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """

        Args:
            file_lines: List of lines from input file

        Returns:

        """
        return 0


with open("input.txt", "r") as file:
    f = file.read().splitlines()

print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
