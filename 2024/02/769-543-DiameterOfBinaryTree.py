"""
Leetcode
543. Diameter of Binary Tree
Easy
2024-02-27

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:

Input: root = [1,2]
Output: 1

 

Constraints:

    The number of nodes in the tree is in the range [1, 104].
    -100 <= Node.val <= 100
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
    Runtime: 40 ms, faster than 74.55% of Python3 online submissions for Diameter of Binary Tree.
    Memory Usage: 17.6 MB, less than 74.69% of Python3 online submissions for Diameter of Binary Tree.
    """

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node: Optional[TreeNode]):
            nonlocal ans

            if not node:
                return -1

            left = 1 + dfs(node.left)
            right = 1 + dfs(node.right)

            ans = max(ans, left + right)
            return max(left, right)

        dfs(root)
        return ans
