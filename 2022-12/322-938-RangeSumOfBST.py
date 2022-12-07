"""
Leetcode
938. Range Sum of BST (easy)
2022-12-07

Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

Example 1:
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

Example 2:
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional


# Runtime: 215 ms, faster than 96.10% of Python3 online submissions for Range Sum of BST.
# Memory Usage: 23.2 MB, less than 8.17% of Python3 online submissions for Range Sum of BST.
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        rangeSum = 0
        curr = root
        q = [curr]
        while q:
            node = q.pop(0)
            val = node.val
            if low <= val <= high:
                rangeSum += val
            if val >= low and node.left:
                q.append(node.left)
            if val <= high and node.right:
                q.append(node.right)
        return rangeSum
