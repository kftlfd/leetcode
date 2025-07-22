"""
Leetcode
2025-07-22
1695. Maximum Erasure Value
Medium

You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

 

Example 1:

Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].

Example 2:

Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].

 

Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^4


Hint 1
The main point here is for the subarray to contain unique elements for each index. Only the first subarrays starting from that index have unique elements.
Hint 2
This can be solved using the two pointers technique
"""

from typing import List


class Solution:
    """
    Runtime 222ms Beats 54.17%
    Memory 29.00MB Beats 30.06%
    """

    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = 0
        window = set()
        cur_sum = 0
        left = 0

        for right in nums:
            while right in window:
                cur_sum -= nums[left]
                window.remove(nums[left])
                left += 1
            window.add(right)
            cur_sum += right
            ans = max(ans, cur_sum)

        return ans


class Solution1:
    """
    Runtime 115ms Beats 99.63%
    Memory 28.97MB Beats 30.06%
    """

    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = 0
        window = [False] * 10001
        cur_sum = 0
        l = 0

        for right in nums:
            while window[right]:
                left = nums[l]
                cur_sum -= left
                window[left] = False
                l += 1
            window[right] = True
            cur_sum += right
            ans = max(ans, cur_sum)

        return ans
