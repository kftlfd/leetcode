"""
Leetcode
897. Increasing Order Search Tree (easy)
2022-04-17

Given the root of a binary search tree, rearrange the tree in in-order 
so that the leftmost node in the tree is now the root of the tree, and 
every node has no left child and only one right child.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



# try 1
# Runtime: 30 ms, faster than 91.17% of Python3 online submissions for Increasing Order Search Tree.
# Memory Usage: 13.8 MB, less than 99.23% of Python3 online submissions for Increasing Order Search Tree.
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        st = []
        
        q = [root]
        while q:
            node = q.pop(0)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
            node.left = None
            st.append(node)
            
        st.sort(key=lambda x: x.val)
        
        root = st.pop(0)
        curr = root
        while st:
            curr.right = st.pop(0)
            curr = curr.right
        curr.right = None
        
        return root



s = Solution()
tests = [
]
print("no tests")
# for t in tests:
#     print(t)
#     print()
