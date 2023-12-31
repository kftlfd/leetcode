"""
Leetcode
863. All Nodes Distance K in Binary Tree (medium)
2023-07-11

Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

Example 2:

Input: root = [1], target = 1, k = 3
Output: []

Constraints:

    The number of nodes in the tree is in the range [1, 500].
    0 <= Node.val <= 500
    All the values Node.val are unique.
    target is the value of one of the nodes in the tree.
    0 <= k <= 1000
"""

from typing import List
from collections import defaultdict, deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    leetcode solution 1: implementing parent pointers (not a good coding practice)
    Time: O(n)
    Space: O(n)
    Runtime: 62 ms, faster than 13.90% of Python3 online submissions for All Nodes Distance K in Binary Tree.
    Memory Usage: 16.9 MB, less than 19.14% of Python3 online submissions for All Nodes Distance K in Binary Tree.
    """

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # recursively add a parent pointer to each node
        def add_parent(cur, parent):
            if cur:
                cur.parent = parent
                add_parent(cur.left, cur)
                add_parent(cur.right, cur)

        add_parent(root, None)

        ans = []
        visited = set()

        def dfs(cur, distance):
            if not cur or cur in visited:
                return
            visited.add(cur)
            if distance == 0:
                ans.append(cur.val)
                return
            dfs(cur.parent, distance - 1)
            dfs(cur.left, distance - 1)
            dfs(cur.right, distance - 1)

        dfs(target, k)

        return ans


class Solution1:
    """
    leetcode solution 2: DFS on equivalent graph
    Time: O(n)
    Space: O(n)
    Runtime: 57 ms, faster than 40.84% of Python3 online submissions for All Nodes Distance K in Binary Tree.
    Memory Usage: 16.9 MB, less than 19.14% of Python3 online submissions for All Nodes Distance K in Binary Tree.
    """

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        # recursively build the undirected graph from the given binary tree
        def build_graph(cur, parent):
            if cur and parent:
                graph[cur.val].append(parent.val)
                graph[parent.val].append(cur.val)
            if cur.left:
                build_graph(cur.left, cur)
            if cur.right:
                build_graph(cur.right, cur)
        build_graph(root, None)

        ans = []
        visited = set([target.val])

        def dfs(cur, distance):
            if distance == k:
                ans.append(cur)
                return
            for neighbor in graph[cur]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor, distance + 1)
        dfs(target.val, 0)

        return ans


class Solution2:
    """
    leetcode solution 3: BFS on equivalent graph
    Time: O(n)
    Space: O(n)
    Runtime: 60 ms, faster than 23.04% of Python3 online submissions for All Nodes Distance K in Binary Tree.
    Memory Usage: 16.8 MB, less than 59.10% of Python3 online submissions for All Nodes Distance K in Binary Tree.
    """

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        # recursively build the undirected graph from the given binary tree
        def build_graph(cur, parent):
            if cur and parent:
                graph[cur.val].append(parent.val)
                graph[parent.val].append(cur.val)
            if cur.left:
                build_graph(cur.left, cur)
            if cur.right:
                build_graph(cur.right, cur)
        build_graph(root, None)

        ans = []
        visited = set([target.val])

        q = deque([(target.val, 0)])
        while q:
            cur, distance = q.popleft()

            if distance == k:
                ans.append(cur)
                continue

            for neighbor in graph[cur]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append((neighbor, distance + 1))

        return ans
