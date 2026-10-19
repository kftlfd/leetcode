"""
Leetcode
2026-10-19
2089. Find Target Indices After Sorting Array
Easy

You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

 

Example 1:

Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
Explanation: After sorting, nums is [1,2,2,3,5].
The indices where nums[i] == 2 are 1 and 2.

Example 2:

Input: nums = [1,2,5,2,3], target = 3
Output: [3]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 3 is 3.

Example 3:

Input: nums = [1,2,5,2,3], target = 5
Output: [4]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 5 is 4.

 

Constraints:

    1 <= nums.length <= 100
    1 <= nums[i], target <= 100


"""


class Solution:
    """
    Runtime 1ms Beats 33.47%
    Memory 19.14MB Beats 90.46%
    """

    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        return [i for i, num in enumerate(sorted(nums)) if num == target]


class Solution2:
    """
    leetcode solution 2: Count Directly
    Runtime 0ms Beats 100.00%
    Memory 18.83MB Beats 99.80%
    """

    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        cnt1 = 0  # Number of elements less than target
        cnt2 = 0  # Number of elements equal to target
        for num in nums:
            if num < target:
                cnt1 += 1
            elif num == target:
                cnt2 += 1
        res = list(range(cnt1, cnt1 + cnt2))  # Array of indices
        return res
