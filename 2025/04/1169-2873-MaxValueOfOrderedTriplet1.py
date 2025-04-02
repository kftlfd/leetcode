"""
Leetcode
2025-04-02
2873. Maximum Value of an Ordered Triplet I
Easy

You are given a 0-indexed integer array nums.

Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.

The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].

 

Example 1:

Input: nums = [12,6,1,2,7]
Output: 77
Explanation: The value of the triplet (0, 2, 4) is (nums[0] - nums[2]) * nums[4] = 77.
It can be shown that there are no ordered triplets of indices with a value greater than 77. 

Example 2:

Input: nums = [1,10,3,4,19]
Output: 133
Explanation: The value of the triplet (1, 2, 4) is (nums[1] - nums[2]) * nums[4] = 133.
It can be shown that there are no ordered triplets of indices with a value greater than 133.

Example 3:

Input: nums = [1,2,3]
Output: 0
Explanation: The only ordered triplet of indices (0, 1, 2) has a negative value of (nums[0] - nums[1]) * nums[2] = -3. Hence, the answer would be 0.

 

Constraints:

    3 <= nums.length <= 100
    1 <= nums[i] <= 10^6


Hint 1
Use three nested loops to find all the triplets.
"""

from typing import List


class Solution:
    """
    Runtime 152ms Beats 37.65%
    Memory 17.94MB Beats 19.20%
    """

    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    ans = max(ans, (nums[i] - nums[j]) * nums[k])

        return ans


class Solution2:
    """
    leetcode solution 2: Greedy
    Runtime 14ms Beats 58.10%
    Memory 17.88MB Beats 37.16%
    """

    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for k in range(2, n):
            maxPrefix = nums[0]
            for j in range(1, k):
                res = max(res, (maxPrefix - nums[j]) * nums[k])
                maxPrefix = max(maxPrefix, nums[j])
        return res


class Solution3:
    """
    leetcode solution 3: Greedy + Prefix Suffix Array
    Runtime 0ms Beats 100.00%
    Memory 17.79MB Beats 54.86%
    """

    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        leftMax = [0] * n
        rightMax = [0] * n
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], nums[i - 1])
            rightMax[n - 1 - i] = max(rightMax[n - i], nums[n - i])
        res = 0
        for j in range(1, n - 1):
            res = max(res, (leftMax[j] - nums[j]) * rightMax[j])
        return res


class Solution4:
    """
    leetcode solution 4: Greedy
    Runtime 6ms Beats 66.08%
    Memory 17.86MB Beats 37.16%
    """

    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        res, imax, dmax = 0, 0, 0
        for k in range(n):
            res = max(res, dmax * nums[k])
            dmax = max(dmax, imax - nums[k])
            imax = max(imax, nums[k])
        return res
