"""
Leetcode
2026-01-09
865. Smallest Subtree with all the Deepest Nodes
Medium

Given the root of a binary tree, the depth of each node is the shortest distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest nodes of the tree.
Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.

Example 2:

Input: root = [1]
Output: [1]
Explanation: The root is the deepest node in the tree.

Example 3:

Input: root = [0,1,3,null,2]
Output: [2]
Explanation: The deepest node in the tree is 2, the valid subtrees are the subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.

 

Constraints:

    The number of nodes in the tree will be in the range [1, 500].
    0 <= Node.val <= 500
    The values of the nodes in the tree are unique.

 

Note: This question is the same as 1123: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

"""

from collections import Counter, namedtuple
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 20.14MB Beats 11.50%
    """

    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node_depth = {}

        def depth_dfs(node, depth):
            if not node:
                return
            node_depth[node] = depth
            depth_dfs(node.left, depth + 1)
            depth_dfs(node.right, depth + 1)

        depth_dfs(root, 1)

        max_depth_values = node_depth.values()
        max_depth = max(max_depth_values)
        max_depth_count = Counter(max_depth_values)[max_depth]

        def dfs(node: Optional[TreeNode]) -> (tuple[None, int] | tuple[TreeNode, int]):
            if not node:
                return None, 0

            left_node, left_cnt = dfs(node.left)
            if left_node:
                return left_node, 0

            right_node, right_cnt = dfs(node.right)
            if right_node:
                return right_node, 0

            cnt = int(node_depth[node] == max_depth) + left_cnt + right_cnt
            if cnt == max_depth_count:
                return node, 0

            return None, cnt

        return dfs(root)[0]


class Solution1:
    """
    leetcode solution 1: Paint Deepest Nodes
    Runtime 0ms Beats 100.00%
    Memory 19.89MB Beats 11.50%
    """

    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Tag each node with it's depth.
        depth = {None: -1}

        def dfs(node, parent=None):
            if node:
                depth[node] = depth[parent] + 1
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)

        max_depth = max(depth.values())

        def answer(node):
            # Return the answer for the subtree at node.
            if not node or depth.get(node, None) == max_depth:
                return node
            L, R = answer(node.left), answer(node.right)
            return node if L and R else L or R

        return answer(root)


class Solution2:
    """
    leetcode solution 2: Recursion
    Runtime 3ms Beats 18.00%
    Memory 19.85MB Beats 11.50%
    """

    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # The result of a subtree is:
        # Result.node: the largest depth node that is equal to or
        #              an ancestor of all the deepest nodes of this subtree.
        # Result.dist: the number of nodes in the path from the root
        #              of this subtree, to the deepest node in this subtree.
        Result = namedtuple("Result", ("node", "dist"))

        def dfs(node):
            # Return the result of the subtree at this node.
            if not node:
                return Result(None, 0)
            L, R = dfs(node.left), dfs(node.right)
            if L.dist > R.dist:
                return Result(L.node, L.dist + 1)
            if L.dist < R.dist:
                return Result(R.node, R.dist + 1)
            return Result(node, L.dist + 1)

        return dfs(root).node
