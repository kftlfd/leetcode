"""
Leetcode
653. Two Sum IV - Input is a BST (easy)
2022-10-09

Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Example 2:
Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 140 ms, faster than 63.09% of Python3 online submissions for Two Sum IV - Input is a BST.
# Memory Usage: 16.2 MB, less than 99.74% of Python3 online submissions for Two Sum IV - Input is a BST.
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        if not root:
            return False

        seen = set()
        q = [root]

        while q:
            for _ in range(len(q)):
                node = q.pop(0)
                if k - node.val in seen:
                    return True
                seen.add(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return False


# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
