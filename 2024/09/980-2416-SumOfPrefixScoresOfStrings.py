"""
Leetcode
2024-09-25
2416. Sum of Prefix Scores of Strings
Hard

You are given an array words of size n consisting of non-empty strings.

We define the score of a string word as the number of strings words[i] such that word is a prefix of words[i].

    For example, if words = ["a", "ab", "abc", "cab"], then the score of "ab" is 2, since "ab" is a prefix of both "ab" and "abc".

Return an array answer of size n where answer[i] is the sum of scores of every non-empty prefix of words[i].

Note that a string is considered as a prefix of itself.

 

Example 1:

Input: words = ["abc","ab","bc","b"]
Output: [5,4,3,2]
Explanation: The answer for each string is the following:
- "abc" has 3 prefixes: "a", "ab", and "abc".
- There are 2 strings with the prefix "a", 2 strings with the prefix "ab", and 1 string with the prefix "abc".
The total is answer[0] = 2 + 2 + 1 = 5.
- "ab" has 2 prefixes: "a" and "ab".
- There are 2 strings with the prefix "a", and 2 strings with the prefix "ab".
The total is answer[1] = 2 + 2 = 4.
- "bc" has 2 prefixes: "b" and "bc".
- There are 2 strings with the prefix "b", and 1 string with the prefix "bc".
The total is answer[2] = 2 + 1 = 3.
- "b" has 1 prefix: "b".
- There are 2 strings with the prefix "b".
The total is answer[3] = 2.

Example 2:

Input: words = ["abcd"]
Output: [4]
Explanation:
"abcd" has 4 prefixes: "a", "ab", "abc", and "abcd".
Each prefix has a score of one, so the total is answer[0] = 1 + 1 + 1 + 1 = 4.

 

Constraints:

    1 <= words.length <= 1000
    1 <= words[i].length <= 1000
    words[i] consists of lowercase English letters.
"""

from collections import defaultdict
from typing import List, Optional


class Solution:
    """
    Runtime: 3540 ms, faster than 14.14% of Python3 online submissions for Sum of Prefix Scores of Strings.
    Memory Usage: 598.4 MB, less than 10.35% of Python3 online submissions for Sum of Prefix Scores of Strings.
    """

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        prefixes = defaultdict(int)

        for word in words:
            for end in range(1, len(word) + 1):
                prefixes[word[:end]] += 1

        def get_score(w: str):
            return sum(prefixes[w[:end]] for end in range(1, len(w) + 1))

        return [get_score(w) for w in words]


class Solution1:
    """
    Runtime: 3224 ms, faster than 27.25% of Python3 online submissions for Sum of Prefix Scores of Strings.
    Memory Usage: 385.3 MB, less than 31.38% of Python3 online submissions for Sum of Prefix Scores of Strings.
    """

    class Trie:

        class TrieNode:
            def __init__(self, occurences=1):
                self.nxt = [None] * 26
                self.occurences = occurences

        def __init__(self, words: Optional[List[str]]):
            self.root = self.TrieNode(0)
            if words:
                for word in words:
                    self.add(word)

        def idx(self, c: str):
            return ord(c) - 97  # ord('a')

        def add(self, word: str):
            cur = self.root
            for c in word:
                i = self.idx(c)
                if not cur.nxt[i]:
                    cur.nxt[i] = self.TrieNode()
                else:
                    cur.nxt[i].occurences += 1
                cur = cur.nxt[i]

        def get_score(self, word: str) -> int:
            score = 0
            cur = self.root
            for c in word:
                i = self.idx(c)
                if cur.nxt[i]:
                    cur = cur.nxt[i]
                    score += cur.occurences
                else:
                    break
            return score

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = self.Trie(words)
        return [trie.get_score(w) for w in words]
