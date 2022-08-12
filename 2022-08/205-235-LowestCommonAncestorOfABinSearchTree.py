"""
Leetcode
235. Lowest Common Ancestor of a Binary Search Tree (easy)
2022-08-12

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
"""


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/discuss/2413331/Python-Easiest-solution-or-Detailed-graph-explantion-or-DFS-or-Beginner-friendly-_
# Runtime: 103 ms, faster than 71.57% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
# Memory Usage: 18.7 MB, less than 68.62% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # found what we want or there is nothing
        if (root == p or root == q or not root):
            return root

        # recursion
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root    # found common ancestor
        elif left:
            return left
        elif right:
            return right


# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
