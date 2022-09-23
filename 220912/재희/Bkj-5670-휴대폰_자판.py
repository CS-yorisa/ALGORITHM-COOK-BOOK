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
        current_node.data = string

    def search(self, string: str) -> int:
        current_node = self.head
        count: int = 0

        for idx, char in enumerate(string):
            if idx == 0 or len(current_node.children) >= 2 or current_node.data:
                count += 1
            current_node = current_node.children[char]

        return count


while True:
    try:
        N: int = int(input())
    except:
        break
    words: list[str] = [input().rstrip() for _ in range(N)]
    trie = Trie()
    for string in words:
        trie.insert(string)
    answer = []
    for string in words:
        answer.append(trie.search(string))

    print(f"{round(sum(answer) / len(answer), 2):.2f}")
