"""
Leetcode
1422. Maximum Score After Splitting a String
Easy
2023-12-22

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
    """
    Runtime: 46 ms, faster than 40.26% of Python3 online submissions for Maximum Score After Splitting a String.
    Memory Usage: 17.3 MB, less than 5.69% of Python3 online submissions for Maximum Score After Splitting a String.
    """

    def maxScore(self, s: str) -> int:
        ans = 0

        ones = [0] * (len(s) + 1)
        for i in range(len(s)-1, -1, -1):
            ones[i] = int(s[i] == "1") + ones[i + 1]

        zeroes = 0

        for i in range(len(s) - 1):
            zeroes += s[i] == "0"
            ans = max(ans, zeroes + ones[i + 1])

        return ans


class Solution2:
    """
    leetcode solution 2: Count Left Zeros and Right Ones
    Runtime: 44 ms, faster than 47.92% of Python3 online submissions for Maximum Score After Splitting a String.
    Memory Usage: 17.1 MB, less than 5.69% of Python3 online submissions for Maximum Score After Splitting a String.
    """

    def maxScore(self, s: str) -> int:
        ones = s.count("1")
        zeros = 0
        ans = 0

        for i in range(len(s) - 1):
            if s[i] == "1":
                ones -= 1
            else:
                zeros += 1

            ans = max(ans, zeros + ones)

        return ans


class Solution3:
    """
    leetcode solution 3: One Pass
    Runtime: 37 ms, faster than 85.12% of Python3 online submissions for Maximum Score After Splitting a String.
    Memory Usage: 17.4 MB, less than 5.69% of Python3 online submissions for Maximum Score After Splitting a String.
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

        return best + ones
