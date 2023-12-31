"""
Leetcode
114. Flatten Binary Tree to Linked List (medium)
2022-07-27

Given the root of a binary tree, flatten the tree into a "linked list":

 - The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
 - The "linked list" should be in the same order as a pre-order traversal of the binary tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/2338948/Explanation-so-far
# Runtime: 61 ms, faster than 44.67% of Python3 online submissions for Flatten Binary Tree to Linked List.
# Memory Usage: 15.2 MB, less than 47.67% of Python3 online submissions for Flatten Binary Tree to Linked List.
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root

        while root:
            if root.left:
                left = root.left
                curr = left
                while curr.right:
                    curr = curr.right
                curr.right = root.right
                root.left = None
                root.right = left
            root = root.right


# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/2338915/PYTHON-oror-EXPLAINED-oror
# Runtime: 38 ms, faster than 94.00% of Python3 online submissions for Flatten Binary Tree to Linked List.
# Memory Usage: 15.2 MB, less than 47.67% of Python3 online submissions for Flatten Binary Tree to Linked List.
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def rightmost(root):
            if (root.right):
                return rightmost(root.right)
            return root

        if root:
            nextright = None
            rightMOST = None

        while root:
            if root.left:
                rightMOST = rightmost(root.left)
                nextright = root.right
                root.right = root.left
                root.left = None
                rightMOST.right = nextright
            root = root.right


# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
