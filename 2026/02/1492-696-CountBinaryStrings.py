"""
Leetcode
2026-02-19
696. Count Binary Substrings
Easy

Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

 

Example 1:

Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

Example 2:

Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

 

Constraints:

    1 <= s.length <= 10^5
    s[i] is either '0' or '1'.


"""


import itertools


class Solution:
    """
    Runtime 147ms Beats 5.03%
    Memory 19.66MB Beats 50.08%
    """

    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)

        def count(i: int) -> int:
            res = 0
            l = i
            r = i + 1
            if l < 0 or r >= n or s[l] == s[r]:
                return 0
            lc, rc = s[l], s[r]
            while l >= 0 and r < n and s[l] == lc and s[r] == rc:
                res += 1
                l -= 1
                r += 1
            return res

        return sum(count(i) for i in range(n))


class Solution1_1:
    """
    leetcode solution 1: Group By Character
    Runtime 76ms Beats 29.85%
    Memory 19.76MB Beats 29.48%
    """

    def countBinarySubstrings(self, s: str) -> int:
        groups = [1]

        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1

        ans = 0

        for i in range(1, len(groups)):
            ans += min(groups[i - 1], groups[i])

        return ans


class Solution1_2:
    """
    leetcode solution 1: Group By Character (Alternate Implentation)
    Runtime 67ms Beats 47.70%
    Memory 20.15MB Beats 8.06%
    """

    def countBinarySubstrings(self, s: str) -> int:
        groups = [len(list(v)) for _, v in itertools.groupby(s)]
        return sum(min(a, b) for a, b in zip(groups, groups[1:]))


class Solution2:
    """
    leetcode solution 2: Linear Scan
    Runtime 47ms Beats 94.59%
    Memory 19.52MB Beats 68.58%
    """

    def countBinarySubstrings(self, s: str) -> int:
        ans, prev, cur = 0, 0, 1

        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                ans += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1

        return ans + min(prev, cur)
