"""
Leetcode
98. Validate Binary Search Tree (medium)
2022-08-11

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

 - The left subtree of a node contains only nodes with keys less than the node's key.
 - The right subtree of a node contains only nodes with keys greater than the node's key.
 - Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 104 ms, faster than 6.02% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 16.9 MB, less than 26.14% of Python3 online submissions for Validate Binary Search Tree.
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def flattenTree(node: Optional[TreeNode]) -> List[int]:
            if not node:
                return []
            return flattenTree(node.left) + [node.val] + flattenTree(node.right)

        vals = flattenTree(root)

        for i in range(1, len(vals)):
            if vals[i] <= vals[i-1]:
                return False

        return True


# https://leetcode.com/problems/validate-binary-search-tree/discuss/2409071/Python-One-liner-96.6-with-detailed-explantion-or-recursion-or-simple-_
# Runtime: 73 ms, faster than 45.90% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 16.4 MB, less than 92.32% of Python3 online submissions for Validate Binary Search Tree.
class Solution1:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return helper(node.left, low, node.val) and helper(node.right, node.val, high)

        return helper(root, -inf, inf)


# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
