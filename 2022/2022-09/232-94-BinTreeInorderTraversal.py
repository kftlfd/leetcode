"""
Leetcode
94. Binary Tree Inorder Traversal (easy)
2022-09-08

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 59 ms, faster than 19.76% of Python3 online submissions for Binary Tree Inorder Traversal.
# Memory Usage: 13.9 MB, less than 60.15% of Python3 online submissions for Binary Tree Inorder Traversal.
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        return [*self.inorderTraversal(root.left), root.val, *self.inorderTraversal(root.right)]


# https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/283746/All-DFS-traversals-(preorder-inorder-postorder)-in-Python-in-1-line
# Runtime: 55 ms, faster than 29.81% of Python3 online submissions for Binary Tree Inorder Traversal.
# Memory Usage: 13.9 MB, less than 13.48% of Python3 online submissions for Binary Tree Inorder Traversal.
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []


# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
