"""
Leetcode
2026-02-10
3719. Longest Balanced Subarray I
Medium

You are given an integer array nums.

A is called balanced if the number of distinct even numbers in the subarray is equal to the number of distinct odd numbers.

Return the length of the longest balanced subarray.

 

Example 1:

Input: nums = [2,5,4,3]

Output: 4

Explanation:

    The longest balanced subarray is [2, 5, 4, 3].
    It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [5, 3]. Thus, the answer is 4.

Example 2:

Input: nums = [3,2,2,5,4]

Output: 5

Explanation:

    The longest balanced subarray is [3, 2, 2, 5, 4].
    It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [3, 5]. Thus, the answer is 5.

Example 3:

Input: nums = [1,2,3,2]

Output: 3

Explanation:

    The longest balanced subarray is [2, 3, 2].
    It has 1 distinct even number [2] and 1 distinct odd number [3]. Thus, the answer is 3.

 

Constraints:

    1 <= nums.length <= 1500
    1 <= nums[i] <= 10^5


Hint 1
Use brute force
Hint 2
Try every subarray and use a map/set data structure to track the distinct even and odd numbers
"""

from typing import List


class Solution:
    """
    Time Limit Exceeded
    """

    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        for length in range(n, 0, -1):
            for l in range(n - length + 1):
                r = l + length
                if self.is_balanced(nums, l, r):
                    return length
        return 0

    def is_balanced(self, nums: List[int], l: int, r: int) -> bool:
        even, odd = set(), set()
        for i in range(l, r):
            num = nums[i]
            if num % 2 == 0:
                even.add(num)
            else:
                odd.add(num)
        return len(even) == len(odd)


class Solution1:
    """
    leetcode solution: Brute Force
    Runtime 1768ms Beats 8.94%
    Memory 19.70MB Beats 34.04%
    """

    def longestBalanced(self, nums: List[int]) -> int:
        max_len = 0

        for i in range(len(nums)):
            odd = {}
            even = {}

            for j in range(i, len(nums)):
                if nums[j] & 1:
                    odd[nums[j]] = odd.get(nums[j], 0) + 1
                else:
                    even[nums[j]] = even.get(nums[j], 0) + 1

                if len(odd) == len(even):
                    max_len = max(max_len, j - i + 1)

        return max_len


class Solution2:
    """
    sample 315ms solution
    Runtime 307ms Beats 94.04%
    Memory 19.79MB Beats 13.62%
    """

    def longestBalanced(self, nums: List[int]) -> int:
        nums = nums[:]
        best = 0
        balance = tuple([set(), set()])
        while len(nums) > best:
            balance[0].clear()
            balance[1].clear()
            for r, x in enumerate(reversed(nums), start=1):
                balance[x & 1].add(x)
                if len(balance[0]) == len(balance[1]):
                    best = max(best, r)
            nums.pop()
        return best
