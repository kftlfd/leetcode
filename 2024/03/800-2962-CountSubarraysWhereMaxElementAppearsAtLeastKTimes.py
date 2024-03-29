"""
Leetcode
2962. Count Subarrays Where Max Element Appears at Least K Times
Medium
2024-03-29

You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.

 

Example 1:

Input: nums = [1,3,2,3,3], k = 2
Output: 6
Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].

Example 2:

Input: nums = [1,4,2,1], k = 3
Output: 0
Explanation: No subarray contains the element 4 at least 3 times.

 

Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^6
    1 <= k <= 10^5
"""

from typing import List


class Solution1:
    """
    leetcode solution 1: Sliding Window
    Runtime: 827 ms, faster than 98.47% of Python3 online submissions for Count Subarrays Where Max Element Appears at Least K Times.
    Memory Usage: 30.9 MB, less than 56.87% of Python3 online submissions for Count Subarrays Where Max Element Appears at Least K Times.
    """

    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        ans = start = max_elements_in_window = 0

        for end in range(len(nums)):
            if nums[end] == max_element:
                max_elements_in_window += 1
            while max_elements_in_window == k:
                if nums[start] == max_element:
                    max_elements_in_window -= 1
                start += 1
            ans += start
        return ans


class Solution2:
    """
    leetcode solution 2: Track Indexes of Max Element
    Runtime: 869 ms, faster than 66.03% of Python3 online submissions for Count Subarrays Where Max Element Appears at Least K Times.
    Memory Usage: 30.9 MB, less than 80.15% of Python3 online submissions for Count Subarrays Where Max Element Appears at Least K Times.
    """

    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        indexes_of_max_elements = []
        ans = 0

        for index, element in enumerate(nums):

            if element == max_element:
                indexes_of_max_elements.append(index)

            freq = len(indexes_of_max_elements)
            if freq >= k:
                ans += indexes_of_max_elements[-k] + 1

        return ans
