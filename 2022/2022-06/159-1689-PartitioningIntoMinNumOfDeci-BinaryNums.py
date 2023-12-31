"""
Leetcode
1689. Partitioning Into Minimum Number Of Deci-Binary Numbers (medium)
2022-06-27

A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.

Example 1:
Input: n = "32"
Output: 3
Explanation: 10 + 11 + 11 = 32

Example 2:
Input: n = "82734"
Output: 8

Example 3:
Input: n = "27346209830709182346"
Output: 9

Hints:
1. Think about if the input was only one digit. Then you need to add up as many ones as the value of this digit.
2. If the input has multiple digits, then you can solve for each digit independently, and merge the answers to form numbers that add up to that input.
3. Thus the answer is equal to the max digit.
"""


# Runtime: 82 ms, faster than 80.27% of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
# Memory Usage: 14.8 MB, less than 50.25% of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))


s = Solution()
tests = [
    "32",
    "82734",
    "27346209830709182346",
]
for t in tests:
    print(t)
    print(s.minPartitions(t))
    print()
