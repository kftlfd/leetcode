"""
Leetcode
199. Binary Tree Right Side View (medium)
2022-07-11

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Runtime: 50 ms, faster than 51.41% of Python3 online submissions for Binary Tree Right Side View.
# Memory Usage: 14 MB, less than 22.93% of Python3 online submissions for Binary Tree Right Side View.
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return root

        curr = root
        q = [curr]
        ans = []

        while q:
            right_val = None
            q2 = []
            for node in q:
                right_val = node.val
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            ans.append(right_val)
            q = q2

        return ans


# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
