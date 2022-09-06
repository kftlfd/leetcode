"""
Leetcode
814. Binary Tree Pruning (medium)
2022-09-06

Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node.

https://leetcode.com/problems/binary-tree-pruning/
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# leetcode solution - recursion
# Runtime: 64 ms, faster than 14.67% of Python3 online submissions for Binary Tree Pruning.
# Memory Usage: 14 MB, less than 23.50% of Python3 online submissions for Binary Tree Pruning.
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def contains_one(node: TreeNode) -> bool:
            if not node:
                return False

            # Check if any node in the left subtree contains a 1.
            left_contains_one = contains_one(node.left)

            # Check if any node in the right subtree contains a 1.
            right_contains_one = contains_one(node.right)

            # If the left subtree does not contain a 1, prune the subtree.
            if not left_contains_one:
                node.left = None

            # If the right subtree does not contain a 1, prune the subtree.
            if not right_contains_one:
                node.right = None

            # Return True if the current node or its left or right subtree contains a 1.
            return node.val or left_contains_one or right_contains_one

        # Return the pruned tree if the tree contains a 1, otherwise return None.
        return root if contains_one(root) else None


# https://leetcode.com/problems/binary-tree-pruning/solution/142544
# Runtime: 68 ms, faster than 8.35% of Python3 online submissions for Binary Tree Pruning.
# Memory Usage: 14 MB, less than 23.50% of Python3 online submissions for Binary Tree Pruning.
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if (root.val == 0 and not root.left and not root.right):
            root = None

        return root


# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
