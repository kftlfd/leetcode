"""
Leetcode
2024-09-22
440. K-th Smallest in Lexicographical Order
Hard

Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

 

Example 1:

Input: n = 13, k = 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.

Example 2:

Input: n = 1, k = 1
Output: 1

 

Constraints:

    1 <= k <= n <= 10^9
"""


class Solution:
    """
    Time Limit Exceeded
    """

    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1

        for _ in range(k-1):
            if cur * 10 <= n:
                cur *= 10
            else:
                while cur % 10 == 9 or cur >= n:
                    cur //= 10
                cur += 1

        return cur


class Solution1:
    """
    leetcode solution: Prefix Tree
    Runtime: 25 ms, faster than 99.00% of Python3 online submissions for K-th Smallest in Lexicographical Order.
    Memory Usage: 16.5 MB, less than 75.62% of Python3 online submissions for K-th Smallest in Lexicographical Order.
    """

    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k -= 1

        while k > 0:
            step = self._count_steps(n, curr, curr + 1)
            # If the steps are less than or equal to k, we skip this prefix's subtree
            if step <= k:
                # Move to the next prefix and decrease k by the number of steps we skip
                curr += 1
                k -= step
            else:
                # Move to the next level of the tree and decrement k by 1
                curr *= 10
                k -= 1

        return curr

    # To count how many numbers exist between prefix1 and prefix2
    def _count_steps(self, n, prefix1, prefix2):
        steps = 0
        while prefix1 <= n:
            steps += min(n + 1, prefix2) - prefix1
            prefix1 *= 10
            prefix2 *= 10
        return steps
