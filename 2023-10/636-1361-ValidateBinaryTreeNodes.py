"""
Leetcode
1361. Validate Binary Tree Nodes (medium)
2023-10-17

You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.

 

Example 1:

Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true

Example 2:

Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false

Example 3:

Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false

 

Constraints:

    n == leftChild.length == rightChild.length
    1 <= n <= 10^4
    -1 <= leftChild[i], rightChild[i] <= n - 1
"""

from typing import List
from collections import deque


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        parents = [None] * n

        for node, (left, right) in enumerate(zip(leftChild, rightChild)):
            if left != -1:
                left_parent = parents[left]
                if left_parent is not None and left_parent != node:
                    return False
                parents[left] = node

            if right != -1:
                right_parent = parents[right]
                if right_parent is not None and right_parent != node:
                    return False
                parents[right] = node

        seen_node_without_parent = False
        for node in parents:
            if node is None:
                if not seen_node_without_parent:
                    seen_node_without_parent = True
                else:
                    return False

        return seen_node_without_parent


class Solution1:
    """
    leetcode solution 1: dfs
    Time: O(n)
    Space: O(n)
    Runtime: 260 ms, faster than 85.33% of Python3 online submissions for Validate Binary Tree Nodes.
    Memory Usage: 19.9 MB, less than 38.02% of Python3 online submissions for Validate Binary Tree Nodes.
    """

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        def find_root():
            children = set(leftChild) | set(rightChild)

            for i in range(n):
                if i not in children:
                    return i

            return -1

        root = find_root()
        if root == -1:
            return False

        seen = {root}
        stack = [root]
        while stack:
            node = stack.pop()
            for child in [leftChild[node], rightChild[node]]:
                if child != -1:
                    if child in seen:
                        return False

                    stack.append(child)
                    seen.add(child)

        return len(seen) == n


class Solution2:
    """
    leetcode solution 2: bfs
    Time: O(n)
    Space: O(n)
    Runtime: 285 ms, faster than 38.92% of Python3 online submissions for Validate Binary Tree Nodes.
    Memory Usage: 20 MB, less than 37.13% of Python3 online submissions for Validate Binary Tree Nodes.
    """

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        def find_root():
            children = set(leftChild) | set(rightChild)

            for i in range(n):
                if i not in children:
                    return i

            return -1

        root = find_root()
        if root == -1:
            return False

        seen = {root}
        queue = deque([root])
        while queue:
            node = queue.popleft()
            for child in [leftChild[node], rightChild[node]]:
                if child != -1:
                    if child in seen:
                        return False

                    queue.append(child)
                    seen.add(child)

        return len(seen) == n


class Solution3:
    """
    leetcode solution 3: union-find
    Time: O(n)
    Space: O(n)
    Runtime: 271 ms, faster than 61.09% of Python3 online submissions for Validate Binary Tree Nodes.
    Memory Usage: 17.9 MB, less than 99.09% of Python3 online submissions for Validate Binary Tree Nodes.
    """

    class UnionFind:
        def __init__(self, n):
            self.components = n
            self.parents = list(range(n))

        def union(self, parent, child):
            parent_parent = self.find(parent)
            child_parent = self.find(child)

            if child_parent != child or parent_parent == child_parent:
                return False

            self.components -= 1
            self.parents[child_parent] = parent_parent
            return True

        def find(self, node):
            if self.parents[node] != node:
                self.parents[node] = self.find(self.parents[node])

            return self.parents[node]

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        uf = self.UnionFind(n)

        for node in range(n):
            for child in [leftChild[node], rightChild[node]]:
                if child == -1:
                    continue

                if not uf.union(node, child):
                    return False

        return uf.components == 1


s = Solution1()
tests = [
    ((4, [1, -1, 3, -1], [2, -1, -1, -1]),
     True),

    ((4, [1, -1, 3, -1], [2, 3, -1, -1]),
     False),

    ((2, [1, 0], [-1, -1]),
     False),

    ((4, [1, 0, 3, -1], [-1, -1, -1, -1]),
     False),
]
for inp, exp in tests:
    res = s.validateBinaryTreeNodes(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
