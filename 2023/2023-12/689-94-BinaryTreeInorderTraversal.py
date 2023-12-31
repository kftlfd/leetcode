"""
Leetcode
94. Binary Tree Inorder Traversal
Easy
2023-12-09

Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [1]
Output: [1]

 

Constraints:

    The number of nodes in the tree is in the range [0, 100].
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
    Runtime: 43 ms, faster than 21.30% of Python3 online submissions for Binary Tree Inorder Traversal.
    Memory Usage: 16.4 MB, less than 19.15% of Python3 online submissions for Binary Tree Inorder Traversal.
    """

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


class Solution1:
    """
    leetcode solution 2: Iterating method using Stack
    Runtime: 40 ms, faster than 44.80% of Python3 online submissions for Binary Tree Inorder Traversal.
    Memory Usage: 16.4 MB, less than 19.15% of Python3 online submissions for Binary Tree Inorder Traversal.
    """

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

        return res


class Solution2:
    """
    leetcode solution 3: Morris Traversal
    Runtime: 41 ms, faster than 39.17% of Python3 online submissions for Binary Tree Inorder Traversal.
    Memory Usage: 16.4 MB, less than 19.15% of Python3 online submissions for Binary Tree Inorder Traversal.
    """

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        curr = root

        while curr:
            if not curr.left:
                res.append(curr.val)
                curr = curr.right
            else:
                pre = curr.left
                while pre.right:
                    pre = pre.right
                pre.right = curr
                temp = curr
                curr = curr.left
                temp.left = None

        return res
