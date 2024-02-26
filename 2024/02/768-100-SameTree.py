"""
Leetcode
100. Same Tree
Easy
2024-02-26

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:

Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:

Input: p = [1,2,1], q = [1,1,2]
Output: false

 

Constraints:

    The number of nodes in both trees is in the range [0, 100].
    -104 <= Node.val <= 104
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Runtime: 42 ms, faster than 20.49% of Python3 online submissions for Same Tree.
    Memory Usage: 16.6 MB, less than 45.81% of Python3 online submissions for Same Tree.
    """

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def is_same(a: Optional[TreeNode], b: Optional[TreeNode]):
            if not a and not b:
                return True

            if (a and not b) or (b and not a):
                return False

            if a.val != b.val:
                return False

            return is_same(a.left, b.left) and is_same(a.right, b.right)

        return is_same(p, q)
