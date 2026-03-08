"""
Leetcode
2026-03-08
1980. Find Unique Binary String
Medium

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


"""

from typing import List


class Solution01:
    """
    Runtime 0ms Beats 100.00%
    Memory 19.39MB Beats 71.26%
    """

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)

        def f(x):
            return format(x, f"0{n}b")

        ans = 0
        nums = sorted(nums)

        i = 0
        while i < n and f(ans) == nums[i]:
            ans += 1
            i += 1

        return f(ans)


class Solution02:
    """
    Runtime 3ms Beats 24.80%
    Memory 19.41MB Beats 52.95%
    """

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)

        def f(x) -> str:
            return format(x, f"0{n}b")

        ans = 0

        while f(ans) in nums:
            ans += 1

        return f(ans)


class Solution4:
    """
    leetcode solution 4: Cantor's Diagonal Argument
    Runtime 0ms Beats 100.00%
    Memory 19.30MB Beats 90.94%
    """

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = []
        for i in range(len(nums)):
            curr = nums[i][i]
            ans.append("1" if curr == "0" else "0")

        return "".join(ans)
