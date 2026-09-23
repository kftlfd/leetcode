"""
Leetcode
2026-09-23
1658. Minimum Operations to Reduce X to Zero
Medium

You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

 

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1

Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.

 

Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^4
    1 <= x <= 10^9

 
Hint 1
Think in reverse; instead of finding the minimum prefix + suffix, find the maximum subarray.
Hint 2
Finding the maximum subarray is standard and can be done greedily.
"""


class Solution01:
    """
    Runtime 115ms Beats 28.15%
    Memory 37.94MB Beats 17.41%
    """

    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        total = sum(nums)
        if total == x:
            return n
        if total < x:
            return -1

        hm = {}
        ans = n + 1

        cur_sum = 0
        i = 0
        while i < n and cur_sum < x:
            cur_sum += nums[i]
            i += 1
            hm[cur_sum] = i
            if cur_sum == x:
                ans = min(ans, i)

        cur_sum = 0
        i = 1
        while i >= 0 and cur_sum < x:
            cur_sum += nums[n - i]
            if cur_sum == x:
                ans = min(ans, i)
            compl = hm.get(x - cur_sum, 0)
            if compl > 0 and compl + i <= n:
                ans = min(ans, compl + i)
            i += 1

        return ans if ans < n + 1 else -1


class Solution02:
    """
    Runtime 64ms Beats 83.48%
    Memory 31.74MB Beats 19.28%
    """

    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        target = sum(nums) - x
        if target == 0:
            return n
        if target < 0:
            return -1

        ans = n + 1
        cur_sum = 0
        l = 0

        for r, num in enumerate(nums):
            cur_sum += num
            while cur_sum > target and l <= r:
                cur_sum -= nums[l]
                l += 1
            if cur_sum == target:
                ans = min(ans, n - (r + 1 - l))

        return ans if ans < n + 1 else -1
