"""
Leetcode
2025-02-20
1980. Find Unique Binary String
Solved
Medium
Topics
Companies
Hint

Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

 

Example 1:

Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.

Example 2:

Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.

Example 3:

Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.

 

Constraints:

    n == nums.length
    1 <= n <= 16
    nums[i].length == n
    nums[i] is either '0' or '1'.
    All the strings of nums are unique.

    
Hint 1
We can convert the given strings into base 10 integers.
Hint 2
Can we use recursion to generate all possible strings?
"""

from typing import List


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.82MB Beats 52.45%
    """

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        format_str = f"0{n}b"

        for i in range(n + 1):
            cur = format(i, format_str)
            if cur in nums:
                continue
            return cur

        return ""


class Solution4:
    """
    leetcode solution 4: Cantor's Diagonal Argument
    Runtime 0ms Beats 100.00%
    Memory 17.86MB Beats 52.45%
    """

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = []
        for i in range(len(nums)):
            curr = nums[i][i]
            ans.append("1" if curr == "0" else "0")

        return "".join(ans)
