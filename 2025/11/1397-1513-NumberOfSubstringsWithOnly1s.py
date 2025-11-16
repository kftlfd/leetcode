"""
Leetcode
2025-11-16
1513. Number of Substrings With Only 1s
Medium

Given a binary string s, return the number of substrings with all characters 1's. Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: s = "0110111"
Output: 9
Explanation: There are 9 substring in total with only 1's characters.
"1" -> 5 times.
"11" -> 3 times.
"111" -> 1 time.

Example 2:

Input: s = "101"
Output: 2
Explanation: Substring "1" is shown 2 times in s.

Example 3:

Input: s = "111111"
Output: 21
Explanation: Each substring contains only 1's characters.

 

Constraints:

    1 <= s.length <= 10^5
    s[i] is either '0' or '1'.


Count number of 1s in each consecutive-1 group. For a group with n consecutive 1s, the total contribution of it to the final answer is (n + 1) * n // 2.
"""


class Solution:
    """
    Runtime 13ms Beats 73.41%
    Memory 18.05MB Beats 82.40%
    """

    def numSub(self, s: str) -> int:
        ans = 0
        cur = 0

        for c in s:
            if c == "1":
                cur += 1
                ans += cur
            else:
                cur = 0

        return ans % (10**9 + 7)


class Solution1:
    """
    leetcode solution: Traverse The String To Find The Longest Substring
    Runtime 21ms Beats 32.96%
    Memory 18.03MB Beats 82.40%
    """

    def numSub(self, s: str) -> int:
        total, consecutive = 0, 0
        length = len(s)
        for i in range(length):
            if s[i] == "0":
                total += consecutive * (consecutive + 1) // 2
                consecutive = 0
            else:
                consecutive += 1

        total += consecutive * (consecutive + 1) // 2
        total %= 10**9 + 7
        return total
