"""
Leetcode
669. Trim a Binary Search Tree (medium)
2022-04-15

Given the root of a binary search tree and the lowest and highest 
boundaries as low and high, trim the tree so that all its elements 
lies in [low, high]. Trimming the tree should not change the 
relative structure of the elements that will remain in the tree 
(i.e., any node's descendant should remain a descendant). It can 
be proven that there is a unique answer.

Return the root of the trimmed binary search tree. Note that the 
root may change depending on the given bounds.
"""

from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



# leetcode solution - recursion
# Runtime: 60 ms, faster than 70.24% of Python3 online submissions for Trim a Binary Search Tree.
# Memory Usage: 18.1 MB, less than 48.91% of Python3 online submissions for Trim a Binary Search Tree.
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        def trim(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node: return node
            elif node.val > high:
                return trim(node.left)
            elif node.val < low:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node
            
        return trim(root)



s = Solution()
tests = [
]
print("no tests")
# for t in tests:
#     print(t)
#     print()
