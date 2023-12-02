class Part1:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """
        You can hear birds chirping and raindrops hitting leaves as the expedition proceeds. Occasionally,
        you can even hear much louder sounds in the distance; how big do the animals get out here, anyway?

        The device the Elves gave you has problems with more than just its
        communication system. You try to run a system update:

        $ system-update --please --pretty-please-with-sugar-on-top
        Error: No space left on device
        Perhaps you can delete some files to make space for the update?

        The filesystem consists of a tree of files (plain data) and directories (which can contain other directories or
        files). The outermost directory is called /. You can navigate around the filesystem, moving into or out of
        directories and listing the contents of the directory you're currently in.

        Within the terminal output, lines that begin with $ are commands you executed,
        very much like some modern computers:

        cd means change directory. This changes which directory is the current directory, but the specific result
        depends on the argument:
        cd x moves in one level: it looks in the current directory for the directory named x and makes it the current
        directory.
        cd .. moves out one level: it finds the directory that contains the current directory, then makes that directory
        the current directory.
        cd / switches the current directory to the outermost directory, /.
        ls means list. It prints out all the files and directories immediately contained by the current directory:
        123 abc means that the current directory contains a file named abc with size 123.
        dir xyz means that the current directory contains a directory named xyz.

        Since the disk is full, your first step should probably be to find directories that are good candidates for
        deletion. To do this, you need to determine the total size of each directory. The total size of a directory is
        the sum of the sizes of the files it contains, directly or indirectly. (Directories themselves do not count as
        having any intrinsic size.)

        The total sizes of the directories above can be found as follows:

        The total size of directory e is 584 because it contains a single file i of size 584 and no other directories.
        The directory a has total size 94853 because it contains files f (size 29116), g (size 2557), and h.lst
        (size 62596), plus file i indirectly (a contains e which contains i).
        Directory d has total size 24933642.
        As the outermost directory, / contains every file. Its total size is 48381165, the sum of the size of every
        file.
        To begin, find all the directories with a total size of at most 100000, then calculate the sum of their
        total sizes. In the example above, these directories are a and e; the sum of their total sizes is
        95437 (94853 + 584). (As in this example, this process can count files more than once!)

        Find all the directories with a total size of at most 100000.

        What is the sum of the total sizes of those directories?

        Args:
            file_lines: List of lines from input file

        Returns:

        """

        class Filesystem:
            def __init__(self, root_name):
                self.files = []
                self.folders = []
                self.root = self.Folder(root_name)
                self.folders.append(self.root)
                self.pwd = self.root

            class Folder:
                def __init__(self, name, parent=None):
                    self.name = name
                    self.parent = parent
                    self.children = []
                    self.size = None

                def add_child(self, child):
                    self.children.append(child)

                def get_size(self):
                    if self.size is None:
                        self.size = sum([child.get_size() for child in self.children])
                        return self.size
                    else:
                        return self.size

            class File:
                def __init__(self, name: str, size: int, parent):
                    self.parent = parent
                    self.size = size
                    self.name = name

                def get_size(self):
                    return self.size

            def add_folder(self, new_folder_name: str):
                new_folder = self.Folder(new_folder_name, self.pwd)
                self.folders.append(new_folder)
                self.pwd.add_child(new_folder)

            def add_file(self, file_name, file_size):
                new_file = self.File(file_name, file_size, self.pwd)
                self.pwd.add_child(new_file)
                self.files.append(new_file)

            def nav_down(self, down_folder_name: str):
                for child in self.pwd.children:
                    if child.name == down_folder_name:
                        self.pwd = child

            def nav_up(self):
                self.pwd = self.pwd.parent

        def day07(file_lines, delete_dir=False):
            with open('input.txt') as fin:
                lines = fin.readlines()

            filesystem = Filesystem('/')
            for line in lines[2:]:
                if line[:3] == 'dir':
                    filesystem.add_folder(line.split()[-1])
                elif line[0].isdigit():
                    filesystem.add_file(line.split()[1], int(line.split()[0]))
                elif line.strip() == '$ cd ..':
                    filesystem.nav_up()
                elif line[:4] == '$ cd':
                    filesystem.nav_down(line.split()[-1])
                else:
                    pass

            if not delete_dir:
                total = 0
                for folder in filesystem.folders:
                    if folder.get_size() <= 100000:
                        total += folder.get_size()

                return total
            else:
                min_delete = filesystem.root.get_size() - 40000000
                min_delete_actual = 7000000000000
                for folder in filesystem.folders:
                    if folder.get_size() > min_delete:
                        if folder.get_size() < min_delete_actual:
                            min_delete_actual = folder.get_size()
                return min_delete_actual
        return day07(file_lines, False)

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



