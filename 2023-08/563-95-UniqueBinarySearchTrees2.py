"""
Leetcode
95. Unique Binary Search Trees II (medium)
2023-08-05

Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

Example 1:

Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:

Input: n = 1
Output: [[1]]

Constraints:

    1 <= n <= 8
"""

from typing import List, Optional
from functools import cache


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    leetcode solution 1: recursive dynamic programming
    Runtime: 51 ms, faster than 98.32% of Python3 online submissions for Unique Binary Search Trees II.
    Memory Usage: 17 MB, less than 98.84% of Python3 online submissions for Unique Binary Search Trees II.
    """

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}
        return self.allPossibleBST(1, n, memo)

    def allPossibleBST(self, start, end, memo):
        res = []

        if start > end:
            res.append(None)
            return res

        if (start, end) in memo:
            return memo[(start, end)]

        # iterate through all values from start to end to construct left and right subtree recursively
        for i in range(start, end + 1):
            left_subtrees = self.allPossibleBST(start, i - 1, memo)
            right_subtrees = self.allPossibleBST(i + 1, end, memo)

            # Loop through all left and right subtrees and connect them to ith root
            for left in left_subtrees:
                for right in right_subtrees:
                    root = TreeNode(i, left, right)
                    res.append(root)

        memo[(start, end)] = res
        return res


class Solution1:
    """
    leetcode solution 2: iterative dynamic programming (space optimized)
    Runtime: 46 ms, faster than 99.68% of Python3 online submissions for Unique Binary Search Trees II.
    Memory Usage: 18.3 MB, less than 17.72% of Python3 online submissions for Unique Binary Search Trees II.
    """

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp = [[] for _ in range(n + 1)]
        dp[0].append(None)

        for number_of_nodes in range(1, n + 1):
            for i in range(1, number_of_nodes + 1):
                j = number_of_nodes - i
                for left in dp[i - 1]:
                    for right in dp[j]:
                        root = TreeNode(i, left, self.clone(right, i))
                        dp[number_of_nodes].append(root)

        return dp[n]

    def clone(self, node, offset):
        if not node:
            return None

        cloned_node = TreeNode(node.val + offset)
        cloned_node.left = self.clone(node.left, offset)
        cloned_node.right = self.clone(node.right, offset)

        return cloned_node


class Solution2:
    """
    https://leetcode.com/problems/unique-binary-search-trees-ii/solution/2000389
    Runtime: 53 ms, faster than 97.04% of Python3 online submissions for Unique Binary Search Trees II.
    Memory Usage: 17.3 MB, less than 84.15% of Python3 online submissions for Unique Binary Search Trees II.
    """

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def generate_trees(l, r):
            return [None] if l > r else [
                TreeNode(val, left, right)
                for val in range(l, r + 1)
                for left in generate_trees(l, val - 1)
                for right in generate_trees(val + 1, r)
            ]

        return generate_trees(1, n)
