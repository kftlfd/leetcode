"""
Leetcode
404. Sum of Left Leaves
Easy
2024-04-14

Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

Example 2:

Input: root = [1]
Output: 0

 

Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    -1000 <= Node.val <= 1000
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
    Runtime: 29 ms, faster than 92.20% of Python3 online submissions for Sum of Left Leaves.
    Memory Usage: 16.8 MB, less than 47.89% of Python3 online submissions for Sum of Left Leaves.
    """

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node: Optional[TreeNode], is_left: bool):
            nonlocal ans

            if not node:
                return

            if not node.left and not node.right and is_left:
                ans += node.val

            dfs(node.left, True)
            dfs(node.right, False)

        dfs(root, False)

        return ans
