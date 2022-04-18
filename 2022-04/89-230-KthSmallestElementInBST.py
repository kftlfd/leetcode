"""
Leetcode
230. Kth Smallest Element in a BST (medium)
2022-04-18

Given the root of a binary search tree, and an integer k, return the kth 
smallest value (1-indexed) of all the values of the nodes in the tree.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



# try 1
# Runtime: 63 ms, faster than 65.78% of Python3 online submissions for Kth Smallest Element in a BST.
# Memory Usage: 18 MB, less than 90.88% of Python3 online submissions for Kth Smallest Element in a BST.
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        st = []
        q = [root]
        while q:
            node = q.pop(0)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
            st.append(node)
        st.sort(key=lambda x: x.val)
        return st[k-1].val

# Runtime: 58 ms, faster than 76.10% of Python3 online submissions for Kth Smallest Element in a BST.
# Memory Usage: 18 MB, less than 90.88% of Python3 online submissions for Kth Smallest Element in a BST.
#             st.append(node.val)
#         st.sort()
#         return st[k-1]



s = Solution()
tests = [
]
print("no tests")
# for t in tests:
#     print(t)
#     print()
