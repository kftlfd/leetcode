"""
Leetcode
2024-12-23
2471. Minimum Number of Operations to Sort a Binary Tree by Level
Medium

You are given the root of a binary tree with unique values.

In one operation, you can choose any two nodes at the same level and swap their values.

Return the minimum number of operations needed to make the values at each level sorted in a strictly increasing order.

The level of a node is the number of edges along the path between it and the root node.

 

Example 1:

Input: root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]
Output: 3
Explanation:
- Swap 4 and 3. The 2nd level becomes [3,4].
- Swap 7 and 5. The 3rd level becomes [5,6,8,7].
- Swap 8 and 7. The 3rd level becomes [5,6,7,8].
We used 3 operations so return 3.
It can be proven that 3 is the minimum number of operations needed.

Example 2:

Input: root = [1,3,2,7,6,5,4]
Output: 3
Explanation:
- Swap 3 and 2. The 2nd level becomes [2,3].
- Swap 7 and 4. The 3rd level becomes [4,6,5,7].
- Swap 6 and 5. The 3rd level becomes [4,5,6,7].
We used 3 operations so return 3.
It can be proven that 3 is the minimum number of operations needed.

Example 3:

Input: root = [1,2,3,4,5,6]
Output: 0
Explanation: Each level is already sorted in increasing order so return 0.

 

Constraints:

    The number of nodes in the tree is in the range [1, 10^5].
    1 <= Node.val <= 10^5
    All the values of the tree are unique.
"""

from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Runtime: 149 ms, faster than 67.32% of Python3 online submissions for Minimum Number of Operations to Sort a Binary Tree by Level.
    Memory Usage: 50.4 MB, less than 15.69% of Python3 online submissions for Minimum Number of Operations to Sort a Binary Tree by Level.
    """

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = 0
        q = [root]

        while q:
            values = [node.val for node in q]
            ans += self.opsToSort(values)

            nxt_q = []
            for node in q:
                if node.left:
                    nxt_q.append(node.left)
                if node.right:
                    nxt_q.append(node.right)
            q = nxt_q

        return ans

    def opsToSort(self, values: List[int]) -> int:
        if len(values) < 2:
            return 0

        idx = {v: i for i, v in enumerate(values)}
        sorted_values = sorted(values)
        swaps = 0

        for cur_i, cur_val in enumerate(values):
            sorted_val = sorted_values[cur_i]
            if cur_val != sorted_val:
                swaps += 1
                sorted_i = idx[sorted_val]
                values[cur_i], values[sorted_i] = values[sorted_i], values[cur_i]
                idx[cur_val] = sorted_i
                idx[sorted_val] = cur_i

        return swaps


class Solution2:
    """
    leetcode solution 2: Bit Manipulation
    Runtime: 125 ms, faster than 99.35% of Python3 online submissions for Minimum Number of Operations to Sort a Binary Tree by Level.
    Memory Usage: 50.6 MB, less than 13.73% of Python3 online submissions for Minimum Number of Operations to Sort a Binary Tree by Level.
    """

    # Constants for bit manipulation
    _SHIFT = 20
    _MASK = 0xFFFFF

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        swaps = 0

        # Process tree level by level using BFS
        while queue:
            level_size = len(queue)
            nodes = []

            # Store node values with encoded positions
            for i in range(level_size):
                node = queue.popleft()
                # Encode value and index: high 20 bits = value, low 20 bits = index
                nodes.append((node.val << self._SHIFT) + i)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Sort nodes by their values (high 20 bits)
            nodes.sort()

            # Count swaps needed to match indices with original positions
            i = 0
            while i < level_size:
                orig_pos = nodes[i] & self._MASK
                if orig_pos != i:
                    # Swap nodes and decrement i to recheck current position
                    nodes[i], nodes[orig_pos] = nodes[orig_pos], nodes[i]
                    swaps += 1
                    i -= 1
                i += 1

        return swaps
