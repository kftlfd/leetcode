"""
Leetcode
513. Find Bottom Left Tree Value
Medium
2024-02-28

Given the root of a binary tree, return the leftmost value in the last row of the tree.

 

Example 1:

Input: root = [2,1,3]
Output: 1

Example 2:

Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7

 

Constraints:

    The number of nodes in the tree is in the range [1, 104].
    -231 <= Node.val <= 231 - 1
"""

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Runtime: 43 ms, faster than 51.90% of Python3 online submissions for Find Bottom Left Tree Value.
    Memory Usage: 18.4 MB, less than 52.22% of Python3 online submissions for Find Bottom Left Tree Value.
    """

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = [root]
        ans = q[0].val

        while q:
            nxt_q = []
            for node in q:
                if node.left:
                    nxt_q.append(node.left)
                if node.right:
                    nxt_q.append(node.right)
            if nxt_q:
                ans = nxt_q[0].val
            q = nxt_q

        return ans


class Solution1:
    """
    sample 30 ms submission
    Runtime: 34 ms, faster than 92.39% of Python3 online submissions for Find Bottom Left Tree Value.
    Memory Usage: 18.2 MB, less than 97.42% of Python3 online submissions for Find Bottom Left Tree Value.
    """

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])

        while q:
            node = q.popleft()

            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)

        return node.val
