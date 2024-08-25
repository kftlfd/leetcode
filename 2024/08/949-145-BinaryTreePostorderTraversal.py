"""
Leetcode
145. Binary Tree Postorder Traversal
Easy
2024-08-25

Given the root of a binary tree, return the postorder traversal of its nodes' values.

 

Example 1:

Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [1]
Output: [1]

 

Constraints:

    The number of the nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

 
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Runtime: 43 ms, faster than 6.95% of Python3 online submissions for Binary Tree Postorder Traversal.
    Memory Usage: 16.5 MB, less than 20.02% of Python3 online submissions for Binary Tree Postorder Traversal.
    """

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]


class Solution1:
    """
    Iterative
    Runtime: 29 ms, faster than 89.65% of Python3 online submissions for Binary Tree Postorder Traversal.
    Memory Usage: 16.4 MB, less than 93.76% of Python3 online submissions for Binary Tree Postorder Traversal.
    """

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        vals = []
        q = [root]
        while q:
            cur = q.pop()
            vals.append(cur.val)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

        return reversed(vals)
