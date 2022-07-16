import sys
from typing import List

input = sys.stdin.readline

class Node(object):

    def __init__(self, key: str) -> None:
        self.key = key
        self.children = {}
        self.words = []  # 문자를 리스트로 저장

class Trie:

    def __init__(self) -> None:
        self.head = Node(None)
    
    def insert(self, words: List[str]) -> None:
        current_node = self.head

        for word in words:
            if word not in current_node.children:
                current_node.children[word] = Node(word)
                # 새 문자를 리스트에 추가
                current_node.words.append(word)
            current_node = current_node.children[word]

    # dfs 탐색으로 개미굴 순회
    def solve(self, current_node: Node, depth: int) -> None:
        words = sorted(current_node.words)
        for word in words:
            print('--' * depth + word)
            # current_node 에 Node 를 넣어 dfs 탐색
            self.solve(current_node.children[word], depth + 1)


N = int(input())
trie = Trie()

for _ in range(N):
    K, *foods = map(str, input().strip().split())
    trie.insert(foods)

trie.solve(trie.head, 0)