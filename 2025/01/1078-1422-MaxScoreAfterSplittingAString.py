"""
Leetcode
2025-01-01
1422. Maximum Score After Splitting a String
Easy

Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

 

Example 1:

Input: s = "011101"
Output: 5 
Explanation: 
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5 
left = "01" and right = "1101", score = 1 + 3 = 4 
left = "011" and right = "101", score = 1 + 2 = 3 
left = "0111" and right = "01", score = 1 + 1 = 2 
left = "01110" and right = "1", score = 2 + 1 = 3

Example 2:

Input: s = "00111"
Output: 5
Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5

Example 3:

Input: s = "1111"
Output: 3

 

Constraints:

    2 <= s.length <= 500
    The string s consists of characters '0' and '1' only.
"""


class Solution:
    def maxScore(self, s: str) -> int:
        zeroes = [0] * len(s)
        if s[0] == "0":
            zeroes[0] = 1
        for i in range(1, len(s)):
            zeroes[i] = zeroes[i-1] + (s[i] == "0")

        ones = [0] * len(s)
        for i in range(len(s)-2, -1, -1):
            ones[i] = ones[i+1] + (s[i+1] == "1")

        ans = 0
        for i in range(len(s)-1):
            ans = max(ans, zeroes[i] + ones[i])

        return ans


class Solution2:
    """
    sample 0ms solution
    """

    def maxScore(self, s: str) -> int:
        left = 0
        right = 0
        ans = 0
        # for i in range(len(s)):
        #     right += 0 if s[i] == '0' else 1
        for si in s:
            right += 0 if si == '0' else 1
        for i in range(len(s)-1):
            left += 1 if s[i] == '0' else 0
            right += 0 if s[i] == '0' else -1
            ans = max(left+right, ans)
        return ans


class Solution3:
    """
    leetcode solution 3: One Pass
    """

    def maxScore(self, s: str) -> int:
        ones = 0
        zeros = 0
        best = float('-inf')

        for i in range(len(s) - 1):
            if s[i] == "1":
                ones += 1
            else:
                zeros += 1

            best = max(best, zeros - ones)

        if s[-1] == "1":
            ones += 1
