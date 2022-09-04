"""
Leetcode
987. Vertical Order Traversal of a Binary Tree (hard)
2022-09-04

Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.

https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/discuss/231256/python-queue-+-hash-map
# Runtime: 71 ms, faster than 12.50% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.
# Memory Usage: 14.3 MB, less than 28.65% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        g = collections.defaultdict(list)
        queue = [(root, 0)]
        while queue:
            new = []
            d = collections.defaultdict(list)
            for node, s in queue:
                d[s].append(node.val)
                if node.left:
                    new += (node.left, s-1),
                if node.right:
                    new += (node.right, s+1),
            for i in d:
                g[i].extend(sorted(d[i]))
            queue = new
        return [g[i] for i in sorted(g)]


# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
