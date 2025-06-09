"""
Leetcode
2025-06-09
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


class Solution00:
    """
    Time Limit Exceeded
    """

    def findKthNumber(self, n: int, k: int) -> int:
        ans = [0, 0]

        def dfs(cur: int):
            if cur > n:
                return False
            ans[0] = cur
            ans[1] += 1
            if ans[1] == k:
                return True
            nxt = cur * 10
            for i in range(10):
                if dfs(nxt + i):
                    return True
            return False

        j = 1
        while j < 10 and not dfs(j):
            j += 1

        return ans[0]


class Solution01:
    """
    Time Limit Exceeded
    """

    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1

        for _ in range(k - 1):
            # If multiplying the current number by 10 is within the limit, do it
            if cur * 10 <= n:
                cur *= 10
            else:
                # Adjust the current number by moving up one digit
                while cur % 10 == 9 or cur >= n:
                    cur //= 10  # Remove the last digit
                cur += 1  # Increment the number

        return cur


class Solution1:
    """
    leetcode solution: Prefix Tree
    Runtime 0ms Beats 100.00%
    Memory 17.98MB Beats 18.91%
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
