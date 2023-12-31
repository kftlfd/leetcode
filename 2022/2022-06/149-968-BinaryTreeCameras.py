"""
Leetcode
968. Binary Tree Cameras (hard)
2022-06-17

You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.

Return the minimum number of cameras needed to monitor all nodes of the tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



# leetcode solution - dynamic programming
# https://leetcode.com/problems/binary-tree-cameras/solution/
# Runtime: 93 ms, faster than 13.48% of Python3 online submissions for Binary Tree Cameras.
# Memory Usage: 14.2 MB, less than 92.17% of Python3 online submissions for Binary Tree Cameras.
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        return min(self.solve(root)[1:])
    
    def solve(self, node):
        if not node:
            return 0, 0, float('inf')
        l = self.solve(node.left)
        r = self.solve(node.right)
        dp0 = l[1] + r[1]
        dp1 = min(l[2] + min(r[1:]), r[2] + min(l[1:]))
        dp2 = 1 + min(l) + min(r)
        return dp0, dp1, dp2



# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
