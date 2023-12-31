"""
Leetcode
129. Sum Root to Leaf Numbers (medium)
2023-03-14

You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

    For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

Example 1:
Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:
Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def fromString(cls, string):
        vals = string[1:-1].split(",")
        vals = map(lambda x: None if x == "null" else int(x), vals)
        return cls.build(list(vals))

    @classmethod
    def build(cls, values):
        if not values:
            return None

        vals = values[:]
        root = cls(vals.pop(0))
        nodes = [root]

        while vals:
            node = nodes.pop(0)

            nextval = vals.pop(0)
            if nextval is not None:
                node.left = cls(nextval)
                nodes.append(node.left)

            if not vals:
                break

            nextval = vals.pop(0)
            if nextval is not None:
                node.right = cls(nextval)
                nodes.append(node.right)

        return root


class Solution:
    """
    Runtime: 37 ms, faster than 33.35% of Python3 online submissions for Sum Root to Leaf Numbers.
    Memory Usage: 13.8 MB, less than 54.98% of Python3 online submissions for Sum Root to Leaf Numbers.
    """

    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def to_int(path: List[int]) -> int:
            path_num = 0
            for i, num in enumerate(path[::-1]):
                path_num += num * (10**i)
            return path_num

        def dfs(node: Optional[TreeNode], path: List[int]) -> int:
            if not node:
                return 0

            curr_path = path + [node.val]

            if not node.left and not node.right:
                return to_int(curr_path)

            return dfs(node.left, curr_path) + dfs(node.right, curr_path)

        return dfs(root, [])


class Solution1:
    """
    https://leetcode.com/problems/sum-root-to-leaf-numbers/discuss/1556417/C++Python-Recursive-and-Iterative-DFS-+-BFS-+-Morris-Traversal-O(1)-or-Beats-100
    Runtime: 32 ms, faster than 70.69% of Python3 online submissions for Sum Root to Leaf Numbers.
    Memory Usage: 13.8 MB, less than 54.98% of Python3 online submissions for Sum Root to Leaf Numbers.
    """

    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(node: Optional[TreeNode], prev_sum: int) -> int:
            if not node:
                return 0

            curr_sum = prev_sum * 10 + node.val

            if not node.left and not node.right:
                return curr_sum

            return dfs(node.left, curr_sum) + dfs(node.right, curr_sum)

        return dfs(root, 0)


s = Solution()
tests = [
    ('[1,2,3]',
     25),

    ('[4,9,0,5,1]',
     1026)
]
for inp, exp in tests:
    tree_root = TreeNode.fromString(inp)
    res = s.sumNumbers(tree_root)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
