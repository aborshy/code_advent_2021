import os
import shutil
from datetime import date

"""
Example structure:
    ~Advent of Code 2015
        -- Day 1
            -testing_template.py
            -solution_template.py
            -input.txt
        -- Day 2
        -- etc.
    ~Advent of Code 2016
        -- Day 1
            -testing_template.py
            -solution_template.py
            -input.txt
        -- Day 2
        -- etc.
    ~etc.
"""


def create_structure():
    """
    Creates file tree of every Advent of Code day and year, from first year (2015) up to the current
    year in the directory ABOVE this one. Adds a quick and rough testing file to build pytests with, a solution file to
    go with the tests (can also be run on its own, without tests), and an empty input.txt file to copy AoC's
    file into. Comment out line 37 to create tree in current directory.
    :return: None
    """
    main_dir = [f"advent_of_code_{x}" for x in range(2015, date.today().year + 1)]
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


create_structure()
