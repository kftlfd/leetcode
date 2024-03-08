"""
Leetcode
3005. Count Elements With Maximum Frequency
Easy
2024-03-08

You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.

 

Example 1:

Input: nums = [1,2,2,3,1,4]
Output: 4
Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
So the number of elements in the array with maximum frequency is 4.

Example 2:

Input: nums = [1,2,3,4,5]
Output: 5
Explanation: All elements of the array have a frequency of 1 which is the maximum.
So the number of elements in the array with maximum frequency is 5.

 

Constraints:

    1 <= nums.length <= 100
    1 <= nums[i] <= 100
"""

from collections import Counter, defaultdict
from typing import List


class Solution:
    """
    Runtime: 46 ms, faster than 41.26% of Python3 online submissions for Count Elements With Maximum Frequency.
    Memory Usage: 16.6 MB, less than 70.06% of Python3 online submissions for Count Elements With Maximum Frequency.
    """

    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        max_freq = cnt.most_common(1)[0][1]
        ans = 0

        for _, freq in cnt.most_common():
            if freq == max_freq:
                ans += freq
            else:
                break

        return ans


class Solution1:
    """
    leetcode solution 3: one-pass sum max frequencies
    Runtime: 35 ms, faster than 94.45% of Python3 online submissions for Count Elements With Maximum Frequency.
    Memory Usage: 16.5 MB, less than 83.74% of Python3 online submissions for Count Elements With Maximum Frequency.
    """

    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqs = defaultdict(int)
        max_freq = 0
        total_freqs = 0

        # Find the frequency of each element
        # Determine the maximum frequency
        # Calculate the total frequencies of elements with the maximum frequency
        for num in nums:
            freqs[num] += 1
            freq = freqs[num]

            # If we discover a higher frequency element
            # Update max_frequency
            # Re-set totalFrequencies to the new max frequency
            if freq > max_freq:
                max_freq = freq
                total_freqs = freq
            # If we find an element with the max frequency, add it to the total
            elif freq == max_freq:
                total_freqs += freq

        return total_freqs
