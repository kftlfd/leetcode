"""
Leetcode
2024-10-24
951. Flip Equivalent Binary Trees
Medium

For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.

 

Example 1:
Flipped Trees Diagram

Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.

Example 2:

Input: root1 = [], root2 = []
Output: true

Example 3:

Input: root1 = [], root2 = [1]
Output: false

 

Constraints:

    The number of nodes in each tree is in the range [0, 100].
    Each tree will have unique node values in the range [0, 99].
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
    Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Flip Equivalent Binary Trees.
    Memory Usage: 16.4 MB, less than 91.19% of Python3 online submissions for Flip Equivalent Binary Trees.
    """

    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True

        if not root1 or not root2 or root1.val != root2.val:
            return False

        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) \
            or (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))


class Solution3:
    """
    leetcode solution 3: Canonical Forms
    Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Flip Equivalent Binary Trees.
    Memory Usage: 16.6 MB, less than 57.29% of Python3 online submissions for Flip Equivalent Binary Trees.
    """

    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.find_canonical_form(root1)
        self.find_canonical_form(root2)
        return self.are_equivalent(root1, root2)

    def find_canonical_form(self, root: TreeNode) -> None:
        if not root:
            return

        # Post-order traversal: first bring subtrees into their canonical form
        self.find_canonical_form(root.left)
        self.find_canonical_form(root.right)

        if not root.right:
            return

        # Swap subtrees, so that left is non-empty
        if not root.left:
            root.left = root.right
            root.right = None
            return
        left = root.left
        right = root.right

        # Swap subtrees
        if left.val > right.val:
            root.left, root.right = root.right, root.left

    def are_equivalent(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        return self.are_equivalent(
            root1.left, root2.left
        ) and self.are_equivalent(root1.right, root2.right)
