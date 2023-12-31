"""
Leetcode
383. Ransom Note (easy)
2022-08-25

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""


# Runtime: 103 ms, faster than 39.67% of Python3 online submissions for Ransom Note.
# Memory Usage: 14.1 MB, less than 53.79% of Python3 online submissions for Ransom Note.
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        lr = len(ransomNote)
        lm = len(magazine)
        ht = {}

        for i in range(max(lr, lm)):
            if i < lm:
                ht[magazine[i]] = ht.get(magazine[i], 0) + 1
            if i < lr:
                ht[ransomNote[i]] = ht.get(ransomNote[i], 0) - 1

        return all([x >= 0 for x in ht.values()])


# https://leetcode.com/problems/ransom-note/discuss/85837/O(m+n)-one-liner-Python
# Runtime: 90 ms, faster than 52.70% of Python3 online submissions for Ransom Note.
# Memory Usage: 14.2 MB, less than 53.79% of Python3 online submissions for Ransom Note.
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not collections.Counter(ransomNote) - collections.Counter(magazine)


s = Solution()
tests = [
    ("a", "b"),
    ("aa", "ab"),
    ("aa", "aab"),
]
for t in tests:
    print(t)
    print(s.canConstruct(t[0], t[1]))
    print()
