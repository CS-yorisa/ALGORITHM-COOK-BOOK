import sys

input = sys.stdin.readline


class Node(object):
    def __init__(self, key: str, data=None) -> None:
        self.key = key
        self.data = data
        self.children = {}


class Trie:
    def __init__(self) -> None:
        self.head = Node(None)

    def insert(self, string: str) -> None:
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = (string, len(string))

    def search(self, string: str) -> list[str, int] or None:
        current_node = self.head

        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return None

        if current_node.data:
            return current_node.data
        else:
            return None


def solve() -> None:
    for i in range(4):
        for j in range(4):
            visited[i][j] = True
            dfs(i, j, board[i][j], 1)
            visited[i][j] = False


def dfs(x: int, y: int, string: str, cnt: int) -> None:
    if cnt > 8:
        return
    trie.insert(string)
    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < 4 and 0 <= ny < 4 and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, string + board[nx][ny], cnt + 1)
            visited[nx][ny] = False


score_table: list[int] = [0, 0, 0, 1, 1, 2, 3, 5, 11]
dx, dy = (1, 1, 0, -1, -1, -1, 0, 1), (0, 1, 1, 1, 0, -1, -1, -1)

w: int = int(input())
words: list[str] = [input().strip() for _ in range(w)]
blank = input()
b: int = int(input())
for i in range(b):
    if i != 0:
        blank = input()
    board: list[str] = [input().strip() for _ in range(4)]
    visited: list[list[bool]] = [[False] * 4 for _ in range(4)]
    trie = Trie()
    answer = []
    solve()
    for word in words:
        check = trie.search(word)
        if check:
            answer.append(check)
    answer.sort(key=lambda x: (-x[1], x[0]))
    score = 0
    for string, length in answer:
        score += score_table[length]
    print(score, answer[0][0], len(answer))
