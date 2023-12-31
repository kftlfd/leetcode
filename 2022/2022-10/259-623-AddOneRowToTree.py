"""
Leetcode
623. Add One Row to Tree (medium)
2022-10-05

Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.

Note that the root node is at depth 1.

The adding rule is:

 - Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
 - cur's original left subtree should be the left subtree of the new left subtree root.
 - cur's original right subtree should be the right subtree of the new right subtree root.
 - If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.

Example 1:
Input: root = [4,2,6,3,1,5], val = 1, depth = 2
Output: [4,1,1,2,null,null,6,3,1,5]

Example 2:
Input: root = [4,2,null,3,1], val = 1, depth = 3
Output: [4,2,null,1,1,3,null,null,1]
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Wrong Answer
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        if depth == 1:
            return TreeNode(val, root)

        q = [root]

        for _ in range(1, depth - 1):
            for __ in range(len(q)):
                node = q.pop()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        for node in q:
            node.left = TreeNode(val, node.left)
            node.right = TreeNode(val, None, node.right)

        return root


# https://leetcode.com/problems/add-one-row-to-tree/discuss/104582/Short-Python-BFS
# Runtime: 149 ms, faster than 5.00% of Python3 online submissions for Add One Row to Tree.
# Memory Usage: 16.6 MB, less than 93.03% of Python3 online submissions for Add One Row to Tree.
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        dummy, dummy.left = TreeNode(None), root
        row = [dummy]
        for _ in range(depth - 1):
            row = [kid for node in row for kid in (
                node.left, node.right) if kid]
        for node in row:
            node.left, node.left.left = TreeNode(val), node.left
            node.right, node.right.right = TreeNode(val), node.right
        return dummy.left


# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
