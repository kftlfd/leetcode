"""
Leetcode
139. Word Break (medium)
2023-08-04

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:

    1 <= s.length <= 300
    1 <= wordDict.length <= 1000
    1 <= wordDict[i].length <= 20
    s and wordDict[i] consist of only lowercase English letters.
    All the strings of wordDict are unique.
"""

from typing import List


class TrieNode:
    def __init__(self, isWord=False):
        self.isWord = isWord
        self.next = {}


class Trie:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for word in words:
            self.insert(word)

    def insert(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.next:
                cur.next[c] = TrieNode()
            cur = cur.next[c]
        cur.isWord = True


class Solution:
    """
    Runtime: 43 ms, faster than 92.66% of Python3 online submissions for Word Break.
    Memory Usage: 18.9 MB, less than 5.08% of Python3 online submissions for Word Break.
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie(wordDict)
        cache = {}

        def check(start_index: int):
            if start_index >= len(s):
                return True

            if start_index in cache:
                return cache[start_index]

            cur = trie.root

            for i in range(start_index, len(s)):
                c = s[i]

                if c not in cur.next:
                    cache[start_index] = False
                    return False

                if cur.next[c].isWord and check(i + 1):
                    cache[start_index] = True
                    return True

                cur = cur.next[c]

            cache[start_index] = cur.isWord
            return cur.isWord

        return check(0)


sol = Solution()
tests = [
    (("leetcode", ["leet", "code"]),
     True),

    (("applepenapple", ["apple", "pen"]),
     True),

    (("catsandog", ["cats", "dog", "sand", "and", "cat"]),
     False)
]
for inp, exp in tests:
    res = sol.wordBreak(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
