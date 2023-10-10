"""
Leetcode
2009. Minimum Number of Operations to Make Array Continuous (hard)
2023-10-10

You are given an integer array nums. In one operation, you can replace any element in nums with any integer.

nums is considered continuous if both of the following conditions are fulfilled:

    All elements in nums are unique.
    The difference between the maximum element and the minimum element in nums equals nums.length - 1.

For example, nums = [4, 2, 5, 3] is continuous, but nums = [1, 2, 3, 5, 6] is not continuous.

Return the minimum number of operations to make nums continuous.

 

Example 1:

Input: nums = [4,2,5,3]
Output: 0
Explanation: nums is already continuous.

Example 2:

Input: nums = [1,2,3,5,6]
Output: 1
Explanation: One possible solution is to change the last element to 4.
The resulting array is [1,2,3,5,4], which is continuous.

Example 3:

Input: nums = [1,10,100,1000]
Output: 3
Explanation: One possible solution is to:
- Change the second element to 2.
- Change the third element to 3.
- Change the fourth element to 4.
The resulting array is [1,2,3,4], which is continuous.

 

Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
"""

from typing import List
from bisect import bisect_right


class Solution:
    """
    leetcode solution 1: binary search
    Time: O(n * log(n))
    Space: O(n)
    Runtime: 702 ms, faster than 62.50% of Python3 online submissions for Minimum Number of Operations to Make Array Continuous.
    Memory Usage: 35.4 MB, less than 38.82% of Python3 online submissions for Minimum Number of Operations to Make Array Continuous.
    """

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        nums = sorted(set(nums))

        for i in range(len(nums)):
            left = nums[i]
            right = left + n - 1
            j = bisect_right(nums, right)
            count = j - i
            ans = min(ans, n - count)

        return ans


class Solution1:
    """
    leetcode solution 2: sliding window
    Time: O(n * log(n))
    Space: O(n)
    Runtime: 675 ms, faster than 82.89% of Python3 online submissions for Minimum Number of Operations to Make Array Continuous.
    Memory Usage: 35.2 MB, less than 71.05% of Python3 online submissions for Minimum Number of Operations to Make Array Continuous.
    """

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        nums = sorted(set(nums))
        j = 0

        for i in range(len(nums)):
            while j < len(nums) and nums[j] < nums[i] + n:
                j += 1
            count = j - i
            ans = min(ans, n - count)

        return ans
