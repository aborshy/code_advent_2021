import os
from datetime import date


def create_structure():
    """
    Creates file tree and placeholder of every Advent of Code day and year, from first year (2015) up to the current
    year in the current directory.
    :return: None
    """
    main_dir = [f"Advent of Code {x}" for x in range(2015, date.today().year + 1)]
    common_dir = [f"Day {x}" for x in range(1, 26)]

    for dir1 in main_dir:
        for dir2 in common_dir:
            try:
                os.makedirs(os.path.join(dir1, dir2))
            except OSError:
                pass
        with open(f'{dir1}/readme.txt', 'w') as f:
            f.write('Placeholder readme.')


create_structure()
