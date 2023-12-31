"""
Leetcode
102. Binary Tree Level Order Traversal (medium)
2022-07-13

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

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


# Runtime: 47 ms, faster than 66.89% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 14.2 MB, less than 84.23% of Python3 online submissions for Binary Tree Level Order Traversal.
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root

        curr = root
        q = [curr]
        levels = []

        while q:
            q2 = []
            level = []
            for node in q:
                level.append(node.val)
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            levels.append(level)
            q = q2

        return levels


# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
