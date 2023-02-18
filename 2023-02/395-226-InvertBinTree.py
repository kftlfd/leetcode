"""
Leetcode
226. Invert Binary Tree (easy)
2023-02-18

Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []
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
    Runtime: 30 ms, faster than 82.96% of Python3 online submissions for Invert Binary Tree.
    Memory Usage: 14 MB, less than 7.55% of Python3 online submissions for Invert Binary Tree.
    """

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


class Solution1:
    """
    https://leetcode.com/problems/invert-binary-tree/discuss/62714/3-4-lines-Python
    Runtime: 34 ms, faster than 59.87% of Python3 online submissions for Invert Binary Tree.
    Memory Usage: 13.9 MB, less than 48.39% of Python3 online submissions for Invert Binary Tree.
    """

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(
                root.right), self.invertTree(root.left)
            return root
