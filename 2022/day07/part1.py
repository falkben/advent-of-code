from __future__ import annotations

from dataclasses import dataclass, field

input = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""
input = open("2022/day07/data.txt").read()


@dataclass
class File:
    name: str
    size: int


@dataclass
class Dir:
    name: str
    parent: "Dir" | None = None
    children: list["Dir"] = field(default_factory=list)
    files: list[File] = field(default_factory=list)


directories = []

cur_dir = None
for line in input.splitlines():
    parts = line.split()
    if parts[0] == "$":
        # command, either ls or cd

        if line == "$ cd ..":
            cur_dir = cur_dir.parent
        elif line == "$ ls":
            continue
        else:
            cur_dir = Dir(name=line[5:], parent=cur_dir)
            if cur_dir.parent is not None:
                cur_dir.parent.children.append(cur_dir)
            directories.append(cur_dir)

    else:
        # listing:
        if parts[0] == "dir":
            # ignore
            continue
        else:
            # file to add to current directory
            cur_dir.files.append(File(name=parts[1], size=int(parts[0])))


def calc_dir_size(dir: Dir) -> int:
    size = sum([f.size for f in dir.files])
    for child in dir.children:
        size += calc_dir_size(child)
    return size


# calc sizes:
sizes = 0
for dir in directories:
    ss = calc_dir_size(dir)
    if ss <= 100000:
        sizes += ss

print(sizes)
