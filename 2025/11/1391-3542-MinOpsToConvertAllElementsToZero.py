"""
Leetcode
2025-11-10
3542. Minimum Operations to Convert All Elements to Zero
Medium
Topics
premium lock iconCompanies
Hint

You are given an array nums of size n, consisting of non-negative integers. Your task is to apply some (possibly zero) operations on the array so that all elements become 0.

In one operation, you can select a

[i, j] (where 0 <= i <= j < n) and set all occurrences of the minimum non-negative integer in that subarray to 0.

Return the minimum number of operations required to make all elements in the array 0.

 

Example 1:

Input: nums = [0,2]

Output: 1

Explanation:

    Select the subarray [1,1] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [0,0].
    Thus, the minimum number of operations required is 1.

Example 2:

Input: nums = [3,1,2,1]

Output: 3

Explanation:

    Select subarray [1,3] (which is [1,2,1]), where the minimum non-negative integer is 1. Setting all occurrences of 1 to 0 results in [3,0,2,0].
    Select subarray [2,2] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [3,0,0,0].
    Select subarray [0,0] (which is [3]), where the minimum non-negative integer is 3. Setting all occurrences of 3 to 0 results in [0,0,0,0].
    Thus, the minimum number of operations required is 3.

Example 3:

Input: nums = [1,2,1,2,1,2]

Output: 4

Explanation:

    Select subarray [0,5] (which is [1,2,1,2,1,2]), where the minimum non-negative integer is 1. Setting all occurrences of 1 to 0 results in [0,2,0,2,0,2].
    Select subarray [1,1] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [0,0,0,2,0,2].
    Select subarray [3,3] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [0,0,0,0,0,2].
    Select subarray [5,5] (which is [2]), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in [0,0,0,0,0,0].
    Thus, the minimum number of operations required is 4.

 

Constraints:

    1 <= n == nums.length <= 10^5
    0 <= nums[i] <= 10^5


Hint 1
Process the values in nums from smallest to largest (excluding 0).
Hint 2
For each target value v, identify its maximal contiguous segments (subarrays where nums[i] == v); each segment can be zeroed out in one operation.
Hint 3
After setting those segments to zero, dynamically update the remaining array and repeat with the next value. 
"""

from typing import List


class Solution:
    """
    Time Limit Exceeded
    954 / 968 testcases passed
    """

    def minOperations(self, nums: List[int]) -> int:
        return self.solve(nums, 0, len(nums))

    def solve(self, nums: List[int], start: int, end: int) -> int:
        min_val = float('inf')
        min_val_idxs = []
        all_zeroes = True
        cur_start = start
        cur_end = end

        while cur_start < end and nums[cur_start] == 0:
            cur_start += 1

        for i in range(cur_start, end):
            num = nums[i]
            if num == 0:
                cur_end = i
                break
            elif num > 0:
                all_zeroes = False
            if num == min_val:
                min_val_idxs.append(i)
            elif num < min_val:
                min_val = num
                min_val_idxs = [i]

        if all_zeroes or cur_end - cur_start < 1:
            return 0

        ans = 1  # remove all occurences of min_val in single operation
        segments = [cur_start-1] + min_val_idxs + [cur_end]
        for i in range(1, len(segments)):
            if segments[i] - segments[i-1] - 1 < 1:
                continue
            ans += self.solve(nums, segments[i-1] + 1, segments[i])

        if cur_end == end:
            return ans

        return ans + self.solve(nums, cur_end, end)


class Solution1:
    """
    leetcode solution: Monotonic stack
    Runtime 183ms Beats 93.13%
    Memory 28.86MB Beats 100.00%
    """

    def minOperations(self, nums: List[int]) -> int:
        s = []
        res = 0
        for a in nums:
            while s and s[-1] > a:
                s.pop()
            if a == 0:
                continue
            if not s or s[-1] < a:
                res += 1
                s.append(a)
        return res
