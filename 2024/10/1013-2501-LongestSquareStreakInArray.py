"""
Leetcode
2024-10-28
2501. Longest Square Streak in an Array
Medium

You are given an integer array nums. A subsequence of nums is called a square streak if:

    The length of the subsequence is at least 2, and
    after sorting the subsequence, each element (except the first element) is the square of the previous number.

Return the length of the longest square streak in nums, or return -1 if there is no square streak.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [4,3,6,16,8,2]
Output: 3
Explanation: Choose the subsequence [4,16,2]. After sorting it, it becomes [2,4,16].
- 4 = 2 * 2.
- 16 = 4 * 4.
Therefore, [4,16,2] is a square streak.
It can be shown that every subsequence of length 4 is not a square streak.

Example 2:

Input: nums = [2,3,5,6,7]
Output: -1
Explanation: There is no square streak in nums so return -1.

 

Constraints:

    2 <= nums.length <= 10^5
    2 <= nums[i] <= 10^5
"""

from typing import List


class Solution:
    """
    Runtime: 239 ms, faster than 16.22% of Python3 online submissions for Longest Square Streak in an Array.
    Memory Usage: 28.8 MB, less than 97.00% of Python3 online submissions for Longest Square Streak in an Array.
    """

    def longestSquareStreak(self, nums: List[int]) -> int:
        n = 10**5 + 1
        num_set = [0] * n  # 0 = not present, 1 = present, -1 = seen

        for num in nums:
            num_set[num] = 1

        ans = 0

        for i in range(2, n):
            if num_set[i] < 1:
                continue
            streak_len = 0
            nxt_pow = i
            while nxt_pow <= n:
                if num_set[nxt_pow] < 1:
                    break
                streak_len += 1
                num_set[nxt_pow] = -1
                nxt_pow = nxt_pow**2
            ans = max(ans, streak_len)

        return ans if ans >= 2 else -1


class Solution1:
    """
    leetcode solution 1: Binary Search
    Runtime: 299 ms, faster than 10.81% of Python3 online submissions for Longest Square Streak in an Array.
    Memory Usage: 28.4 MB, less than 97.00% of Python3 online submissions for Longest Square Streak in an Array.
    """

    def longestSquareStreak(self, nums: List[int]) -> int:
        # Sort the array in ascending order
        nums = sorted(nums)

        # Set to keep track of numbers we've already processed
        processed_numbers = set()

        longest_streak = 0

        # Iterate through each number in the sorted array
        for current in nums:
            # Skip if we've already processed this number
            if current in processed_numbers:
                continue

            streak = current
            streak_length = 1

            # Continue the streak as long as we can find the square of the current number
            while streak * streak <= 10**5:
                if self._binary_search(nums, streak * streak):
                    streak *= streak
                    processed_numbers.add(streak)
                    streak_length += 1
                else:
                    break

            # Update the longest streak if necessary
            longest_streak = max(longest_streak, streak_length)

        # Return -1 if no valid streak found, otherwise return the longest streak
        return longest_streak if longest_streak >= 2 else -1

    # Binary search helper function to efficiently find a value in the sorted array
    def _binary_search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


class Solution2:
    """
    leetcode solution 2: Set
    Runtime: 112 ms, faster than 59.46% of Python3 online submissions for Longest Square Streak in an Array.
    Memory Usage: 33.8 MB, less than 48.00% of Python3 online submissions for Longest Square Streak in an Array.
    """

    def longestSquareStreak(self, nums: List[int]) -> int:
        longest_streak = 0

        # Create a set to store all unique numbers from the input array
        unique_numbers = set(nums)

        # Iterate through each number in the input array
        for start_number in nums:
            current_streak = 0
            current = start_number

            # Continue the streak as long as we can find the next square in the set
            while current in unique_numbers:
                current_streak += 1

                # Break if the next square would be larger than 10^5 (problem constraint)
                if current * current > 10**5:
                    break

                current *= current

            # Update the longest streak if necessary
            longest_streak = max(longest_streak, current_streak)

        # Return -1 if no valid streak found, otherwise return the longest streak
        return longest_streak if longest_streak >= 2 else -1


class Solution3:
    """
    leetcode solution 3: Map
    Runtime: 138 ms, faster than 45.95% of Python3 online submissions for Longest Square Streak in an Array.
    Memory Usage: 37.6 MB, less than 13.00% of Python3 online submissions for Longest Square Streak in an Array.
    """

    def longestSquareStreak(self, nums: List[int]) -> int:
        # Dictionary to store the length of square streak for each number
        streak_lengths = {}

        nums = sorted(nums)

        for number in nums:
            root = int(number**0.5)

            # Check if the number is a perfect square and its square root is in the dictionary
            if root * root == number and root in streak_lengths:
                # Extend the streak from its square root
                streak_lengths[number] = streak_lengths[root] + 1
            else:
                # Start a new streak
                streak_lengths[number] = 1

        # Find the maximum streak length
        longest_streak = max(streak_lengths.values(), default=0)

        # Return -1 if no valid streak found, otherwise return the longest streak
        return longest_streak if longest_streak > 1 else -1
