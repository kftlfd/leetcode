"""
Leetcode
945. Minimum Increment to Make Array Unique
Medium
2024-06-14

You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.

Return the minimum number of moves to make every value in nums unique.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,2]
Output: 1
Explanation: After 1 move, the array could be [1, 2, 3].

Example 2:

Input: nums = [3,2,1,2,1,7]
Output: 6
Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.

 

Constraints:

    1 <= nums.length <= 10^5
    0 <= nums[i] <= 10^5
"""

from collections import Counter
from typing import List


class Solution:
    """
    Runtime: 684 ms, faster than 13.51% of Python3 online submissions for Minimum Increment to Make Array Unique.
    Memory Usage: 34 MB, less than 15.54% of Python3 online submissions for Minimum Increment to Make Array Unique.
    """

    def minIncrementForUnique(self, nums: List[int]) -> int:
        moves = 0
        cnt = Counter(nums)

        for num in sorted(cnt.keys()):
            if cnt[num] == 1:
                continue

            distribute = cnt[num] - 1
            nxt_num = num + 1
            while nxt_num not in cnt and distribute > 0:
                moves += distribute
                distribute -= 1
                nxt_num += 1

            moves += distribute
            cnt[nxt_num] += distribute

        return moves


class Solution1:
    """
    leetcode solution 1: Sorting
    Runtime: 627 ms, faster than 72.52% of Python3 online submissions for Minimum Increment to Make Array Unique.
    Memory Usage: 30 MB, less than 97.07% of Python3 online submissions for Minimum Increment to Make Array Unique.
    """

    def minIncrementForUnique(self, nums: List[int]) -> int:
        min_increments = 0

        nums = sorted(nums)

        for i in range(1, len(nums)):
            # Ensure each element is greater than its previous
            if nums[i] <= nums[i - 1]:
                # Add the required increment to minIncrements
                increment = nums[i - 1] + 1 - nums[i]
                min_increments += increment

                # Set the element to be greater than its previous
                nums[i] = nums[i - 1] + 1

        return min_increments


class Solution2:
    """
    leetcode solution 2: Counting
    Runtime: 570 ms, faster than 93.69% of Python3 online submissions for Minimum Increment to Make Array Unique.
    Memory Usage: 30 MB, less than 97.07% of Python3 online submissions for Minimum Increment to Make Array Unique.
    """

    def minIncrementForUnique(self, nums: List[int]) -> int:
        n = len(nums)
        max_val = max(nums)
        min_increments = 0

        # Create a frequencyCount array to store the frequency of each value in nums
        frequency_count = [0] * (n + max_val + 1)

        # Populate frequencyCount array with the frequency of each value in nums
        for val in nums:
            frequency_count[val] += 1

        # Iterate over the frequencyCount array to make all values unique
        for i in range(len(frequency_count)):
            if frequency_count[i] <= 1:
                continue

            # Determine excess occurrences, carry them over to the next value,
            # ensure single occurrence for current value, and update min_increments.
            duplicates = frequency_count[i] - 1
            frequency_count[i + 1] += duplicates
            # frequency_count[i] = 1
            min_increments += duplicates

        return min_increments


s = Solution()
tests = [
    ([3, 2, 1, 2, 1, 7],
     6),
]
for inp, exp in tests:
    res = s.minIncrementForUnique(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
