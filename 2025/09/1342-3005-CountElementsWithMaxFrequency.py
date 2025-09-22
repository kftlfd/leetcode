"""
Leetcode
2025-09-22
3005. Count Elements With Maximum Frequency
Easy

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

from collections import Counter
from typing import List


class Solution:
    """
    Runtime 4ms Beats 10.47%
    Memory 17.78MB Beats 58.05%
    """

    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = [0] * 101

        for num in nums:
            freq[num] += 1

        max_freq = 0
        total_freq = 0

        for freq in freq:
            if freq == max_freq:
                total_freq += freq
            elif freq > max_freq:
                max_freq = freq
                total_freq = freq

        return total_freq


class Solution2:
    """
    leetcode solution 2: Sort Frequencies and Sum Max Frequencies
    Runtime 3ms Beats 34.62%
    Memory 17.58MB Beats 97.86%
    """

    def maxFrequencyElements(self, nums: List[int]) -> int:
        # Find the frequency of each element
        frequencies = [0] * 100
        for num in nums:
            frequencies[num - 1] += 1

        # Determine the maximum frequency, stored in the last index of the sorted array
        frequencies.sort()
        max_freq_index = len(frequencies) - 1
        total_frequencies = frequencies[max_freq_index]

        # Calculate the total frequencies of elements with the maximum frequency
        # Start from the last index and iterate right to left
        while max_freq_index > 0 and frequencies[max_freq_index] == frequencies[max_freq_index - 1]:
            total_frequencies += frequencies[max_freq_index]
            max_freq_index -= 1
        return total_frequencies


class Solution3:
    """
    leetcode solution 3: One-Pass Sum Max Frequencies
    Runtime 4ms Beats 10.47%
    Memory 17.80MB Beats 58.05%
    """

    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequencies = {}
        max_frequency = 0
        total_frequencies = 0

        # Find the frequency of each element
        # Determine the maximum frequency
        # Calculate the total frequencies of elements with the maximum frequency
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
            frequency = frequencies[num]

            # If we discover a higher frequency element
            # Update max_frequency
            # Re-set totalFrequencies to the new max frequency
            if frequency > max_frequency:
                max_frequency = frequency
                total_frequencies = frequency
            # If we find an element with the max frequency, add it to the total
            elif frequency == max_frequency:
                total_frequencies += frequency

        return total_frequencies


class Solution4:
    """
    sample 0ms solution
    Runtime 0ms Beats 100.00%
    Memory 17.77MB Beats 58.05%
    """

    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        maxf = max(freq.values())
        return sum(v for v in freq.values() if v == maxf)
