"""
Leetcode
387. First Unique Character in a String (easy)
2022-08-16

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1
"""


# Runtime: 97 ms, faster than 91.13% of Python3 online submissions for First Unique Character in a String.
# Memory Usage: 14.1 MB, less than 96.20% of Python3 online submissions for First Unique Character in a String.
class Solution:
    def firstUniqChar(self, s: str) -> int:
        ht = {}
        l = len(s)
        for i, c in enumerate(s):
            if c in ht:
                ht[c] = l
            else:
                ht[c] = i
        vals = [x for x in ht.values() if x < l]
        return min(vals) if vals else -1


# leetcode solution
# Runtime: 107 ms, faster than 87.03% of Python3 online submissions for First Unique Character in a String.
# Memory Usage: 14.2 MB, less than 59.01% of Python3 online submissions for First Unique Character in a String.
class Solution1:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1


s = Solution()
tests = [
    "leetcode",
    "loveleetcode",
    "aabb",
]
for t in tests:
    print(t)
    print(s.firstUniqChar(t))
    print()
