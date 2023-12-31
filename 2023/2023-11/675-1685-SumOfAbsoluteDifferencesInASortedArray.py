"""
Leetcode
1685. Sum of Absolute Differences in a Sorted Array (medium)
2023-11-25

You are given an integer array nums sorted in non-decreasing order.

Build and return an integer array result with the same length as nums such that result[i] is equal to the summation of absolute differences between nums[i] and all the other elements in the array.

In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j < nums.length and j != i (0-indexed).

 

Example 1:

Input: nums = [2,3,5]
Output: [4,3,5]
Explanation: Assuming the arrays are 0-indexed, then
result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.

Example 2:

Input: nums = [1,4,6,8,10]
Output: [24,15,13,15,21]

 

Constraints:

    2 <= nums.length <= 10^5
    1 <= nums[i] <= nums[i + 1] <= 10^4

Hints:
- Absolute difference is the same as max(a, b) - min(a, b). How can you use this fact with the fact that the array is sorted?
- For nums[i], the answer is (nums[i] - nums[0]) + (nums[i] - nums[1]) + ... + (nums[i] - nums[i-1]) + (nums[i+1] - nums[i]) + (nums[i+2] - nums[i]) + ... + (nums[n-1] - nums[i]).
- It can be simplified to (nums[i] * i - (nums[0] + nums[1] + ... + nums[i-1])) + ((nums[i+1] + nums[i+2] + ... + nums[n-1]) - nums[i] * (n-i-1)). One can build prefix and suffix sums to compute this quickly.
"""

from typing import List


class Solution:
    """
    Runtime: 740 ms, faster than 43.31% of Python3 online submissions for Sum of Absolute Differences in a Sorted Array.
    Memory Usage: 32 MB, less than 20.38% of Python3 online submissions for Sum of Absolute Differences in a Sorted Array.
    """

    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:

        n = len(nums)

        prefix_sums = nums[:]
        for i in range(1, n):
            prefix_sums[i] += prefix_sums[i - 1]
        total_sum = prefix_sums[-1]

        ans = [0] * n

        for i, num in enumerate(nums):
            cur_sum = prefix_sums[i]
            prefix = cur_sum - num
            suffix = total_sum - cur_sum
            ans[i] = (num * i - prefix) + (suffix - num * (n - i - 1))

        return ans


class Solution1:
    """
    leetcode solution 2: Calculating Prefix Sum on the Fly
    Runtime: 702 ms, faster than 87.58% of Python3 online submissions for Sum of Absolute Differences in a Sorted Array.
    Memory Usage: 31.8 MB, less than 51.59% of Python3 online submissions for Sum of Absolute Differences in a Sorted Array.
    """

    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:

        n = len(nums)
        total_sum = sum(nums)
        left_sum = 0
        ans = []

        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]

            left_count = i
            right_count = n - 1 - i

            left_total = left_count * nums[i] - left_sum
            right_total = right_sum - right_count * nums[i]

            ans.append(left_total + right_total)
            left_sum += nums[i]

        return ans
