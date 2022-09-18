"""
Title : Boggle
Link : https://www.acmicpc.net/problem/9202
"""

from sys import stdin

input = stdin.readline
II = lambda: int(input())
IS = lambda: input().strip()


def search(x: int, y: int, string: str, visited: set):
    global trie, words_count, delta, boggle_board
    if string not in trie:
        return
    if trie[string][1]:
        words_count.add(string)
    for dx, dy in delta:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 4 and 0 <= ny < 4:
            if (nx, ny) in visited:
                continue
            search(
                nx,
                ny,
                string + boggle_board[nx][ny],
                visited | {(nx, ny)},
            )


if __name__ == "__main__":
    W: int = II()
    words: list[str] = [IS() for _ in range(W)]
    trie = {"": [set(), False]}
    for word in words:
        last_word: str = ""
        for s in word:
            next_word: str = last_word + s
            trie[last_word][0].add(s)
            if next_word not in trie:
                trie[next_word] = [set(), False]
            last_word = next_word
        trie[last_word][1] = True

    input()
    B: int = II()
    words_point: dict[int, int] = {1: 0, 2: 0, 3: 1, 4: 1, 5: 2, 6: 3, 7: 5, 8: 11}
    delta: tuple[tuple[int]] = (
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
    )
    for _ in range(B):
        boggle_board: list[str] = [IS() for _ in range(4)]
        words_count: set = set()

        for i, line in enumerate(boggle_board):
            for j, s in enumerate(line):
                if s not in trie:
                    continue
                search(i, j, s, {(i, j)})

        words_count = sorted(words_count, key=lambda x: len(x))
        score: int = sum([words_point[len(x)] for x in words_count])
        max_len_word: str = words_count[-1]
        print(score, max_len_word, len(words_count))

        try:
            input()
        except Exception:
            break
