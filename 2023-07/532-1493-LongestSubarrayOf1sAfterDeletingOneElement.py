"""
Leetcode
1493. Longest Subarray of 1's After Deleting One Element (medium)
2023-07-05

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

Constraints:

    1 <= nums.length <= 10^5
    nums[i] is either 0 or 1.
"""

from typing import List


class Solution:
    """
    Runtime: 380 ms, faster than 63.73% of Python3 online submissions for Longest Subarray of 1's After Deleting One Element.
    Memory Usage: 19 MB, less than 72.32% of Python3 online submissions for Longest Subarray of 1's After Deleting One Element.
    """

    def longestSubarray(self, nums: List[int]) -> int:
        prev_block = 0
        curr_block = 0
        separated = False
        max_subarray = 0
        all_ones = True

        for num in nums:
            if num == 1:
                if separated:
                    prev_block = curr_block
                    curr_block = 1
                    separated = False
                else:
                    curr_block += 1
                max_subarray = max(max_subarray, curr_block + prev_block)
                continue

            all_ones = False

            if not separated:
                separated = True
            else:
                prev_block = 0
                curr_block = 0

        ans = max_subarray if not all_ones else max_subarray - 1
        return max(ans, 0)


class Solution1:
    """
    Improved
    https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/solution/1957020
    Runtime: 341 ms, faster than 97.54% of Python3 online submissions for Longest Subarray of 1's After Deleting One Element.
    Memory Usage: 19 MB, less than 41.03% of Python3 online submissions for Longest Subarray of 1's After Deleting One Element.
    """

    def longestSubarray(self, nums: List[int]) -> int:
        max_subarray = 0
        prev = 0
        curr = 0

        for num in nums:
            if num != 1:
                max_subarray = max(max_subarray, prev + curr)
                prev = curr
                curr = 0
            else:
                curr += 1

        max_subarray = max(max_subarray, prev + curr)

        return min(max_subarray, len(nums) - 1)


class Solution2:
    """
    leetcode solution: sliding window
    Runtime: 402 ms, faster than 39.31% of Python3 online submissions for Longest Subarray of 1's After Deleting One Element.
    Memory Usage: 19.2 MB, less than 12.20% of Python3 online submissions for Longest Subarray of 1's After Deleting One Element.
    """

    def longestSubarray(self, nums: List[int]) -> int:
        zero_count = 0  # number of zeros in window
        longest_window = 0
        start = 0  # left end of the window

        for i in range(len(nums)):
            zero_count += nums[i] == 0

            # shrink the window until zero counts come under the limit
            while zero_count > 1:
                zero_count -= nums[start] == 0
                start += 1

            longest_window = max(longest_window, i - start)

        return longest_window


s = Solution1()
tests = [
    ([0, 0, 1, 1],
     2),

    ([0, 0, 0],
     0),

    ([1, 1, 0, 1],
     3),

    ([0, 1, 1, 1, 0, 1, 1, 0, 1],
     5),

    ([1, 1, 1],
     2),
]
for inp, exp in tests:
    res = s.longestSubarray(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
