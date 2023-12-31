"""
Leetcode
112. Path Sum (medium)
2022-10-04

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 81 ms, faster than 42.11% of Python3 online submissions for Path Sum.
# Memory Usage: 15 MB, less than 91.98% of Python3 online submissions for Path Sum.
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, curr_sum):
            if not node:
                return False
            new_sum = curr_sum + node.val
            if not node.left and not node.right and new_sum == targetSum:
                return True
            else:
                return dfs(node.left, new_sum) or dfs(node.right, new_sum)

        return dfs(root, 0)


# Runtime: 92 ms, faster than 21.28% of Python3 online submissions for Path Sum.
# Memory Usage: 15.1 MB, less than 16.13% of Python3 online submissions for Path Sum.
class Solution1:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        new_sum = targetSum - root.val

        if not root.left and not root.right and new_sum == 0:
            return True

        return self.hasPathSum(root.left, new_sum) or self.hasPathSum(root.right, new_sum)


# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
