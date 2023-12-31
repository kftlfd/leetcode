"""
Leetcode
1903. Largest Odd Number in String
Easy
2023-12-08

You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.

Example 2:

Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".

Example 3:

Input: num = "35427"
Output: "35427"
Explanation: "35427" is already an odd number.

 

Constraints:

    1 <= num.length <= 105
    num only consists of digits and does not contain any leading zeros.
"""


class Solution:
    """
    Runtime: 63 ms, faster than 22.28% of Python3 online submissions for Largest Odd Number in String.
    Memory Usage: 17.8 MB, less than 80.27% of Python3 online submissions for Largest Odd Number in String.
    """

    def largestOddNumber(self, num: str) -> str:

        odds = ("1", "3", "5", "7", "9")

        for end in range(len(num) - 1, -1, -1):
            c = num[end]
            if c in odds:
                return num[:end+1]

        return ""
