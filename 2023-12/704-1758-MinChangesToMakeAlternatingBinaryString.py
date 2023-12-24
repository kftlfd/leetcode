"""
Leetcode
1758. Minimum Changes To Make Alternating Binary String
Easy
2023-12-24

You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.

 

Example 1:

Input: s = "0100"
Output: 1
Explanation: If you change the last character to '1', s will be "0101", which is alternating.

Example 2:

Input: s = "10"
Output: 0
Explanation: s is already alternating.

Example 3:

Input: s = "1111"
Output: 2
Explanation: You need two operations to reach "0101" or "1010".

 

Constraints:

    1 <= s.length <= 10^4
    s[i] is either '0' or '1'.
"""


class Solution:
    """
    Runtime: 53 ms, faster than 51.47% of Python3 online submissions for Minimum Changes To Make Alternating Binary String.
    Memory Usage: 17.4 MB, less than 5.67% of Python3 online submissions for Minimum Changes To Make Alternating Binary String.
    """

    def minOperations(self, s: str) -> int:
        s_0_changes = 0
        s_1_changes = 0

        chars = ['0', '1']
        s_0_index = 0
        s_1_index = 1

        for c in s:
            if c != chars[s_0_index]:
                s_0_changes += 1

            if c != chars[s_1_index]:
                s_1_changes += 1

            s_0_index = (s_0_index + 1) % 2
            s_1_index = (s_1_index + 1) % 2

        return min(s_0_changes, s_1_changes)


class Solution1:
    """
    leetcode solution 1
    Runtime: 37 ms, faster than 98.74% of Python3 online submissions for Minimum Changes To Make Alternating Binary String.
    Memory Usage: 17.5 MB, less than 5.67% of Python3 online submissions for Minimum Changes To Make Alternating Binary String.
    """

    def minOperations(self, s: str) -> int:
        start0 = 0
        start1 = 0

        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == "0":
                    start1 += 1
                else:
                    start0 += 1
            else:
                if s[i] == "1":
                    start1 += 1
                else:
                    start0 += 1

        return min(start0, start1)


class Solution2:
    """
    leetcode solution 2: Only Check One
    Runtime: 42 ms, faster than 93.70% of Python3 online submissions for Minimum Changes To Make Alternating Binary String.
    Memory Usage: 17.2 MB, less than 5.67% of Python3 online submissions for Minimum Changes To Make Alternating Binary String.
    """

    def minOperations(self, s: str) -> int:
        start0 = 0

        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == "1":
                    start0 += 1
            else:
                if s[i] == "0":
                    start0 += 1

        return min(start0, len(s) - start0)
