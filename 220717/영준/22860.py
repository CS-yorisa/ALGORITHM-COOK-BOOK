"""
Title : 폴더 정리 (small)
Link : https://www.acmicpc.net/problem/22860
"""

from collections import deque
from dataclasses import dataclass, field
from sys import stdin

input = stdin.readline


@dataclass
class Directory:
    parent: str
    files_count: int = 0
    files: set = field(default_factory=set)

    def get_different_files_count(self) -> int:
        return len(list(self.files))


def add_folder(F: str, parent: str, child: str) -> None:
    global directory, folder_to_directory
    directory[child] = Directory(parent=parent)
    folder_to_directory[F] = child


def add_file(folder_name: str, file_name: str) -> None:
    global directory
    directory[folder_name].files.add(file_name)
    directory[folder_name].files_count += 1


def update_files(folder_name: str, file_name: str) -> None:
    global directory
    while folder_name != "main":
        parent = directory[folder_name].parent
        directory[parent].files.add(file_name)
        directory[parent].files_count += 1
        folder_name = parent


if __name__ == "__main__":
    N, M = map(int, input().split())
    directory: dict[str, Directory] = {"main": Directory(parent="")}
    folder_to_directory: dict[str, str] = {"main": "main"}
    folders = deque()
    files = deque()
    parent_directory = "main"
    for _ in range(N + M):
        P, F, C = input().strip().split()
        if P == "main":
            if C == "0":
                add_file(parent_directory, F)
                folder_to_directory[F] = parent_directory
            else:
                child_directory = f"{parent_directory}/{F}"
                add_folder(F, parent_directory, child_directory)
        else:
            if C == "0":
                files.append((P, F))
            else:
                folders.append((P, F))
    while folders:
        if folders[0][0] not in folder_to_directory:
            folders.rotate(1)
            continue
        P, F = folders.popleft()
        parent_directory = folder_to_directory[P]
        child_directory = f"{parent_directory}/{F}"
        add_folder(F, parent_directory, child_directory)
    while files:
        P, F = files.popleft()
        parent_directory = folder_to_directory[P]
        add_file(parent_directory, F)
        update_files(parent_directory, F)
    for _ in range(int(input())):
        d = input().strip()
        print(directory[d].get_different_files_count(), directory[d].files_count)

"""
3 3
A C 1
main A 1
main B 1
A a 0
C a 0
B a 0
4
main
main/A
main/A/C
main/B
"""
