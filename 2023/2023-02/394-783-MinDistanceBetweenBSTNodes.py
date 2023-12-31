"""
Leetcode
783. Minimum Distance Between BST Nodes (easy)
2023-02-17

Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

Example 1:
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1
"""

from typing import List, Optional
from math import inf

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """
    Runtime: 35 ms, faster than 56.78% of Python3 online submissions for Minimum Distance Between BST Nodes.
    Memory Usage: 13.9 MB, less than 32.56% of Python3 online submissions for Minimum Distance Between BST Nodes.
    """

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return []
            return dfs(node.left) + [node.val] + dfs(node.right)

        vals = dfs(root)

        min_diff = inf

        for i in range(1, len(vals)):
            min_diff = min(min_diff, vals[i] - vals[i-1])
            if min_diff == 1:
                break

        return min_diff


class Solution1:
    """
    leetcode solution 2: In-order Traversal Without List
    Runtime: 30 ms, faster than 85.98% of Python3 online submissions for Minimum Distance Between BST Nodes.
    Memory Usage: 13.9 MB, less than 32.56% of Python3 online submissions for Minimum Distance Between BST Nodes.
    """

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        min_diff = inf
        prev_node = None

        def dfs(node):
            nonlocal min_diff, prev_node

            if not node:
                return
            dfs(node.left)
            if prev_node:
                min_diff = min(min_diff, node.val - prev_node.val)
            prev_node = node
            dfs(node.right)

        dfs(root)

        return min_diff
