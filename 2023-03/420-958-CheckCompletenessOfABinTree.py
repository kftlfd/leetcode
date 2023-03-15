"""
Leetcode
958. Check Completeness of a Binary Tree (medium)
2023-03-16

Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example 1:
Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.

Example 2:
Input: root = [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
"""

from typing import Optional
from queue import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    https://leetcode.com/problems/check-completeness-of-a-binary-tree/solution/1832637
    Runtime: 36 ms, faster than 69.68% of Python3 online submissions for Check Completeness of a Binary Tree.
    Memory Usage: 13.9 MB, less than 61.50% of Python3 online submissions for Check Completeness of a Binary Tree.
    """

    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        prev_node = root
        while queue:
            node = queue.popleft()
            if node:
                if not prev_node:  # found gap
                    return False
                queue.append(node.left)
                queue.append(node.right)
            prev_node = node
        return True
