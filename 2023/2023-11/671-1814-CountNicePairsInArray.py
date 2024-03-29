"""
Leetcode
1814. Count Nice Pairs in an Array (medium)
2023-11-21

You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:

    0 <= i < j < nums.length
    nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])

Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [42,11,1,97]
Output: 2
Explanation: The two pairs are:
 - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
 - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.

Example 2:

Input: nums = [13,10,35,24,76]
Output: 4

 

Constraints:

    1 <= nums.length <= 10^5
    0 <= nums[i] <= 10^9

Hints:
- The condition can be rearranged to (nums[i] - rev(nums[i])) == (nums[j] - rev(nums[j])).
- Transform each nums[i] into (nums[i] - rev(nums[i])). Then, count the number of (i, j) pairs that have equal values.
- Keep a map storing the frequencies of values that you have seen so far. For each i, check if nums[i] is in the map. If it is, then add that count to the overall count. Then, increment the frequency of nums[i].
"""

from typing import List
from collections import defaultdict


class Solution:
    """
    Runtime: 577 ms, faster than 67.99% of Python3 online submissions for Count Nice Pairs in an Array.
    Memory Usage: 26.9 MB, less than 21.53% of Python3 online submissions for Count Nice Pairs in an Array.
    """

    def countNicePairs(self, nums: List[int]) -> int:
        count = defaultdict(int)

        def rev(num: int) -> int:
            return int(str(num)[::-1])

        for num in nums:
            count[num - rev(num)] += 1

        def pairs(n: int) -> int:
            return n * (n - 1) // 2

        return sum(pairs(n) for n in count.values()) % (10**9 + 7)


class Solution1:
    """
    leetcode solution: Counting With Hash Map
    Runtime: 633 ms, faster than 34.28% of Python3 online submissions for Count Nice Pairs in an Array.
    Memory Usage: 27.1 MB, less than 12.18% of Python3 online submissions for Count Nice Pairs in an Array.
    """

    def countNicePairs(self, nums: List[int]) -> int:
        def rev(num):
            result = 0
            while num:
                result = result * 10 + num % 10
                num //= 10

            return result

        arr = []
        for i in range(len(nums)):
            arr.append(nums[i] - rev(nums[i]))

        dic = defaultdict(int)
        ans = 0
        MOD = 10 ** 9 + 7
        for num in arr:
            ans = (ans + dic[num]) % MOD
            dic[num] += 1

        return ans
