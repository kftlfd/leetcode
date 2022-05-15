"""
Leetcode
1302. Deepest Leaves Sum (medium)
2022-05-15

Given the root of a binary tree, return the sum of values of its deepest leaves. 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



# try 1
# Runtime: 182 ms, faster than 99.72% of Python3 online submissions for Deepest Leaves Sum.
# Memory Usage: 17.8 MB, less than 66.46% of Python3 online submissions for Deepest Leaves Sum.
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        q = [root]
        nxt = []
        
        while q:
            for node in q:
                if node.left: nxt.append(node.left)
                if node.right: nxt.append(node.right)
            if nxt:
                q = nxt
                nxt = []
            else:
                break
                
        ans = 0
        for node in q:
            ans += node.val
            
        return ans



# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
