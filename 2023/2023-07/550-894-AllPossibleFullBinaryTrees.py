"""
Leetcode
894. All Possible Full Binary Trees (medium)
2023-07-23

Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Example 1:

Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]

Example 2:

Input: n = 3
Output: [[0,0,0]]
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Runtime: 173 ms, faster than 90.42% of Python3 online submissions for All Possible Full Binary Trees.
    Memory Usage: 19.7 MB, less than 96.47% of Python3 online submissions for All Possible Full Binary Trees.
    """

    memo = {
        0: [],
        1: [TreeNode(0)],
    }

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []

        if n in self.memo:
            return self.memo[n]

        ans = []
        for i in range(n):
            for left in self.allPossibleFBT(i):
                for right in self.allPossibleFBT(n - 1 - i):
                    ans.append(TreeNode(0, left, right))
        self.memo[n] = ans

        return self.memo[n]


class Solution1:
    """
    leetcode solution 2: iterative dynamic programming
    Time: O(2^(n/2))
    Space: O(n * 2^(n/2))
    Runtime: 176 ms, faster than 83.81% of Python3 online submissions for All Possible Full Binary Trees.
    Memory Usage: 19.8 MB, less than 88.71% of Python3 online submissions for All Possible Full Binary Trees.
    """

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []

        dp = [[] for _ in range(n + 1)]
        dp[1].append(TreeNode(0))

        for count in range(3, n + 1, 2):
            for i in range(1, count - 1, 2):
                j = count - 1 - i
                for left in dp[i]:
                    for right in dp[j]:
                        root = TreeNode(0, left, right)
                        dp[count].append(root)

        return dp[n]


s = Solution()
t = s.allPossibleFBT(3)
print(t)
