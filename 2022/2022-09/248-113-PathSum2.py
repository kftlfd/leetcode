"""
Leetcode
113. Path Sum II (medium)
2022-09-24

Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:
Input: root = [1,2], targetSum = 0
Output: []
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/path-sum-ii/discuss/1382469/Python-dfs-solution-with-complexity-explained
# Runtime: 79 ms, faster than 44.80% of Python3 online submissions for Path Sum II.
# Memory Usage: 15.6 MB, less than 72.84% of Python3 online submissions for Path Sum II.
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, sm):
            if not node:
                return []
            if not node.left and not node.right and sm == node.val:
                return [[node.val]]

            lft = dfs(node.left, sm - node.val)
            rgh = dfs(node.right, sm - node.val)
            return [cand + [node.val] for cand in lft + rgh]

        return [s[::-1] for s in dfs(root, targetSum)]


# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
