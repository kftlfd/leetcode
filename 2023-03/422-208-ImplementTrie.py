"""
Leetcode
208. Implement Trie (Prefix Tree) (medium)
2023-03-17

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

    Trie() Initializes the trie object.
    void insert(String word) Inserts the string word into the trie.
    boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
    boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
"""


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

from typing import Optional


class TrieNode:
    def __init__(self, is_word=False):
        self.is_word = is_word
        self.next_vals = [None] * 26


class Trie:
    """
    Runtime: 209 ms, faster than 29.70% of Python3 online submissions for Implement Trie (Prefix Tree).
    Memory Usage: 33.4 MB, less than 8.15% of Python3 online submissions for Implement Trie (Prefix Tree).
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not curr.next_vals[idx]:
                curr.next_vals[idx] = TrieNode()
            curr = curr.next_vals[idx]
        curr.is_word = True

    def traverse(self, word: str) -> Optional[TrieNode]:
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not curr.next_vals[idx]:
                return None
            curr = curr.next_vals[idx]
        return curr

    def search(self, word: str) -> bool:
        node = self.traverse(word)
        return node.is_word if node else False

    def startsWith(self, prefix: str) -> bool:
        node = self.traverse(prefix)
        return node is not None


class TrieNode2:
    def __init__(self):
        self.is_word = False
        self.chars = {}


class Trie2:
    """
    Runtime: 158 ms, faster than 85.19% of Python3 online submissions for Implement Trie (Prefix Tree).
    Memory Usage: 31.7 MB, less than 52.72% of Python3 online submissions for Implement Trie (Prefix Tree).
    """

    def __init__(self):
        self.root = TrieNode2()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.chars:
                curr.chars[c] = TrieNode2()
            curr = curr.chars[c]
        curr.is_word = True

    def traverse(self, word: str) -> Optional[TrieNode2]:
        curr = self.root
        for c in word:
            if c not in curr.chars:
                return None
            curr = curr.chars[c]
        return curr

    def search(self, word: str) -> bool:
        node = self.traverse(word)
        return node.is_word if node else False

    def startsWith(self, prefix: str) -> bool:
        node = self.traverse(prefix)
        return node is not None


tests = [
    ((
        ["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
        [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    ),
        '[null, null, true, false, true, null, true]'),
]

for inp, exp in tests:
    t = None
    outputs = []

    for method, args in zip(*inp):
        if method == "Trie":
            t = Trie2()
            outputs.append("null")
        elif method == "insert":
            r = t.insert(*args)
            outputs.append(r if r else "null")
        elif method == "search":
            r = t.search(*args)
            outputs.append(
                "true" if r is True else "false" if r is False else r)
        elif method == "startsWith":
            r = t.startsWith(*args)
            outputs.append(
                "true" if r is True else "false" if r is False else r)

    res = f"[{', '.join(outputs)}]"

    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
