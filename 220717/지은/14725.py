import sys
input = sys.stdin.readline

class Trie:
    def __init__(self):
        self.head = {}

    def insert(self, string):
        cur_node = self.head
        for char in string:
            if char not in cur_node:
                cur_node[char] = {}
            cur_node = cur_node[char]
        # 문자열 끝났다는 표시
        cur_node['*'] = {}

    def search(self, depth, cur_node=None):
        if depth == 0:
            cur_node = self.head

        for char in sorted(cur_node.keys()):
            if char!='*':
                print('--'*depth, char, sep="")
            self.search(depth+1, cur_node[char])

trie = Trie()
for _ in range(int(input())):
    data = list(input().split())
    trie.insert(data[1:])

trie.search(0)