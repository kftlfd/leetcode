"""
Leetcode
995. Minimum Number of K Consecutive Bit Flips
Hard
2024-06-24

You are given a binary array nums and an integer k.

A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [0,1,0], k = 1
Output: 2
Explanation: Flip nums[0], then flip nums[2].

Example 2:

Input: nums = [1,1,0], k = 2
Output: -1
Explanation: No matter how we flip subarrays of size 2, we cannot make the array become [1,1,1].

Example 3:

Input: nums = [0,0,0,1,0,1,1,0], k = 3
Output: 3
Explanation: 
Flip nums[0],nums[1],nums[2]: nums becomes [1,1,1,1,0,1,1,0]
Flip nums[4],nums[5],nums[6]: nums becomes [1,1,1,1,1,0,0,0]
Flip nums[5],nums[6],nums[7]: nums becomes [1,1,1,1,1,1,1,1]

 

Constraints:

    1 <= nums.length <= 10^5
    1 <= k <= nums.length
"""

from collections import deque
from typing import List


class Solution1:
    """
    leetcode solution 1: Using an Auxiliary Array
    Runtime: 802 ms, faster than 50.70% of Python3 online submissions for Minimum Number of K Consecutive Bit Flips.
    Memory Usage: 19.8 MB, less than 35.21% of Python3 online submissions for Minimum Number of K Consecutive Bit Flips.
    """

    def minKBitFlips(self, nums: List[int], k: int) -> int:
        flipped = [False] * len(nums)

        valid_flips_from_past_window = 0

        flip_count = 0

        for i, num in enumerate(nums):
            if i >= k:
                if flipped[i - k]:
                    valid_flips_from_past_window -= 1

            # check if current bit needs to be flipped
            if valid_flips_from_past_window % 2 == num:
                if i + k > len(nums):
                    # flipping the window extends beyond the array len
                    return -1

                valid_flips_from_past_window += 1
                flipped[i] = True
                flip_count += 1

        return flip_count


class Solution2:
    """
    leetcode solution 2: Using a Deque
    Runtime: 798 ms, faster than 59.86% of Python3 online submissions for Minimum Number of K Consecutive Bit Flips.
    Memory Usage: 19.6 MB, less than 76.06% of Python3 online submissions for Minimum Number of K Consecutive Bit Flips.
    """

    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)  # Length of the input list
        flip_queue = deque()  # Queue to keep track of flips
        flipped = 0  # Current flip state
        result = 0  # Total number of flips

        for i, num in enumerate(nums):

            # Remove the effect of the oldest flip if it's out of the current window
            if i >= k:
                flipped ^= flip_queue[0]

            # If the current bit is 0 (i.e., it needs to be flipped)
            if flipped == num:

                # If we cannot flip a subarray starting at index i
                if i + k > n:
                    return -1

                # Add a flip at this position
                flip_queue.append(1)
                flipped ^= 1  # Toggle the flipped state
                result += 1  # Increment the flip count
            else:
                flip_queue.append(0)
            # Remove the oldest flip effect if the queue is longer than k

            if len(flip_queue) > k:
                flip_queue.popleft()
        return result


class Solution3:
    """
    leetcode solution 3: In Constant Space
    Runtime: 781 ms, faster than 86.62% of Python3 online submissions for Minimum Number of K Consecutive Bit Flips.
    Memory Usage: 19.6 MB, less than 51.41% of Python3 online submissions for Minimum Number of K Consecutive Bit Flips.    
    """

    def minKBitFlips(self, nums: List[int], k: int) -> int:
        current_flips = 0  # Tracks the current number of flips
        total_flips = 0  # Tracks the total number of flips

        for i, num in enumerate(nums):
            # If the window slides out of the range and the leftmost element is
            #  marked as flipped (2), decrement current_flips
            if i >= k and nums[i - k] == 2:
                current_flips -= 1

            # Check if the current bit needs to be flipped
            if (current_flips % 2) == num:
                # If flipping would exceed array bounds, return -1
                if i + k > len(nums):
                    return -1
                # Mark the current bit as flipped
                nums[i] = 2
                current_flips += 1
                total_flips += 1

        # Note: We have modified the nums array, but sometimes there are restrictions
        # against changing the input. In such cases, you can restore the original
        # value of nums[i - k] by subtracting 2 (nums[i - k] -= 2;) below the line where
        # we decrement currentFlips--. This way, it will restore its original state
        # before marking it as 2. This technique is a clever way to maintain the original
        # array, but we haven't included it for easier visual understanding.

        return total_flips
