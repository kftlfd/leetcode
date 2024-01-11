"""
Leetcode
1026. Maximum Difference Between Node and Ancestor
Medium
2024-01-11

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

 

Constraints:

    The number of nodes in the tree is in the range [2, 5000].
    0 <= Node.val <= 10^5
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
    Runtime: 37 ms, faster than 88.16% of Python3 online submissions for Maximum Difference Between Node and Ancestor.
    Memory Usage: 19.1 MB, less than 71.14% of Python3 online submissions for Maximum Difference Between Node and Ancestor.
    """

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = 0

        def dfs(node):
            nonlocal ans

            if not node:
                return (float('inf'), float('-inf'))

            if not node.left and not node.right:
                return (node.val, node.val)

            min_left, max_left = dfs(node.left)
            min_right, max_right = dfs(node.right)
            min_child = min(min_left, min_right)
            max_child = max(max_left, max_right)

            ans = max(
                ans,
                abs(node.val - min_child),
                abs(node.val - max_child)
            )

            return (
                min(min_left, node.val, min_right),
                max(max_left, node.val, max_right)
            )

        dfs(root)

        return ans
