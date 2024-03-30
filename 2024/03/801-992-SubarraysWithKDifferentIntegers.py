"""
Leetcode
992. Subarrays with K Different Integers
Hard
2024-03-30

Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

    For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

 

Constraints:

    1 <= nums.length <= 2 * 10^4
    1 <= nums[i], k <= nums.length
"""

from collections import defaultdict
from typing import List, Optional


class Solution1:
    """
    leetcode solution 1: Sliding Window
    Runtime: 331 ms, faster than 76.31% of Python3 online submissions for Subarrays with K Different Integers.
    Memory Usage: 19.8 MB, less than 74.22% of Python3 online submissions for Subarrays with K Different Integers.
    """

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.slidingWindowAtMost(nums, k) - self.slidingWindowAtMost(nums, k - 1)

    # Helper function to count the number of subarrays with at most k distinct elements.
    def slidingWindowAtMost(self, nums: List[int], distinctK: int) -> int:
        # To store the occurrences of each element.
        freq_map = defaultdict(int)
        left = 0
        total_count = 0

        # Right pointer of the sliding window iterates through the array.
        for right in range(len(nums)):
            freq_map[nums[right]] += 1

            # If the number of distinct elements in the window exceeds k,
            # we shrink the window from the left until we have at most k distinct elements.
            while len(freq_map) > distinctK:
                freq_map[nums[left]] -= 1
                if freq_map[nums[left]] == 0:
                    del freq_map[nums[left]]
                left += 1

            # Update the total count by adding the length of the current subarray.
            total_count += right - left + 1

        return total_count


class Solution2:
    """
    leetcode solution 2: Sliding Window in One Pass
    Runtime: 290 ms, faster than 92.22% of Python3 online submissions for Subarrays with K Different Integers.
    Memory Usage: 20.6 MB, less than 17.89% of Python3 online submissions for Subarrays with K Different Integers.
    """

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # Dictionary to store the count of distinct values encountered
        distinct_count = defaultdict(int)

        total_count = 0
        left = 0
        right = 0
        curr_count = 0

        while right < len(nums):
            # Increment the count of the current element in the window
            distinct_count[nums[right]] += 1

            # If encountering a new distinct element, decrement K
            if distinct_count[nums[right]] == 1:
                k -= 1

            # If K becomes negative, adjust the window from the left
            if k < 0:
                # Move the left pointer until the count of distinct elements becomes valid again
                distinct_count[nums[left]] -= 1
                if distinct_count[nums[left]] == 0:
                    k += 1
                left += 1
                curr_count = 0

            # If K becomes zero, calculate subarrays
            if k == 0:
                # While the count of left remains greater than 1, keep shrinking the window from the left
                while distinct_count[nums[left]] > 1:
                    distinct_count[nums[left]] -= 1
                    left += 1
                    curr_count += 1
                # Add the count of subarrays with K distinct elements to the total count
                total_count += (curr_count + 1)

            # Move the right pointer to expand the window
            right += 1

        return total_count
