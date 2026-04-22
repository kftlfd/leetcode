"""
Leetcode
2026-04-22
2452. Words Within Two Edits of Dictionary
Medium

You are given two string arrays, queries and dictionary. All words in each array comprise of lowercase English letters and have the same length.

In one edit you can take a word from queries, and change any letter in it to any other letter. Find all words from queries that, after a maximum of two edits, equal some word from dictionary.

Return a list of all words from queries, that match with some word from dictionary after a maximum of two edits. Return the words in the same order they appear in queries.

 

Example 1:

Input: queries = ["word","note","ants","wood"], dictionary = ["wood","joke","moat"]
Output: ["word","note","wood"]
Explanation:
- Changing the 'r' in "word" to 'o' allows it to equal the dictionary word "wood".
- Changing the 'n' to 'j' and the 't' to 'k' in "note" changes it to "joke".
- It would take more than 2 edits for "ants" to equal a dictionary word.
- "wood" can remain unchanged (0 edits) and match the corresponding dictionary word.
Thus, we return ["word","note","wood"].

Example 2:

Input: queries = ["yes"], dictionary = ["not"]
Output: []
Explanation:
Applying any two edits to "yes" cannot make it equal to "not". Thus, we return an empty array.

 

Constraints:

    1 <= queries.length, dictionary.length <= 100
    n == queries[i].length == dictionary[j].length
    1 <= n <= 100
    All queries[i] and dictionary[j] are composed of lowercase English letters.


"""

from typing import List


class Solution01:
    """
    Runtime 124ms Beats 17.65%
    Memory 19.40MB Beats 50.49%
    """

    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []

        for word in queries:
            for dict_word in dictionary:
                if self.str_dist(word, dict_word) <= 2:
                    ans.append(word)
                    break

        return ans

    def str_dist(self, s1: str, s2: str) -> int:
        return sum(a != b for a, b in zip(s1, s2))


class Solution02:
    """
    Runtime 12ms Beats 65.20%
    Memory 19.54MB Beats 30.88%
    """

    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def valid(s1: str, s2: str):
            dist = 0
            for a, b in zip(s1, s2):
                if a != b:
                    dist += 1
                    if dist > 2:
                        return False
            return True

        return [
            w for w in queries
            if any(valid(w, dw) for dw in dictionary)
        ]


class Solution2:
    """
    leetcode solution 2: Trie
    Runtime 47ms Beats 46.57%
    Memory 23.00MB Beats 7.35%
    """

    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        for w in dictionary:
            self.insert(w)

        res = []
        for q in queries:
            if self.dfs(q, 0, self.root, 0):
                res.append(q)
        return res

    class TrieNode:
        def __init__(self):
            self.child = [None] * 26
            self.isEnd = False

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            idx = ord(c) - ord("a")
            if not node.child[idx]:
                node.child[idx] = self.TrieNode()
            node = node.child[idx]
        node.isEnd = True

    def dfs(self, word, i, node, cnt):
        if cnt > 2 or not node:
            return False

        if i == len(word):
            return node.isEnd

        idx = ord(word[i]) - ord("a")

        # no changes made
        if node.child[idx] and self.dfs(word, i + 1, node.child[idx], cnt):
            return True

        # made changes
        if cnt < 2:
            for c in range(26):
                if c == idx:
                    continue
                if node.child[c] and self.dfs(
                    word, i + 1, node.child[c], cnt + 1
                ):
                    return True

        return False
