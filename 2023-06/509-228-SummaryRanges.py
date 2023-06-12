"""
Leetcode
228. Summary Ranges (easy)
2023-06-12

You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

    "a->b" if a != b
    "a" if a == b

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

Constraints:

    0 <= nums.length <= 20
    -2^31 <= nums[i] <= 2^31 - 1
    All the values of nums are unique.
    nums is sorted in ascending order.
"""

from typing import List


class Solution:
    """
    Runtime: 50 ms, faster than 26.46% of Python3 online submissions for Summary Ranges.
    Memory Usage: 16.4 MB, less than 26.14% of Python3 online submissions for Summary Ranges.
    """

    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        out = []

        cur_start = nums[0]
        cur_end = nums[0]

        def save_range():
            if cur_start == cur_end:
                out.append(f"{cur_start}")
            else:
                out.append(f"{cur_start}->{cur_end}")

        for i in range(1, len(nums)):
            num = nums[i]
            if num == cur_end + 1:
                cur_end = num
                continue
            save_range()
            cur_start = num
            cur_end = num

        save_range()

        return out


class Solution1:
    """
    leetcode solution
    Runtime: 54 ms, faster than 7.89% of Python3 online submissions for Summary Ranges.
    Memory Usage: 16.4 MB, less than 26.14% of Python3 online submissions for Summary Ranges.
    """

    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        i = 0

        while i < len(nums):
            start = nums[i]
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                i += 1

            if start != nums[i]:
                ranges.append(str(start) + "->" + str(nums[i]))
            else:
                ranges.append(str(nums[i]))

            i += 1

        return ranges


s = Solution()
tests = [
    ([0, 1, 2, 4, 5, 7],
     ["0->2", "4->5", "7"]),

    ([0, 2, 3, 4, 6, 8, 9],
     ["0", "2->4", "6", "8->9"]),
]
for inp, exp in tests:
    res = s.summaryRanges(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
