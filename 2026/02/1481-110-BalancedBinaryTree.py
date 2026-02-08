"""
Leetcode
2026-02-08
110. Balanced Binary Tree
Easy

Given a binary tree, determine if it is .

 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:

Input: root = []
Output: true

 

Constraints:

    The number of nodes in the tree is in the range [0, 5000].
    -10^4 <= Node.val <= 10^4


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
    Runtime 1ms Beats 67.62%
    Memory 20.40MB Beats 52.53%
    """

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.getHeight(root)[0]

    def getHeight(self, root: Optional[TreeNode]) -> tuple[bool, int]:
        if not root:
            return (True, 0)
        if not root.left and not root.right:
            return (True, 1)
        b_left, h_left = self.getHeight(root.left)
        b_right, h_right = self.getHeight(root.right)
        return (
            b_left and b_right and abs(h_left - h_right) <= 1,
            1 + max(h_left, h_right)
        )


class Solution1:
    """
    sample 0ms solution
    Runtime 0ms Beats 100.00%
    Memory 20.51MB Beats 23.25%
    """
    balanced: bool

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def dfs(node):
            if node is None:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)

            if abs(l-r) > 1:
                self.balanced = False

            return max(l, r) + 1

        dfs(root)
        return self.balanced
