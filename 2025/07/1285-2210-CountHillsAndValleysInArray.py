"""
Leetcode
2025-07-27
2210. Count Hills and Valleys in an Array
Easy

You are given a 0-indexed integer array nums. An index i is part of a hill in nums if the closest non-equal neighbors of i are smaller than nums[i]. Similarly, an index i is part of a valley in nums if the closest non-equal neighbors of i are larger than nums[i]. Adjacent indices i and j are part of the same hill or valley if nums[i] == nums[j].

Note that for an index to be part of a hill or valley, it must have a non-equal neighbor on both the left and right of the index.

Return the number of hills and valleys in nums.

 

Example 1:

Input: nums = [2,4,1,1,6,5]
Output: 3
Explanation:
At index 0: There is no non-equal neighbor of 2 on the left, so index 0 is neither a hill nor a valley.
At index 1: The closest non-equal neighbors of 4 are 2 and 1. Since 4 > 2 and 4 > 1, index 1 is a hill. 
At index 2: The closest non-equal neighbors of 1 are 4 and 6. Since 1 < 4 and 1 < 6, index 2 is a valley.
At index 3: The closest non-equal neighbors of 1 are 4 and 6. Since 1 < 4 and 1 < 6, index 3 is a valley, but note that it is part of the same valley as index 2.
At index 4: The closest non-equal neighbors of 6 are 1 and 5. Since 6 > 1 and 6 > 5, index 4 is a hill.
At index 5: There is no non-equal neighbor of 5 on the right, so index 5 is neither a hill nor a valley. 
There are 3 hills and valleys so we return 3.

Example 2:

Input: nums = [6,6,5,5,4,1]
Output: 0
Explanation:
At index 0: There is no non-equal neighbor of 6 on the left, so index 0 is neither a hill nor a valley.
At index 1: There is no non-equal neighbor of 6 on the left, so index 1 is neither a hill nor a valley.
At index 2: The closest non-equal neighbors of 5 are 6 and 4. Since 5 < 6 and 5 > 4, index 2 is neither a hill nor a valley.
At index 3: The closest non-equal neighbors of 5 are 6 and 4. Since 5 < 6 and 5 > 4, index 3 is neither a hill nor a valley.
At index 4: The closest non-equal neighbors of 4 are 5 and 1. Since 4 < 5 and 4 > 1, index 4 is neither a hill nor a valley.
At index 5: There is no non-equal neighbor of 1 on the right, so index 5 is neither a hill nor a valley.
There are 0 hills and valleys so we return 0.

 

Constraints:

    3 <= nums.length <= 100
    1 <= nums[i] <= 100


Hint 1
For each index, could you find the closest non-equal neighbors?
Hint 2
Ensure that adjacent indices that are part of the same hill or valley are not double-counted.
"""

from typing import List


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.92MB Beats 20.24%
    """

    def countHillValley(self, nums: List[int]) -> int:
        arr = []
        for num in nums:
            if not arr or arr[-1] != num:
                arr.append(num)

        ans = 0

        for i in range(1, len(arr) - 1):
            left, cur, right = arr[i-1:i+2]
            if (left < cur > right) or (left > cur < right):
                ans += 1

        return ans


class Solution1:
    """
    leetcode solution: Count the Number of Peaks and Valleys in the Array
    Runtime 4ms Beats 5.78%
    Memory 17.68MB Beats 90.84%
    """

    def countHillValley(self, nums: List[int]) -> int:
        res = 0  # number of peaks and valleys
        n = len(nums)
        for i in range(1, n - 1):
            if nums[i] == nums[i - 1]:
                # deduplication
                continue
            left = (
                0  # left side possibly unequal neighboring corresponding state
            )
            for j in range(i - 1, -1, -1):
                if nums[j] > nums[i]:
                    left = 1
                    break
                elif nums[j] < nums[i]:
                    left = -1
                    break
            right = (
                0  # right side possibly unequal neighboring corresponding state
            )
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    right = 1
                    break
                elif nums[j] < nums[i]:
                    right = -1
                    break
            if left == right and left != 0:
                # at this time, index i is part of a peak or valley.
                res += 1
        return res


class Solution2:
    """
    https://leetcode.com/problems/count-hills-and-valleys-in-an-array/editorial/comments/3095416/
    Runtime 0ms Beats 100.00%
    Memory 17.68MB Beats 90.84%
    """

    def countHillValley(self, nums: List[int]) -> int:
        left = nums[0]
        count = 0
        for i in range(1, len(nums) - 1):
            cur, right = nums[i], nums[i + 1]
            if cur != right:
                if left < cur > right or left > cur < right:
                    count += 1
                left = cur
        return count
