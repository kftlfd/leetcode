"""
Leetcode
2026-04-21
1722. Minimize Hamming Distance After Swap Operations
Medium

You are given two integer arrays, source and target, both of length n. You are also given an array allowedSwaps where each allowedSwaps[i] = [ai, bi] indicates that you are allowed to swap the elements at index ai and index bi (0-indexed) of array source. Note that you can swap elements at a specific pair of indices multiple times and in any order.

The Hamming distance of two arrays of the same length, source and target, is the number of positions where the elements are different. Formally, it is the number of indices i for 0 <= i <= n-1 where source[i] != target[i] (0-indexed).

Return the minimum Hamming distance of source and target after performing any amount of swap operations on array source.

 

Example 1:

Input: source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
Output: 1
Explanation: source can be transformed the following way:
- Swap indices 0 and 1: source = [2,1,3,4]
- Swap indices 2 and 3: source = [2,1,4,3]
The Hamming distance of source and target is 1 as they differ in 1 position: index 3.

Example 2:

Input: source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []
Output: 2
Explanation: There are no allowed swaps.
The Hamming distance of source and target is 2 as they differ in 2 positions: index 1 and index 2.

Example 3:

Input: source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]
Output: 0

 

Constraints:

    n == source.length == target.length
    1 <= n <= 10^5
    1 <= source[i], target[i] <= 10^5
    0 <= allowedSwaps.length <= 10^5
    allowedSwaps[i].length == 2
    0 <= ai, bi <= n - 1
    ai != bi


Hint 1
The source array can be imagined as a graph where each index is a node and each allowedSwaps[i] is an edge.
Hint 2
Nodes within the same component can be freely swapped with each other.
Hint 3
For each component, find the number of common elements. The elements that are not in common will contribute to the total Hamming distance.
"""

from collections import Counter, defaultdict
from typing import List


class Solution:
    """
    Runtime 258ms Beats 51.13%
    Memory 54.84MB Beats 82.71%
    """

    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)

        root = list(range(n))

        def find(x: int) -> int:
            r = root[x]
            while root[r] != r:
                r = root[r]
            return r

        def union(x: int, y: int):
            rx = find(x)
            yx = find(y)
            root[yx] = rx

        for x, y in allowedSwaps:
            union(x, y)

        root = [find(i) for i in range(n)]

        cnt = defaultdict(Counter)

        for i, src in enumerate(source):
            cnt[root[i]][src] += 1

        ans = 0

        for i, tgt in enumerate(target):
            if cnt[root[i]][tgt] > 0:
                cnt[root[i]][tgt] -= 1
            else:
                ans += 1

        return ans


class Solution2:
    """
    leetcode solution: Hash Table + Union-Find Set
    Runtime 193ms Beats 81.20%
    Memory 54.54MB Beats 86.47%
    """

    class UnionFind:
        def __init__(self, n):
            self.fa = list(range(n))
            self.rank = [0] * n

        def find(self, x):
            if self.fa[x] != x:
                self.fa[x] = self.find(self.fa[x])
            return self.fa[x]

        def union(self, x, y):
            x = self.find(x)
            y = self.find(y)
            if x == y:
                return
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            self.fa[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        uf = self.UnionFind(n)
        for a, b in allowedSwaps:
            uf.union(a, b)

        sets = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            f = uf.find(i)
            sets[f][source[i]] += 1

        ans = 0
        for i in range(n):
            f = uf.find(i)
            if sets[f][target[i]] > 0:
                sets[f][target[i]] -= 1
            else:
                ans += 1
        return ans
