"""
Leetcode
229. Majority Element II (medium)
2023-10-05

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]

Example 2:

Input: nums = [1]
Output: [1]

Example 3:

Input: nums = [1,2]
Output: [1,2]

 

Constraints:

    1 <= nums.length <= 5 * 10^4
    -10^9 <= nums[i] <= 10^9
"""

from typing import List
from collections import Counter


class Solution:
    """
    Runtime: 114 ms, faster than 41.15% of Python3 online submissions for Majority Element II.
    Memory Usage: 17.7 MB, less than 84.36% of Python3 online submissions for Majority Element II.
    """

    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) // 3
        count = Counter(nums)
        return [num for num, freq in count.items() if freq > n]


class Solution1:
    """
    https://leetcode.com/problems/majority-element-ii/discuss/858872/Python-Voting-O(n)-solution-explained
    Runtime: 123 ms, faster than 11.93% of Python3 online submissions for Majority Element II.
    Memory Usage: 17.7 MB, less than 84.36% of Python3 online submissions for Majority Element II.
    """

    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter()
        for num in nums:
            count[num] += 1
            if len(count) == 3:
                new_count = Counter()
                for elem, freq in count.items():
                    if freq != 1:
                        new_count[elem] = freq - 1
                count = new_count

        cands = Counter(num for num in nums if num in count)
        return [num for num in cands if cands[num] > len(nums)/3]
