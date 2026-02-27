"""
Leetcode
2026-02-27
3666. Minimum Operations to Equalize Binary String
Hard

You are given a binary string s, and an integer k.

In one operation, you must choose exactly k different indices and flip each '0' to '1' and each '1' to '0'.

Return the minimum number of operations required to make all characters in the string equal to '1'. If it is not possible, return -1.

 

Example 1:

Input: s = "110", k = 1

Output: 1

Explanation:

    There is one '0' in s.
    Since k = 1, we can flip it directly in one operation.

Example 2:

Input: s = "0101", k = 3

Output: 2

Explanation:

One optimal set of operations choosing k = 3 indices in each operation is:

    Operation 1: Flip indices [0, 1, 3]. s changes from "0101" to "1000".
    Operation 2: Flip indices [1, 2, 3]. s changes from "1000" to "1111".

Thus, the minimum number of operations is 2.

Example 3:

Input: s = "101", k = 2

Output: -1

Explanation:

Since k = 2 and s has only one '0', it is impossible to flip exactly k indices to make all '1'. Hence, the answer is -1.

 

Constraints:

    1 <= s.length <= 10^5
    s[i] is either '0' or '1'.
    1 <= k <= s.length


Hint 1
Model state as z = number of zeros; flipping k picks i zeros (i between max(0, k - (n - z)) and min(k, z)) and transforms z to z' = z + k - 2 * i, so z' lies in a contiguous range and has parity (z + k) % 2.
Hint 2
Build a graph on states 0..n and run BFS from initial z to reach 0; each edge from z goes to all z' in that computed interval.
Hint 3
For speed, keep two ordered sets of unvisited states by parity and erase ranges with lower_bound while BFSing to achieve near O(n log n) time.
"""

from collections import deque
import math
from sortedcontainers import SortedList


class Solution:
    """
    leetcode solution: Breadth-First Search
    Runtime 3400ms Beats 6.00%
    Memory 24.83MB Beats 36.00%
    """

    def minOperations(self, s: str, k: int) -> int:
        n, m = len(s), s.count("0")
        dist = [math.inf] * (n + 1)
        nodeSets = [
            SortedList(range(0, n + 1, 2)),
            SortedList(range(1, n + 1, 2)),
        ]
        q = deque([m])
        dist[m] = 0
        nodeSets[m % 2].remove(m)
        while q:
            m = q.popleft()
            c1, c2 = max(k - n + m, 0), min(m, k)
            lnode, rnode = m + k - 2 * c2, m + k - 2 * c1
            nodeSet = nodeSets[lnode % 2]
            idx = nodeSet.bisect_left(lnode)
            while idx < len(nodeSet) and nodeSet[idx] <= rnode:
                m2 = nodeSet[idx]
                dist[m2] = dist[m] + 1
                q.append(m2)
                nodeSet.pop(idx)
        return -1 if dist[0] == math.inf else dist[0]
