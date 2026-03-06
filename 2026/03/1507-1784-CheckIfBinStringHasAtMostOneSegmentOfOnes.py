"""
Leetcode
2026-03-06
1784. Check if Binary String Has at Most One Segment of Ones
Easy
Topics
premium lock iconCompanies
Hint

Given a binary string s without leading zeros, return true if s contains at most one contiguous segment of ones. Otherwise, return false.

 

Example 1:

Input: s = "1001"
Output: false
Explanation: The ones do not form a contiguous segment.

Example 2:

Input: s = "110"
Output: true

 

Constraints:

    1 <= s.length <= 100
    s[i] is either '0' or '1'.
    s[0] is '1'.


"""


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 19.35MB Beats 41.18%
    """

    def checkOnesSegment(self, s: str) -> bool:
        ones_ended = False

        for i in range(1, len(s)):
            if s[i] == "1" and ones_ended:
                return False
            if s[i] == "0" and s[i - 1] == "1":
                ones_ended = True

        return True


class Solution1:
    """
    leetcode solution
    Runtime 0ms Beats 100.00%
    Memory 19.29MB Beats 77.09%
    """

    def checkOnesSegment(self, s: str) -> bool:
        return "01" not in s
