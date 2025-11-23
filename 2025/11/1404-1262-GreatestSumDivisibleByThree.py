"""
Leetcode
2025-11-23
1262. Greatest Sum Divisible by Three
Medium

Given an integer array nums, return the maximum possible sum of elements of the array such that it is divisible by three.

 

Example 1:

Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).

Example 2:

Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.

Example 3:

Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).

 

Constraints:

    1 <= nums.length <= 4 * 10^4
    1 <= nums[i] <= 10^4


Hint 1
Represent the state as DP[pos][mod]: maximum possible sum starting in the position "pos" in the array where the current sum modulo 3 is equal to mod.
"""

from typing import List


class Solution1:
    """
    leetcode solution 1: Greedy + Forward Thinking
    Runtime 30ms Beats 63.02%
    Memory 22.10MB Beats 36.39%
    """

    def maxSumDivThree(self, nums: List[int]) -> int:
        a = [x for x in nums if x % 3 == 0]
        b = sorted([x for x in nums if x % 3 == 1], reverse=True)
        c = sorted([x for x in nums if x % 3 == 2], reverse=True)

        ans = 0
        lb, lc = len(b), len(c)
        for cntb in [lb - 2, lb - 1, lb]:
            if cntb >= 0:
                for cntc in [lc - 2, lc - 1, lc]:
                    if cntc >= 0 and (cntb - cntc) % 3 == 0:
                        ans = max(ans, sum(b[:cntb]) + sum(c[:cntc]))
        return ans + sum(a)


class Solution2:
    """
    leetcode solution 2: Greedy + Backward Thinking
    Runtime 34ms Beats 61.24%
    Memory 22.13MB Beats 30.77%
    """

    def maxSumDivThree(self, nums: List[int]) -> int:
        # a = [x for x in nums if x % 3 == 0]
        b = sorted([x for x in nums if x % 3 == 1], reverse=True)
        c = sorted([x for x in nums if x % 3 == 2], reverse=True)
        tot, remove = sum(nums), float("inf")

        if tot % 3 == 0:
            remove = 0
        elif tot % 3 == 1:
            if len(b) >= 1:
                remove = min(remove, b[-1])
            if len(c) >= 2:
                remove = min(remove, c[-2] + c[-1])
        else:
            if len(b) >= 2:
                remove = min(remove, b[-2] + b[-1])
            if len(c) >= 1:
                remove = min(remove, c[-1])

        return tot - int(remove)


class Solution3:
    """
    leetcode solution 3: Dynamic Programming
    Runtime 121ms Beats 25.15%
    Memory 21.68MB Beats 92.60%
    """

    def maxSumDivThree(self, nums: List[int]) -> int:
        f = [0, -float("inf"), -float("inf")]
        for num in nums:
            g = f[:]
            for i in range(3):
                g[(i + num % 3) % 3] = max(g[(i + num % 3) % 3], f[i] + num)
            f = g
        return f[0]
