"""
Leetcode
104. Maximum Depth of Binary Tree (easy)
2023-02-16

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
"""

from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """
    Runtime: 38 ms, faster than 91.32% of Python3 online submissions for Maximum Depth of Binary Tree.
    Memory Usage: 16.2 MB, less than 49.77% of Python3 online submissions for Maximum Depth of Binary Tree.
    """

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node, depth):
            if not node:
                return 0
            if not node.left and not node.right:
                return depth
            return max(dfs(node.left, depth+1), dfs(node.right, depth+1))

        return dfs(root, 1)
