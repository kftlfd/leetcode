"""
Leetcode
2385. Amount of Time for Binary Tree to Be Infected
Medium
2024-01-10

You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.

Each minute, a node becomes infected if:

    The node is currently uninfected.
    The node is adjacent to an infected node.

Return the number of minutes needed for the entire tree to be infected.

 

Example 1:

Input: root = [1,5,3,null,4,10,6,9,2], start = 3
Output: 4
Explanation: The following nodes are infected during:
- Minute 0: Node 3
- Minute 1: Nodes 1, 10 and 6
- Minute 2: Node 5
- Minute 3: Node 4
- Minute 4: Nodes 9 and 2
It takes 4 minutes for the whole tree to be infected so we return 4.

Example 2:

Input: root = [1], start = 1
Output: 0
Explanation: At minute 0, the only node in the tree is infected so we return 0.

 

Constraints:

    The number of nodes in the tree is in the range [1, 105].
    1 <= Node.val <= 105
    Each node has a unique value.
    A node with a value of start exists in the tree.

Hints:
- Convert the tree to an undirected graph to make it easier to handle.
- Use BFS starting at the start node to find the distance between each node and the start node. The answer is the maximum distance.
"""

from collections import defaultdict, deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Runtime: 334 ms, faster than 96.83% of Python3 online submissions for Amount of Time for Binary Tree to Be Infected.
    Memory Usage: 55.5 MB, less than 93.86% of Python3 online submissions for Amount of Time for Binary Tree to Be Infected.
    """

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if not root:
            return 0

        graph = defaultdict(list)
        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                q.append(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                q.append(node.right)

        ans = -1
        q = [start]
        seen = {start}
        while q:
            ans += 1
            nxt_q = []
            for node in q:
                for nxt_node in graph[node]:
                    if nxt_node not in seen:
                        nxt_q.append(nxt_node)
                        seen.add(nxt_node)
            q = nxt_q

        return ans


class Solution2:
    """
    leetcode solution 2: One-Pass Depth-First Search
    Runtime: 246 ms, faster than 99.63% of Python3 online submissions for Amount of Time for Binary Tree to Be Infected.
    Memory Usage: 51.2 MB, less than 99.26% of Python3 online submissions for Amount of Time for Binary Tree to Be Infected.
    """

    def __init__(self):
        self.max_distance = 0

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.max_distance = 0
        self.traverse(root, start)
        return self.max_distance

    def traverse(self, root, start):
        depth = 0
        if root is None:
            return depth

        left_depth = self.traverse(root.left, start)
        right_depth = self.traverse(root.right, start)

        if root.val == start:
            self.max_distance = max(left_depth, right_depth)
            depth = -1
        elif left_depth >= 0 and right_depth >= 0:
            depth = max(left_depth, right_depth) + 1
        else:
            distance = abs(left_depth) + abs(right_depth)
            self.max_distance = max(self.max_distance, distance)
            depth = min(left_depth, right_depth) - 1

        return depth
