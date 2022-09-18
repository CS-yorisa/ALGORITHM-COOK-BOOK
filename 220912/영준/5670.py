"""
Title : 휴대폰 자판
Link : https://www.acmicpc.net/problem/5670
"""

from sys import stdin

input = stdin.readline
II = lambda: int(input())
IS = lambda: input().strip()


def make_trie(words: list[str]) -> dict[str:set]:
    trie = {"": set()}
    for word in words:
        word_now = ""
        for s in word:
            word_next = word_now + s
            trie[word_now].add(word_next)
            if word_next not in trie:
                trie[word_next] = set()
            word_now = word_next
        trie[word_now].add("")
    return trie


def search(words: list[str], trie: dict[str:set]) -> int:
    total_time = 0
    for word in words:
        word_now = ""
        for s in word:
            word_next = word_now + s
            if trie[word_now] and trie[word_now] != {
                word_next,
            }:
                total_time += 1
            word_now = word_next
    if len(list(trie[""])) == 1:
        total_time += len(words)
    return total_time


if __name__ == "__main__":
    while True:
        try:
            N = II()
        except Exception:
            break
        words = [IS() for _ in range(N)]
        trie = make_trie(words)
        print(f"{search(words, trie) / N:.2f}")
