"""
Leetcode
2026-05-15
153. Find Minimum in Rotated Sorted Array
Medium

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

 

Constraints:

    n == nums.length
    1 <= n <= 5000
    -5000 <= nums[i] <= 5000
    All the integers of nums are unique.
    nums is sorted and rotated between 1 and n times.


Hint 1
Array was originally in ascending order. Now that the array is rotated, there would be a point in the array where there is a small deflection from the increasing sequence. eg. The array would be something like [4, 5, 6, 7, 0, 1, 2].
Hint 2
You can divide the search space into two and see which direction to go. Can you think of an algorithm which has O(logN) search complexity?
Hint 3
 1. All the elements to the left of inflection point > first element of the array.
 2. All the elements to the right of inflection point < first element of the array.
"""

from typing import List, Optional


class Solution01:
    """
    Runtime 0ms Beats 100.00%
    Memory 19.33MB Beats 66.55%
    """

    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        def dfs(l: int, r: int) -> Optional[int]:
            i = (l + r) // 2

            if i + 1 < n and nums[i + 1] < nums[i]:
                return nums[i + 1]

            if l == r:
                return None

            left = dfs(l, i)
            if left is not None:
                return left

            return dfs(i + 1, r)

        ans = dfs(0, n)

        return ans if ans is not None else nums[0]


class Solution02:
    """
    Runtime 0ms Beats 100.00%
    Memory 19.43MB Beats 24.97%
    """

    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        first = nums[0]

        l = 0
        r = n
        ans = first
        while l < r:
            i = (l + r) // 2
            if nums[i] < first:
                ans = nums[i]
                r = i
            else:
                l = i + 1

        return ans
