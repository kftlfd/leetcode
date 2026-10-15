"""
Leetcode
2026-10-15
2913. Subarrays Distinct Element Sum of Squares I
Easy

You are given a 0-indexed integer array nums.

The distinct count of a subarray of nums is defined as:

    Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].

Return the sum of the squares of distinct counts of all subarrays of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,1]
Output: 15
Explanation: Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 + 22 + 22 + 22 = 15.

Example 2:

Input: nums = [1,1]
Output: 3
Explanation: Three possible subarrays are:
[1]: 1 distinct value
[1]: 1 distinct value
[1,1]: 1 distinct value
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 = 3.

 

Constraints:

    1 <= nums.length <= 100
    1 <= nums[i] <= 100


"""

from collections import defaultdict
from typing import List


class Solution:
    """
    Runtime 19ms Beats 82.77%
    Memory 18.83MB Beats 99.38%
    """

    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for i in range(n):
            cnt = {nums[i]}
            ans += 1
            for j in range(i + 1, n):
                cnt.add(nums[j])
                ans += len(cnt)**2

        return ans


class Solution2:
    """
    leetcode solution 2: Binary Indexed Tree
    Runtime 29ms Beats 51.38%
    Memory 19.11MB Beats 91.08%
    """

    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        res = cur = 0
        bit = self.BIT(n + 10)
        seen = {}
        mod = 10**9 + 7
        for i, a in enumerate(nums):
            j = seen.get(a, -1) + 1
            cur += bit.query(j, i) * 2 + i - j + 1
            res += cur
            bit.add(j, i, 1)
            seen[a] = i
        return res % mod

    class BIT:
        def __init__(self, n: int):
            self.size = n
            self._tree1 = defaultdict(int)
            self._tree2 = defaultdict(int)

        def _lowbit(self, index: int) -> int:
            return index & -index

        def add(self, left: int, right: int, delta: int) -> None:
            self._add(left, delta)
            self._add(right + 1, -delta)

        def query(self, left: int, right: int) -> int:
            return self._query(right) - self._query(left - 1)

        def _add(self, index: int, delta: int) -> None:
            index += 1
            if index < 0:
                raise ValueError("index must be a positive integer")

            rawIndex = index
            while index <= self.size:
                self._tree1[index] += delta
                self._tree2[index] += (rawIndex - 1) * delta
                index += self._lowbit(index)

        def _query(self, index: int) -> int:
            index += 1
            if index > self.size:
                index = self.size

            rawIndex = index
            res = 0
            while index > 0:
                res += rawIndex * self._tree1[index] - self._tree2[index]
                index -= self._lowbit(index)
            return res
