"""
Leetcode
242. Valid Anagram (easy)
2022-07-28

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""


# Runtime: 69 ms, faster than 62.41% of Python3 online submissions for Valid Anagram.
# Memory Usage: 15.1 MB, less than 11.53% of Python3 online submissions for Valid Anagram.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


# Runtime: 91 ms, faster than 30.29% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.6 MB, less than 34.60% of Python3 online submissions for Valid Anagram.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ht = {}

        for c in s:
            ht[c] = ht.get(c, 0) + 1

        for c in t:
            if c not in ht:
                return False
            ht[c] -= 1

        return all([x == 0 for x in ht.values()])


s = Solution()
tests = [
    ("anagram", "nagaram"),
    ("rat", "car"),
]
for s1, s2 in tests:
    print(s1, s2)
    print(s.isAnagram(s1, s2))
    print()
