"""
Leetcode
2026-05-28
3093. Longest Common Suffix Queries
Hard

You are given two arrays of strings wordsContainer and wordsQuery.

For each wordsQuery[i], you need to find a string from wordsContainer that has the longest common suffix with wordsQuery[i]. If there are two or more strings in wordsContainer that share the longest common suffix, find the string that is the smallest in length. If there are two or more such strings that have the same smallest length, find the one that occurred earlier in wordsContainer.

Return an array of integers ans, where ans[i] is the index of the string in wordsContainer that has the longest common suffix with wordsQuery[i].

 

Example 1:

Input: wordsContainer = ["abcd","bcd","xbcd"], wordsQuery = ["cd","bcd","xyz"]

Output: [1,1,1]

Explanation:

Let's look at each wordsQuery[i] separately:

    For wordsQuery[0] = "cd", strings from wordsContainer that share the longest common suffix "cd" are at indices 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3.
    For wordsQuery[1] = "bcd", strings from wordsContainer that share the longest common suffix "bcd" are at indices 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3.
    For wordsQuery[2] = "xyz", there is no string from wordsContainer that shares a common suffix. Hence the longest common suffix is "", that is shared with strings at index 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3.

Example 2:

Input: wordsContainer = ["abcdefgh","poiuygh","ghghgh"], wordsQuery = ["gh","acbfgh","acbfegh"]

Output: [2,0,2]

Explanation:

Let's look at each wordsQuery[i] separately:

    For wordsQuery[0] = "gh", strings from wordsContainer that share the longest common suffix "gh" are at indices 0, 1, and 2. Among these, the answer is the string at index 2 because it has the shortest length of 6.
    For wordsQuery[1] = "acbfgh", only the string at index 0 shares the longest common suffix "fgh". Hence it is the answer, even though the string at index 2 is shorter.
    For wordsQuery[2] = "acbfegh", strings from wordsContainer that share the longest common suffix "gh" are at indices 0, 1, and 2. Among these, the answer is the string at index 2 because it has the shortest length of 6.

 

Constraints:

    1 <= wordsContainer.length, wordsQuery.length <= 10^4
    1 <= wordsContainer[i].length <= 5 * 10^3
    1 <= wordsQuery[i].length <= 5 * 10^3
    wordsContainer[i] consists only of lowercase English letters.
    wordsQuery[i] consists only of lowercase English letters.
    Sum of wordsContainer[i].length is at most 5 * 10^5.
    Sum of wordsQuery[i].length is at most 5 * 10^5.

 
"""

from typing import List


class Solution:
    """
    Runtime 1172ms Beats 73.59%
    Memory 165.03MB Beats 77.36%
    """

    class Trie:

        class TrieNode:
            def __init__(self, idx: int, w_len: int):
                self.idx = idx
                self.w_len = w_len
                self.nxt = {}

        def __init__(self):
            self.root = self.TrieNode(1 << 31, 1 << 31)

        def add(self, word: str, idx: int):
            l = len(word)

            cur = self.root
            for c in reversed(word):
                if c not in cur.nxt:
                    cur.nxt[c] = self.TrieNode(idx, l)
                else:
                    node = cur.nxt[c]
                    if l < node.w_len:
                        node.w_len = l
                        node.idx = idx
                    elif l == node.w_len and idx < node.idx:
                        node.idx = idx
                cur = cur.nxt[c]

            if l < self.root.w_len:
                self.root.w_len = l
                self.root.idx = idx
            elif l == self.root.w_len and idx < self.root.idx:
                self.root.idx = idx

        def get_lcs_idx(self, word: str):
            cur = self.root
            for c in reversed(word):
                if c not in cur.nxt:
                    break
                cur = cur.nxt[c]
            return cur.idx

    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = self.Trie()

        for i, word in enumerate(wordsContainer):
            trie.add(word, i)

        return [trie.get_lcs_idx(word) for word in wordsQuery]


class Solution1:
    """
    leetcode solution
    Runtime 1745ms Beats29.56%
    Memory 180.29MB Beats 49.06%
    """

    class Trie:

        class TrieNode:
            def __init__(self):
                self.children = {}
                self.min_len = float("inf")
                self.idx = float("inf")

        def __init__(self):
            self.root = self.TrieNode()

        def insert(self, s: str, idx: int):
            node = self.root
            if len(s) < node.min_len:
                node.min_len = len(s)
                node.idx = idx

            for ch in s:
                c = ch
                if c not in node.children:
                    node.children[c] = self.TrieNode()
                node = node.children[c]

                if len(s) < node.min_len:
                    node.min_len = len(s)
                    node.idx = idx

        def query(self, s: str) -> int:
            node = self.root

            for ch in s:
                if ch in node.children:
                    node = node.children[ch]
                else:
                    break

            return int(node.idx)

    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = self.Trie()

        for i, word in enumerate(wordsContainer):
            reversed_word = word[::-1]
            trie.insert(reversed_word, i)

        res = []
        for query in wordsQuery:
            reversed_query = query[::-1]
            res.append(trie.query(reversed_query))

        return res
