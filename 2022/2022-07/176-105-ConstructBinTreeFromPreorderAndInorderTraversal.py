"""
Leetcode
105. Construct Binary Tree from Preorder and Inorder Traversal (medium)
2022-07-14

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34579/Python-short-recursive-solution.
# Runtime: 202 ms, faster than 60.55% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
# Memory Usage: 53.5 MB, less than 59.72% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root


s = Solution()
tests = [
    ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]),
    ([-1], [-1])
]
for t in tests:
    print(t)
    print(s.buildTree(t[0], t[1]))
    print()
