"""
Leetcode
144. Binary Tree Preorder Traversal (easy)
2023-01-09

Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]
"""

from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Recursive
# Runtime: 33 ms, faster than 82.20% of Python3 online submissions for Binary Tree Preorder Traversal.
# Memory Usage: 13.8 MB, less than 57.18% of Python3 online submissions for Binary Tree Preorder Traversal.
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


# Iterative (stack)
# Runtime: 37 ms, faster than 69.37% of Python3 online submissions for Binary Tree Preorder Traversal.
# Memory Usage: 13.7 MB, less than 96.79% of Python3 online submissions for Binary Tree Preorder Traversal.
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        ans = []

        q = [root]
        while q:
            node = q.pop()
            if not node:
                continue
            ans.append(node.val)
            q.append(node.right)
            q.append(node.left)

        return ans


# leetcode solution 3 - Morris traversal
# Runtime: 31 ms, faster than 87.43% of Python3 online submissions for Binary Tree Preorder Traversal.
# Memory Usage: 13.8 MB, less than 57.18% of Python3 online submissions for Binary Tree Preorder Traversal.
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        ans = []
        curr = root

        while curr:

            # If there is no left child, go for the right child.
            # Otherwise, find the last node in the left subtree.
            if not curr.left:
                ans.append(curr.val)
                curr = curr.right
                continue

            last = curr.left
            while last.right and last.right != curr:
                last = last.right

            # If the last node is not modified, we let
            # 'curr' be its right child. Otherwise, it means we
            # have finished visiting the entire left subtree.
            if not last.right:
                ans.append(curr.val)
                last.right = curr
                curr = curr.left
            else:
                last.right = None
                curr = curr.right

        return ans
