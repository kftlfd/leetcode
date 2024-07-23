"""
Leetcode
1636. Sort Array by Increasing Frequency
Easy
2024-07-23

Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

 

Example 1:

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

Example 2:

Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.

Example 3:

Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]

 

Constraints:

    1 <= nums.length <= 100
    -100 <= nums[i] <= 100
"""

from typing import Counter, List


class Solution:
    """
    Runtime: 43 ms, faster than 90.09% of Python3 online submissions for Sort Array by Increasing Frequency.
    Memory Usage: 16.5 MB, less than 76.93% of Python3 online submissions for Sort Array by Increasing Frequency.
    """

    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        sorted_nums = sorted(((-freq, num)
                             for num, freq in cnt.items()), reverse=True)

        ans = []
        for _, n in sorted_nums:
            ans += [n] * cnt[n]

        return ans


class Solution1:
    """
    leetcode solution
    Runtime: 51 ms, faster than 49.72% of Python3 online submissions for Sort Array by Increasing Frequency.
    Memory Usage: 16.6 MB, less than 37.68% of Python3 online submissions for Sort Array by Increasing Frequency.
    """

    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        return sorted(nums, key=lambda x: (cnt[x], -x))
