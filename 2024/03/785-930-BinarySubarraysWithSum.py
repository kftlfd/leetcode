"""
Leetcode
930. Binary Subarrays With Sum
Medium
2024-03-14

Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

 

Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15

 

Constraints:

    1 <= nums.length <= 3 * 104
    nums[i] is either 0 or 1.
    0 <= goal <= nums.length
"""

from typing import List


class Solution1:
    """
    leetcode solution 1: Prefix Sum
    Runtime: 225 ms, faster than 45.29% of Python3 online submissions for Binary Subarrays With Sum.
    Memory Usage: 20.1 MB, less than 56.59% of Python3 online submissions for Binary Subarrays With Sum.
    """

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        total_count = 0
        current_sum = 0
        # {prefix: number of occurrence}
        freq = {}  # To store the frequency of prefix sums

        for num in nums:
            current_sum += num
            if current_sum == goal:
                total_count += 1

            # Check if there is any prefix sum that can be subtracted from the current sum to get the desired goal
            if current_sum - goal in freq:
                total_count += freq[current_sum - goal]

            freq[current_sum] = freq.get(current_sum, 0) + 1

        return total_count


class Solution2:
    """
    leetcode solution 2: Sliding Window
    Runtime: 227 ms, faster than 37.35% of Python3 online submissions for Binary Subarrays With Sum.
Memory Usage: 17.3 MB, less than 96.40% of Python3 online submissions for Binary Subarrays With Sum.
    """

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.sliding_window_at_most(nums, goal) - self.sliding_window_at_most(nums, goal - 1)

    def sliding_window_at_most(self, nums: List[int], goal: int) -> int:
        start, current_sum, total_count = 0, 0, 0

        # Iterate through the array using a sliding window approach
        for end in range(len(nums)):
            current_sum += nums[end]

            # Adjust the window by moving the start pointer to the right
            # until the sum becomes less than or equal to the goal
            while start <= end and current_sum > goal:
                current_sum -= nums[start]
                start += 1

            # Update the total count by adding the length of the current subarray
            total_count += end - start + 1

        return total_count


class Solution3:
    """
    leetcode solution 3: Sliding Window in One Pass
    Runtime: 213 ms, faster than 85.34% of Python3 online submissions for Binary Subarrays With Sum.
    Memory Usage: 17.5 MB, less than 79.03% of Python3 online submissions for Binary Subarrays With Sum.
    """

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        start = 0
        prefix_zeros = 0
        current_sum = 0
        total_count = 0

        # Loop through the array using end pointer
        for end, num in enumerate(nums):
            # Add current element to the sum
            current_sum += num

            # Slide the window while condition is met
            while start < end and (nums[start] == 0 or current_sum > goal):
                if nums[start] == 1:
                    prefix_zeros = 0
                else:
                    prefix_zeros += 1

                current_sum -= nums[start]
                start += 1

            # Count subarrays when window sum matches the goal
            if current_sum == goal:
                total_count += 1 + prefix_zeros

        return total_count
