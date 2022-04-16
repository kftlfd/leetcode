"""
Leetcode
538. Convert BST to Greater Tree (medium)
2022-04-16

Given the root of a Binary Search Tree (BST), convert it to a Greater Tree 
such that every key of the original BST is changed to the original key plus 
the sum of all keys greater than the original key in BST.
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



# leetcode solution 1 - recursion
# Runtime: 121 ms, faster than 43.08% of Python3 online submissions for Convert BST to Greater Tree.
# Memory Usage: 16.7 MB, less than 53.49% of Python3 online submissions for Convert BST to Greater Tree.
class Solution:

    def __init__(self):
        self.total = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root



s = Solution()
tests = [
]
print("no tests")
# for t in tests:
#     print(t)
#     print()
