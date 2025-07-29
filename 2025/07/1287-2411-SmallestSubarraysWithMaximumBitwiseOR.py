"""
Leetcode
2025-07-29
2411. Smallest Subarrays With Maximum Bitwise OR
Medium

You are given a 0-indexed array nums of length n, consisting of non-negative integers. For each index i from 0 to n - 1, you must determine the size of the minimum sized non-empty subarray of nums starting at i (inclusive) that has the maximum possible bitwise OR.

    In other words, let Bij be the bitwise OR of the subarray nums[i...j]. You need to find the smallest subarray starting at i, such that bitwise OR of this subarray is equal to max(Bik) where i <= k <= n - 1.

The bitwise OR of an array is the bitwise OR of all the numbers in it.

Return an integer array answer of size n where answer[i] is the length of the minimum sized subarray starting at i with maximum bitwise OR.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,0,2,1,3]
Output: [3,3,2,2,1]
Explanation:
The maximum possible bitwise OR starting at any index is 3. 
- Starting at index 0, the shortest subarray that yields it is [1,0,2].
- Starting at index 1, the shortest subarray that yields the maximum bitwise OR is [0,2,1].
- Starting at index 2, the shortest subarray that yields the maximum bitwise OR is [2,1].
- Starting at index 3, the shortest subarray that yields the maximum bitwise OR is [1,3].
- Starting at index 4, the shortest subarray that yields the maximum bitwise OR is [3].
Therefore, we return [3,3,2,2,1]. 

Example 2:

Input: nums = [1,2]
Output: [2,1]
Explanation:
Starting at index 0, the shortest subarray that yields the maximum bitwise OR is of length 2.
Starting at index 1, the shortest subarray that yields the maximum bitwise OR is of length 1.
Therefore, we return [2,1].

 

Constraints:

    n == nums.length
    1 <= n <= 10^5
    0 <= nums[i] <= 10^9


Hint 1
Consider trying to solve the problem for each bit position separately.
Hint 2
For each bit position, find the position of the next number that has a 1 in that position, if any.
Hint 3
Take the maximum distance to such a number, including the current number.
Hint 4
Iterate backwards to achieve a linear complexity.
"""

from math import inf
from typing import List


class Solution00:
    """
    Time Limit Exceeded 57 / 59 testcases passed
    """

    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        max_or = 0

        for i in range(n-1, -1, -1):
            max_or |= nums[i]
            cur_or = 0

            for j in range(i, n):
                cur_or |= nums[j]
                if cur_or == max_or:
                    ans[i] = j - i + 1
                    break

        return ans


class Solution01:
    """
    Runtime 1386ms Beats 18.11%
    Memory 28.98MB Beats 86.61%
    """

    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        bit_dist = [0] * 30

        for i in range(n-1, -1, -1):
            max_dist = i

            for b in range(30):
                mask = 1 << b
                if nums[i] & mask == mask:
                    bit_dist[b] = i
                max_dist = max(max_dist, bit_dist[b])

            ans[i] = max_dist - i + 1

        return ans


class Solution1:
    """
    leetcode solution: Enumeration
    Runtime 966ms Beats 38.58%
    Memory 29.00MB Beats 66.14%
    """

    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos = [-1] * 31
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            j = i
            for bit in range(31):
                if (nums[i] & (1 << bit)) == 0:
                    if pos[bit] != -1:
                        j = max(j, pos[bit])
                else:
                    pos[bit] = i
            ans[i] = j - i + 1
        return ans


class Solution2:
    """
    sample 122ms solution
    Runtime 111ms Beats 97.64%
    Memory 29.66MB Beats 48.82%
    """

    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        nums = nums[:]
        length = len(nums)
        res = [inf] * length
        for i in range(length):
            x = nums[i]
            res[i] = 1
            j = i - 1
            while j >= 0 and nums[j] | x != nums[j]:
                res[j] = i - j + 1
                nums[j] |= x
                j -= 1
        return res  # type: ignore
