"""
Leetcode
700. Search in a Binary Search Tree (easy)
2022-04-14

You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



# try 1
# Runtime: 88 ms, faster than 73.54% of Python3 online submissions for Search in a Binary Search Tree.
# Memory Usage: 16.4 MB, less than 96.41% of Python3 online submissions for Search in a Binary Search Tree.
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        while curr and curr.val != val:
            if val > curr.val:
                curr = curr.right
            else:
                curr = curr.left
        return curr



# recursion
# Runtime: 84 ms, faster than 78.42% of Python3 online submissions for Search in a Binary Search Tree.
# Memory Usage: 16.6 MB, less than 28.83% of Python3 online submissions for Search in a Binary Search Tree.
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root or root.val == val: return root
        
        return self.searchBST(root.left, val) if root.val > val else self.searchBST(root.right, val)



s = Solution()
tests = [
    [[4,2,7,1,3], 2],
    [[4,2,7,1,3], 5]
]
print('no tests')
# for t in tests:
#     print(t)
#     print()
