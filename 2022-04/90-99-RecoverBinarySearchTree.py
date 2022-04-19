"""
Leetcode
99. Recover Binary Search Tree (medium)
2022-04-19

You are given the root of a binary search tree (BST), where the values 
of exactly two nodes of the tree were swapped by mistake. Recover the 
tree without changing its structure.
"""

"""
Do not return anything, modify root in-place instead.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



# https://leetcode.com/problems/recover-binary-search-tree/discuss/917430/Python-O(n)O(1)-Morris-traversal-explained
# Runtime: 136 ms, faster than 16.77% of Python3 online submissions for Recover Binary Search Tree.
# Memory Usage: 14.2 MB, less than 94.87% of Python3 online submissions for Recover Binary Search Tree.
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        cur, node, cands = root, TreeNode(-float("inf")), []
        while cur:
            if cur.left:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                if not pre.right:
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    if cur.val < node.val:
                        cands += [node, cur]
                    node = cur
                    cur = cur.right
            else:
                if cur.val < node.val:
                    cands += [node, cur]
                node = cur
                cur = cur.right
            
        cands[0].val, cands[-1].val = cands[-1].val, cands[0].val        



s = Solution()
tests = [
]
print("no tests")
# for t in tests:
#     print(t)
#     print()
