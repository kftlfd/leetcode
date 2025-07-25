"""
Leetcode
2025-07-25
3487. Maximum Unique Subarray Sum After Deletion
Easy

You are given an integer array nums.

You are allowed to delete any number of elements from nums without making it empty. After performing the deletions, select a

of nums such that:

    All elements in the subarray are unique.
    The sum of the elements in the subarray is maximized.

Return the maximum sum of such a subarray.

 

Example 1:

Input: nums = [1,2,3,4,5]

Output: 15

Explanation:

Select the entire array without deleting any element to obtain the maximum sum.

Example 2:

Input: nums = [1,1,0,1,1]

Output: 1

Explanation:

Delete the element nums[0] == 1, nums[1] == 1, nums[2] == 0, and nums[3] == 1. Select the entire array [1] to obtain the maximum sum.

Example 3:

Input: nums = [1,2,-1,-2,1,0,-1]

Output: 3

Explanation:

Delete the elements nums[2] == -1 and nums[3] == -2, and select the subarray [2, 1] from [1, 2, 1, 0, -1] to obtain the maximum sum.

 

Constraints:

    1 <= nums.length <= 100
    -100 <= nums[i] <= 100

    
Hint 1
If the maximum element in the array is less than zero, the answer is the maximum element.
Hint 2
Otherwise, the answer is the sum of all unique values that are greater than or equal to zero.
"""

from typing import List


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.98MB Beats 11.24%
    """

    def maxSum(self, nums: List[int]) -> int:
        seen = [False] * 101
        max_num = nums[0]
        pos_sum = 0

        for num in nums:
            max_num = max(num, max_num)
            if num > 0 and not seen[num]:
                pos_sum += num
                seen[num] = True

        if max_num <= 0:
            return max_num

        return pos_sum


class Solution1:
    """
    leetcode solution: Duplicate Removal for Positive Numbers
    Runtime 0ms Beats 100.00%
    Memory 17.67MB Beats 85.25%
    """

    def maxSum(self, nums: List[int]) -> int:
        positiveNumsSet = set([num for num in nums if num > 0])
        return max(nums) if len(positiveNumsSet) == 0 else sum(positiveNumsSet)
