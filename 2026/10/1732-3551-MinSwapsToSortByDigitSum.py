"""
Leetcode
2026-10-17
3551. Minimum Swaps to Sort by Digit Sum
Medium

You are given an array nums of distinct positive integers. You need to sort the array in increasing order based on the sum of the digits of each number. If two numbers have the same digit sum, the smaller number appears first in the sorted order.

Return the minimum number of swaps required to rearrange nums into this sorted order.

A swap is defined as exchanging the values at two distinct positions in the array.

 

Example 1:

Input: nums = [37,100]

Output: 1

Explanation:

    Compute the digit sum for each integer: [3 + 7 = 10, 1 + 0 + 0 = 1] → [10, 1]
    Sort the integers based on digit sum: [100, 37]. Swap 37 with 100 to obtain the sorted order.
    Thus, the minimum number of swaps required to rearrange nums is 1.

Example 2:

Input: nums = [22,14,33,7]

Output: 0

Explanation:

    Compute the digit sum for each integer: [2 + 2 = 4, 1 + 4 = 5, 3 + 3 = 6, 7 = 7] → [4, 5, 6, 7]
    Sort the integers based on digit sum: [22, 14, 33, 7]. The array is already sorted.
    Thus, the minimum number of swaps required to rearrange nums is 0.

Example 3:

Input: nums = [18,43,34,16]

Output: 2

Explanation:

    Compute the digit sum for each integer: [1 + 8 = 9, 4 + 3 = 7, 3 + 4 = 7, 1 + 6 = 7] → [9, 7, 7, 7]
    Sort the integers based on digit sum: [16, 34, 43, 18]. Swap 18 with 16, and swap 43 with 34 to obtain the sorted order.
    Thus, the minimum number of swaps required to rearrange nums is 2.

 

Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
    nums consists of distinct positive integers.


Hint 1
First, sort the array based on digit sum (and value as a tiebreaker). Then, map each original value to its index in the sorted array.
Hint 2
Now, the problem reduces to finding the minimum number of swaps to sort this mapped array. The answer is n - number_of_cycles in the permutation.
"""

from typing import List


class Solution:
    """
    Wrong Answer
    """

    def minSwaps(self, nums: List[int]) -> int:

        def num_key(num: int) -> tuple[int, int]:
            dsum = 0
            cur = num
            while cur > 0:
                cur, d = divmod(cur, 10)
                dsum += d
            return (dsum, num)

        misplaced = sum(num1 != num2 for num1, num2 in zip(
            nums, sorted(nums, key=num_key)))
        return (misplaced + 1) // 2


class Solution1:
    """
    leetcode solution 1: Permutation Cycles
    Runtime 1026ms Beats 71.68%
    Memory 43.41MB Beats 79.65%
    """

    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        digitSum = [0] * n
        for i, v in enumerate(nums):
            s = 0
            while v > 0:
                s += v % 10
                v //= 10
            digitSum[i] = s

        indices = list(range(n))
        indices.sort(key=lambda i: (digitSum[i], nums[i]))

        targetPos = [0] * n
        for pos, idx in enumerate(indices):
            targetPos[idx] = pos

        visited = [False] * n
        cycles = 0
        for i in range(n):
            if not visited[i]:
                cycles += 1
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = targetPos[j]

        return n - cycles


class Solution2:
    """
    leetcode solution 2: Union-Find
    Runtime 1451ms Beats 20.35%
    Memory 64.93MB Beats 5.31%
    """

    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        digitSum = [0] * n
        for i, v in enumerate(nums):
            s = 0
            while v > 0:
                s += v % 10
                v //= 10
            digitSum[i] = s

        indices = list(range(n))
        indices.sort(key=lambda i: (digitSum[i], nums[i]))

        targetPos = [0] * n
        for pos, idx in enumerate(indices):
            targetPos[idx] = pos

        parent = list(range(n))
        components = n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for i in range(n):
            ri = find(i)
            rj = find(targetPos[i])
            if ri != rj:
                parent[ri] = rj
                components -= 1

        return n - components
