"""
Leetcode
530. Minimum Absolute Difference in BST (easy)
2023-06-14

Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

Example 1:

Input: root = [4,2,6,1,3]
Output: 1

Example 2:

Input: root = [1,0,48,null,null,12,49]
Output: 1

Constraints:

    The number of nodes in the tree is in the range [2, 10^4].
    0 <= Node.val <= 10^5
"""

from typing import Optional
from math import inf


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Runtime: 88 ms, faster than 5.10% of Python3 online submissions for Minimum Absolute Difference in BST.
    Memory Usage: 18.7 MB, less than 42.66% of Python3 online submissions for Minimum Absolute Difference in BST.
    """

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def get_vals(node):
            if not node:
                return []
            return get_vals(node.left) + [node.val] + get_vals(node.right)

        vals = get_vals(root)

        ans = inf
        for i in range(1, len(vals)):
            ans = min(ans, vals[i] - vals[i - 1])

        return ans


class Solution2:
    """
    leetcode solution: In-order Traversal Without List
    Runtime: 63 ms, faster than 80.86% of Python3 online submissions for Minimum Absolute Difference in BST.
    Memory Usage: 18.7 MB, less than 42.66% of Python3 online submissions for Minimum Absolute Difference in BST.
    """

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.minDistance = 1e9
        # Initially, it will be null.
        self.prevNode = None

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            # Find the difference with the previous value if it is there.
            if self.prevNode is not None:
                self.minDistance = min(
                    self.minDistance, node.val - self.prevNode)
            self.prevNode = node.val
            inorder(node.right)

        inorder(root)
        return self.minDistance
