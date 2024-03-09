"""
Leetcode
2540. Minimum Common Value
Easy
2024-03-09

Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

 

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4]
Output: 2
Explanation: The smallest element common to both arrays is 2, so we return 2.

Example 2:

Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
Output: 2
Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.

 

Constraints:

    1 <= nums1.length, nums2.length <= 105
    1 <= nums1[i], nums2[j] <= 109
    Both nums1 and nums2 are sorted in non-decreasing order.
"""

from typing import List


class Solution:
    """
    Runtime: 379 ms, faster than 19.77% of Python3 online submissions for Minimum Common Value.
    Memory Usage: 35.5 MB, less than 87.52% of Python3 online submissions for Minimum Common Value.
    """

    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        idx1 = 0
        idx2 = 0

        while idx1 < n1 and idx2 < n2:
            if nums1[idx1] == nums2[idx2]:
                break

            if nums1[idx1] < nums2[idx2]:
                idx1 += 1
            else:
                idx2 += 1

        return nums1[idx1] if idx1 < n1 and idx2 < n2 else -1


class Solution1:
    """
    leetcode solution 3: binary search
    Runtime: 465 ms, faster than 11.87% of Python3 online submissions for Minimum Common Value.
    Memory Usage: 35.5 MB, less than 73.75% of Python3 online submissions for Minimum Common Value.
    """

    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        def binary_search(target, nums):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    return True
            return False

        # Binary search should be done on the larger array
        # If nums1 is longer, call getCommon with the arrays swapped
        if len(nums1) > len(nums2):
            return self.getCommon(nums2, nums1)

        # Search for each element of nums1 in nums2
        # Return the first common element found
        for num in nums1:
            if binary_search(num, nums2):
                return num

        # Return -1 if there are no common elements
        return -1
