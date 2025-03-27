"""
Leetcode
2025-03-27
2780. Minimum Index of a Valid Split
Medium

An element x of an integer array arr of length m is dominant if more than half the elements of arr have a value of x.

You are given a 0-indexed integer array nums of length n with one dominant element.

You can split nums at an index i into two arrays nums[0, ..., i] and nums[i + 1, ..., n - 1], but the split is only valid if:

    0 <= i < n - 1
    nums[0, ..., i], and nums[i + 1, ..., n - 1] have the same dominant element.

Here, nums[i, ..., j] denotes the subarray of nums starting at index i and ending at index j, both ends being inclusive. Particularly, if j < i then nums[i, ..., j] denotes an empty subarray.

Return the minimum index of a valid split. If no valid split exists, return -1.

 

Example 1:

Input: nums = [1,2,2,2]
Output: 2
Explanation: We can split the array at index 2 to obtain arrays [1,2,2] and [2]. 
In array [1,2,2], element 2 is dominant since it occurs twice in the array and 2 * 2 > 3. 
In array [2], element 2 is dominant since it occurs once in the array and 1 * 2 > 1.
Both [1,2,2] and [2] have the same dominant element as nums, so this is a valid split. 
It can be shown that index 2 is the minimum index of a valid split. 

Example 2:

Input: nums = [2,1,3,1,1,1,7,1,2,1]
Output: 4
Explanation: We can split the array at index 4 to obtain arrays [2,1,3,1,1] and [1,7,1,2,1].
In array [2,1,3,1,1], element 1 is dominant since it occurs thrice in the array and 3 * 2 > 5.
In array [1,7,1,2,1], element 1 is dominant since it occurs thrice in the array and 3 * 2 > 5.
Both [2,1,3,1,1] and [1,7,1,2,1] have the same dominant element as nums, so this is a valid split.
It can be shown that index 4 is the minimum index of a valid split.

Example 3:

Input: nums = [3,3,3,3,7,2,2]
Output: -1
Explanation: It can be shown that there is no valid split.

 

Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
    nums has exactly one dominant element.


Hint 1
Find the dominant element of nums by using a hashmap to maintain element frequency, we denote the dominant element as x and its frequency as f.
Hint 2
For each index in [0, n - 2], calculate f1, x’s frequency in the subarray [0, i] when looping the index. And f2, x’s frequency in the subarray [i + 1, n - 1] which is equal to f - f1. Then we can check whether x is dominant in both subarrays.
"""

from collections import Counter, defaultdict
from typing import List


class Solution01:
    """
    Wrong Answer
    """

    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        dominant, dom_total = Counter(nums).most_common(1)[0]

        cur = 0
        pref_sum = [0] * n
        for i, num in enumerate(nums):
            if num == dominant:
                cur += 1
            pref_sum[i] = cur

        def is_valid(i: int) -> bool:
            return pref_sum[i] * 2 > (i + 1) and (dom_total - pref_sum[i]) * 2 > (n - i - 1)

        left = 0
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            if is_valid(mid):
                right = mid
            else:
                left = mid + 1

        return right if right < n - 1 else -1


class Solution02:
    """
    Runtime 70ms Beats 52.48%
    Memory 33.34MB Beats 59.90%
    """

    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        dominant, dom_total = Counter(nums).most_common(1)[0]

        cur = 0
        pref_sum = [0] * n
        for i, num in enumerate(nums):
            if num == dominant:
                cur += 1
            pref_sum[i] = cur

        for i in range(n - 1):
            if pref_sum[i] * 2 > (i + 1) and (dom_total - pref_sum[i]) * 2 > (n - i - 1):
                return i

        return -1


class Solution1:
    """
    leetcode solution 1: Hash Map
    Runtime 115ms Beats 24.26%
    Memory 34.61MB Beats 24.26%
    """

    def minimumIndex(self, nums: List[int]) -> int:
        first_map = defaultdict(int)
        second_map = defaultdict(int)
        n = len(nums)

        # Add all elements of nums to second_map
        for num in nums:
            second_map[num] += 1

        for index in range(n):
            # Create split at current index
            num = nums[index]
            second_map[num] -= 1
            first_map[num] += 1

            # Check if valid split
            if (
                first_map[num] * 2 > index + 1
                and second_map[num] * 2 > n - index - 1
            ):
                return index

        # No valid split exists
        return -1


class Solution2:
    """
    leetcode solution 2: Boyer-Moore Majority Voting Algorithm
    Runtime 56ms Beats 67.33%
    Memory 32.05MB Beats 80.20%
    """

    def minimumIndex(self, nums: List[int]) -> int:
        # Find the majority element
        x = nums[0]
        count = 0
        x_count = 0
        n = len(nums)

        for num in nums:
            if num == x:
                count += 1
            else:
                count -= 1
            if count == 0:
                x = num
                count = 1

        # Count frequency of majority element
        for num in nums:
            if num == x:
                x_count += 1

        # Check if valid split is possible
        count = 0
        for index in range(n):
            if nums[index] == x:
                count += 1
            remaining_count = x_count - count
            if count * 2 > index + 1 and remaining_count * 2 > n - index - 1:
                return index

        return -1


s = Solution02()
tests = [
    ([2, 1, 3, 1, 1, 1, 7, 1, 2, 1],
     4),
]
for inp, exp in tests:
    res = s.minimumIndex(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
