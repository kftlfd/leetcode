"""
Leetcode
2025-10-22
3347. Maximum Frequency of an Element After Performing Operations II
Hard

You are given an integer array nums and two integers k and numOperations.

You must perform an operation numOperations times on nums, where in each operation you:

    Select an index i that was not selected in any previous operations.
    Add an integer in the range [-k, k] to nums[i].

Return the maximum possible

of any element in nums after performing the operations.

 

Example 1:

Input: nums = [1,4,5], k = 1, numOperations = 2

Output: 2

Explanation:

We can achieve a maximum frequency of two by:

    Adding 0 to nums[1], after which nums becomes [1, 4, 5].
    Adding -1 to nums[2], after which nums becomes [1, 4, 4].

Example 2:

Input: nums = [5,11,20,20], k = 5, numOperations = 1

Output: 2

Explanation:

We can achieve a maximum frequency of two by:

    Adding 0 to nums[1].

 

Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
    0 <= k <= 10^9
    0 <= numOperations <= nums.length

Hint 1
The optimal values to check are nums[i] - k, nums[i], and nums[i] + k.
"""

import bisect
from collections import defaultdict
from typing import List


class Solution:
    """
    leetcode solution: Sort + Enumerate + Binary Search
    Runtime 1136ms Beats 53.23%
    Memory 51.12MB Beats 50.00%
    """

    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        ans = 0
        num_count = defaultdict(int)
        modes = set()

        def add_mode(value):
            modes.add(value)
            if value - k >= nums[0]:
                modes.add(value - k)
            if value + k <= nums[-1]:
                modes.add(value + k)

        last_num_index = 0
        for i in range(n):
            if nums[i] != nums[last_num_index]:
                num_count[nums[last_num_index]] = i - last_num_index
                ans = max(ans, i - last_num_index)
                add_mode(nums[last_num_index])
                last_num_index = i

        num_count[nums[last_num_index]] = n - last_num_index
        ans = max(ans, n - last_num_index)
        add_mode(nums[last_num_index])

        for mode in sorted(modes):
            l = bisect.bisect_left(nums, mode - k)
            r = bisect.bisect_right(nums, mode + k) - 1
            if mode in num_count:
                temp_ans = min(r - l + 1, num_count[mode] + numOperations)
            else:
                temp_ans = min(r - l + 1, numOperations)
            ans = max(ans, temp_ans)

        return ans
