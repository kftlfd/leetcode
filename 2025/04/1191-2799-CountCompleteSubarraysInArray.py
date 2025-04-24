"""
Leetcode
2025-04-24
2799. Count Complete Subarrays in an Array
Medium

You are given an array nums consisting of positive integers.

We call a subarray of an array complete if the following condition is satisfied:

    The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.

Return the number of complete subarrays.

A subarray is a contiguous non-empty part of an array.



Example 1:

Input: nums = [1,3,1,2,2]
Output: 4
Explanation: The complete subarrays are the following: [1,3,1,2], [1,3,1,2,2], [3,1,2] and [3,1,2,2].

Example 2:

Input: nums = [5,5,5,5]
Output: 10
Explanation: The array consists only of the integer 5, so any subarray is complete. The number of subarrays that we can choose is 10.



Constraints:

    1 <= nums.length <= 1000
    1 <= nums[i] <= 2000


Hint 1
Let’s say k is the number of distinct elements in the array. Our goal is to find the number of subarrays with k distinct elements.
Hint 2
Since the constraints are small, you can check every subarray.
"""

from typing import List


class Solution00:
    """
    Time Limit Exceeded 1065 / 1074 testcases passed
    """

    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        k = len(set(nums))
        ans = 0

        for left in range(n - k + 1):
            for right in range(left + k, n + 1):
                if len(set(nums[left:right])) == k:
                    ans += n - right + 1
                    break

        return ans


class Solution1:
    """
    leetcode solution: Sliding Window
    Runtime 15ms Beats 57.69%
    Memory 17.97MB Beats 76.05%
    """

    def countCompleteSubarrays(self, nums: List[int]) -> int:
        res = 0
        cnt = {}
        n = len(nums)
        right = 0
        distinct = len(set(nums))
        for left in range(n):
            if left > 0:
                remove = nums[left - 1]
                cnt[remove] -= 1
                if cnt[remove] == 0:
                    cnt.pop(remove)
            while right < n and len(cnt) < distinct:
                add = nums[right]
                cnt[add] = cnt.get(add, 0) + 1
                right += 1
            if len(cnt) == distinct:
                res += n - right + 1
        return res
