"""
Leetcode
97. Interleaving String (medium)
2023-08-25

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively, such that:

    s = s1 + s2 + ... + sn
    t = t1 + t2 + ... + tm
    |n - m| <= 1
    The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

Note: a + b is the concatenation of strings a and b.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.

Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.

Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true

Constraints:

    0 <= s1.length, s2.length <= 100
    0 <= s3.length <= 200
    s1, s2, and s3 consist of lowercase English letters.
"""


from functools import cache


class Solution:
    """
    Runtime: 47 ms, faster than 79.98% of Python3 online submissions for Interleaving String.
    Memory Usage: 17.4 MB, less than 25.31% of Python3 online submissions for Interleaving String.
    """

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        @cache
        def dfs(p1: int, p2: int, p3: int) -> bool:
            if p3 >= len(s3):
                return True

            if p1 < len(s1) and s1[p1] == s3[p3] and dfs(p1 + 1, p2, p3 + 1):
                return True

            if p2 < len(s2) and s2[p2] == s3[p3] and dfs(p1, p2 + 1, p3 + 1):
                return True

            return False

        return dfs(0, 0, 0)


s = Solution()
tests = [
    (("aabcc", "dbbca", "aadbbcbcac"),
     True),

    (("aabcc", "dbbca", "aadbbbaccc"),
     False),

    (("", "", ""),
     True),
]
for inp, exp in tests:
    res = s.isInterleave(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
