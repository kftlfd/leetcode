"""
Leetcode
1448. Count Good Nodes in Binary Tree (medium)
2022-09-01

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:
Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:
Input: root = [1]
Output: 1
Explanation: Root is considered as good.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/count-good-nodes-in-binary-tree/discuss/635258/JavaPython-3-Simple-recursive-and-iterative-DFS-codes-w-brief-explanation-and-analysis.
# Runtime: 558 ms, faster than 6.47% of Python3 online submissions for Count Good Nodes in Binary Tree.
# Memory Usage: 32.4 MB, less than 87.02% of Python3 online submissions for Count Good Nodes in Binary Tree.
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def count(node: TreeNode, v: int) -> int:
            if node is None:
                return 0
            mx = max(node.val, v)
            return (node.val >= v) + count(node.left, mx) + count(node.right, mx)

        return count(root, root.val)


# https://leetcode.com/problems/count-good-nodes-in-binary-tree/discuss/635258/JavaPython-3-Simple-recursive-and-iterative-DFS-codes-w-brief-explanation-and-analysis.
# Runtime: 798 ms, faster than 5.03% of Python3 online submissions for Count Good Nodes in Binary Tree.
# Memory Usage: 32.8 MB, less than 7.60% of Python3 online submissions for Count Good Nodes in Binary Tree.
class Solution1:
    def goodNodes(self, root: TreeNode) -> int:

        cnt = 0
        stk = [(root, root.val)]
        while stk:
            cur, current_max = stk.pop()
            cnt += cur.val >= current_max
            for kid in cur.left, cur.right:
                if kid:
                    stk.append((kid, max(cur.val, current_max)))
        return cnt


# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
