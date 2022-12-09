"""
Leetcode
1026. Maximum Difference Between Node and Ancestor (medium)
2022-12-09

Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

Example 1:
Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

Example 2:
Input: root = [1,null,2,null,0,3]
Output: 3
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional


# leetcode solution
# Runtime: 38 ms, faster than 96.71% of Python3 online submissions for Maximum Difference Between Node and Ancestor.
# Memory Usage: 20 MB, less than 60.12% of Python3 online submissions for Maximum Difference Between Node and Ancestor.
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        def helper(node, curr_max, curr_min):
            if not node:
                return curr_max - curr_min

            curr_max = max(curr_max, node.val)
            curr_min = min(curr_min, node.val)
            left = helper(node.left, curr_max, curr_min)
            right = helper(node.right, curr_max, curr_min)
            return max(left, right)

        return helper(root, root.val, root.val)
