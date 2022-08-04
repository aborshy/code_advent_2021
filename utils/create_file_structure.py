import os
import shutil
from datetime import date
import time

"""
Example structure:
    ~advent_of_code_2015
        -- day_1
            -tests.py
            -solution.py
            -input.txt
        -- day_2
        -- etc.
    ~advent_of_code_2016
        -- day_1
            -tests.py
            -solution.py
            -input.txt
        -- day_2
        -- etc.
    ~etc.
"""


def input_years():
    """
    Prompts user to input years desired to generate.
    Returns: None
    """
    print("Welcome to AoC file tree generator!\n")
    while True:
        try:
            start_year = int(input("From which year would you like to generate files? (AoC started in 2015!)\n"))
        except ValueError:
            print("Not a valid year.")
            continue
        if start_year < 2015:
            print("AoC didn't start then!")
        else:
            print(f"Accepted {start_year}.\n")
            break

    while True:
        try:
            end_year = int(input(f"Up to which year would you like to generate files?"
                                 f" (It's currently {date.today().year}!)\n"))
        except ValueError:
            print("Not a valid year.")
            continue
        if end_year > date.today().year:
            print("Please enter up to the current year.")
        else:
            print(f"Accepted {end_year}.\n")
            break

    return start_year, end_year


def create_structure(start, end):
    """
    Creates file tree of every Advent of Code day and year, from first year (2015) up to the current
    year in the directory ABOVE this one. Adds a quick and rough testing file to build pytests with, a solution file to
    go with the tests (can also be run on its own, without tests), and an empty input.txt file to copy AoC's
    file into. Comment out line 37 to create tree in current directory.
    :return: None
    """
    main_dir = [f"advent_of_code_{x}" for x in range(start, end + 1)]
    common_dir = [f"day_{x:02d}" for x in range(1, 26)]

    # makes it so script can be run from utils folder and populate main dir, comment out to do in current dir
    os.chdir('../')

    try:
        os.makedirs(os.getcwd())
    except OSError:
        pass

    for dir1 in main_dir:
        for dir2 in common_dir:
            try:
                os.makedirs(os.path.join(dir1, dir2))
                shutil.copy('utils/solution_template.py', f"{dir1}/{dir2}/solution.py")
                shutil.copy('utils/testing_template.py', f"{dir1}/{dir2}/tests.py")
                with open(f'{dir1}/{dir2}/input.txt', 'w') as f:
                    f.write('')
            except OSError:
                print(f"Passing over {dir1}/{dir2} as path is currently occupied.")
                continue
        with open(f'{dir1}/readme.txt', 'w') as f:
            f.write('Placeholder readme! Please change me!')
        print(f"Created {dir1}")


s, e = input_years()
print(f"Generating trees between {s} and {e}...")
time.sleep(1)
create_structure(s, e)
print("Finished, exiting...")
time.sleep(1)
