"""
Leetcode
2026-07-10
3534. Path Existence Queries in a Graph II
Hard

You are given an integer n representing the number of nodes in a graph, labeled from 0 to n - 1.

You are also given an integer array nums of length n and an integer maxDiff.

An undirected edge exists between nodes i and j if the absolute difference between nums[i] and nums[j] is at most maxDiff (i.e., |nums[i] - nums[j]| <= maxDiff).

You are also given a 2D integer array queries. For each queries[i] = [ui, vi], find the minimum distance between nodes ui and vi. If no path exists between the two nodes, return -1 for that query.

Return an array answer, where answer[i] is the result of the ith query.

Note: The edges between the nodes are unweighted.

 

Example 1:

Input: n = 5, nums = [1,8,3,4,2], maxDiff = 3, queries = [[0,3],[2,4]]

Output: [1,1]

Explanation:

The resulting graph is:

Query	Shortest Path	Minimum Distance
[0, 3]	0 → 3	1
[2, 4]	2 → 4	1

Thus, the output is [1, 1].

Example 2:

Input: n = 5, nums = [5,3,1,9,10], maxDiff = 2, queries = [[0,1],[0,2],[2,3],[4,3]]

Output: [1,2,-1,1]

Explanation:

The resulting graph is:

Query	Shortest Path	Minimum Distance
[0, 1]	0 → 1	1
[0, 2]	0 → 1 → 2	2
[2, 3]	None	-1
[4, 3]	3 → 4	1

Thus, the output is [1, 2, -1, 1].

Example 3:

Input: n = 3, nums = [3,6,1], maxDiff = 1, queries = [[0,0],[0,1],[1,2]]

Output: [0,-1,-1]

Explanation:

There are no edges between any two nodes because:

    Nodes 0 and 1: |nums[0] - nums[1]| = |3 - 6| = 3 > 1
    Nodes 0 and 2: |nums[0] - nums[2]| = |3 - 1| = 2 > 1
    Nodes 1 and 2: |nums[1] - nums[2]| = |6 - 1| = 5 > 1

Thus, no node can reach any other node, and the output is [0, -1, -1].

 

Constraints:

    1 <= n == nums.length <= 10^5
    0 <= nums[i] <= 10^5
    0 <= maxDiff <= 10^5
    1 <= queries.length <= 10^5
    queries[i] == [ui, vi]
    0 <= ui, vi < n


Hint 1
Sort the nodes according to nums[i].
Hint 2
Can we use binary jumping?
Hint 3
Use binary jumping with a sparse table data structure.
"""

from typing import List


class Solution1:
    """
    Sorting + Two Pointers + Binary Lifting
    https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/solutions/8387302/sorting-two-pointers-binary-lifting-on-l-qgju
    Runtime 1799ms Beats 48.39%
    Memory 88.49MB Beats 45.16%
    """

    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        new_nums = sorted(enumerate(nums), key=lambda x: x[1])
        get_i = [0] * n
        for i, (orig, _) in enumerate(new_nums):
            get_i[orig] = i

        LOG = 18
        st = [[0] * LOG for _ in range(n)]

        r = 0
        for i in range(n):
            if r < i:
                r = i
            while (r + 1 < n and
                   new_nums[r + 1][1] - new_nums[r][1] <= maxDiff and
                   new_nums[r + 1][1] - new_nums[i][1] <= maxDiff):
                r += 1
            st[i][0] = r

        for j in range(1, LOG):
            for i in range(n):
                st[i][j] = st[st[i][j - 1]][j - 1]

        ans = []
        for u, v in queries:
            a, b = get_i[u], get_i[v]
            if a > b:
                a, b = b, a
            if a == b:
                ans.append(0)
                continue

            curr, steps = a, 0
            for j in range(LOG - 1, -1, -1):
                if st[curr][j] < b:
                    curr = st[curr][j]
                    steps += (1 << j)

            ans.append(steps + 1 if st[curr][0] >= b else -1)

        return ans
