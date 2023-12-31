"""
Leetcode
1339. Maximum Product of Splitted Binary Tree (medium)
2022-12-10

Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.

Example 1:
Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)

Example 2:
Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def fromString(cls, s):
        vals = s[1:-1].split(",")
        vals = map(lambda x: None if x == "null" else int(x), vals)
        return cls.build(list(vals))

    @classmethod
    def build(cls, values):
        if not values:
            return

        vals = values[:]
        root = cls(vals.pop(0))
        nodes = [root]

        while vals:
            node = nodes.pop(0)

            nextval = vals.pop(0)
            if nextval:
                node.left = cls(nextval)
                nodes.append(node.left)

            if not vals:
                break

            nextval = vals.pop(0)
            if nextval:
                node.right = cls(nextval)
                nodes.append(node.right)

        return root


# wrong
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        subTreeSums = set()

        def treeSum(node):
            if not node:
                return 0
            subTreeSum = node.val + treeSum(node.left) + treeSum(node.right)
            subTreeSums.add(subTreeSum)
            return subTreeSum

        totalSum = treeSum(root)

        ans = 0

        for s in subTreeSums:
            ans = max(ans, s * (totalSum - s))

        return ans % (10**9 - 7)


# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/discuss/496549/JavaC++Python-Easy-and-Concise
# Runtime: 1121 ms, faster than 8.90% of Python3 online submissions for Maximum Product of Splitted Binary Tree.
# Memory Usage: 75.6 MB, less than 38.79% of Python3 online submissions for Maximum Product of Splitted Binary Tree.
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        self.res = total = 0

        def s(root):
            if not root:
                return 0
            left, right = s(root.left), s(root.right)
            self.res = max(self.res, left * (total - left),
                           right * (total - right))
            return left + right + root.val

        total = s(root)
        s(root)
        return self.res % (10**9 + 7)


s = Solution()
tests = [
    ("[1,null,2,3,4,null,null,5,6]",
     90),

    ("[1,2,3,4,5,6]",
     110),
]
for inp, exp in tests:
    root = TreeNode.fromString(inp)
    res = s.maxProduct(root)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
