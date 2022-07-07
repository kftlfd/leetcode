"""
Leetcode
97. Interleaving String (medium)
2022-07-07

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

 - s = s1 + s2 + ... + sn
 - t = t1 + t2 + ... + tm
 - |n - m| <= 1
 - The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

Note: a + b is the concatenation of strings a and b.
"""


# https://leetcode.com/problems/interleaving-string/discuss/31885/Python-DP-solutions-(O(m*n)-O(n)-space)-BFS-DFS.
# Runtime: 41 ms, faster than 93.82% of Python3 online submissions for Interleaving String.
# Memory Usage: 13.9 MB, less than 90.66% of Python3 online submissions for Interleaving String.
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        r, c, l = len(s1), len(s2), len(s3)
        if r+c != l:
            return False
        dp = [True for _ in range(c+1)]
        for j in range(1, c+1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
        for i in range(1, r+1):
            dp[0] = (dp[0] and s1[i-1] == s3[i-1])
            for j in range(1, c+1):
                dp[j] = (dp[j] and s1[i-1] == s3[i-1+j]
                         ) or (dp[j-1] and s2[j-1] == s3[i-1+j])
        return dp[-1]


s = Solution()
tests = [
    ("aabcc", "dbbca", "aadbbcbcac"),
    ("aabcc", "dbbca", "aadbbbaccc"),
    ("", "", ""),
]
for t in tests:
    print(t)
    print(s.isInterleave(t[0], t[1], t[2]))
    print()
