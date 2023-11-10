"""
Leetcode
1743. Restore the Array From Adjacent Pairs (medium)
2023-11-10

There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.

You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.

It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.

Return the original array nums. If there are multiple solutions, return any of them.

 

Example 1:

Input: adjacentPairs = [[2,1],[3,4],[3,2]]
Output: [1,2,3,4]
Explanation: This array has all its adjacent pairs in adjacentPairs.
Notice that adjacentPairs[i] may not be in left-to-right order.

Example 2:

Input: adjacentPairs = [[4,-2],[1,4],[-3,1]]
Output: [-2,4,1,-3]
Explanation: There can be negative numbers.
Another solution is [-3,1,4,-2], which would also be accepted.

Example 3:

Input: adjacentPairs = [[100000,-100000]]
Output: [100000,-100000]

 

Constraints:

    nums.length == n
    adjacentPairs.length == n - 1
    adjacentPairs[i].length == 2
    2 <= n <= 10^5
    -10^5 <= nums[i], ui, vi <= 10^5
    There exists some nums that has adjacentPairs as its pairs.

Hints:
- Find the first element of nums - it will only appear once in adjacentPairs.
- The adjacent pairs are like edges of a graph. Perform a depth-first search from the first element.
"""

from typing import List
from collections import defaultdict, deque


class Solution:
    """
    Runtime: 2203 ms, faster than 5.24% of Python3 online submissions for Restore the Array From Adjacent Pairs.
    Memory Usage: 66.9 MB, less than 61.69% of Python3 online submissions for Restore the Array From Adjacent Pairs.
    """

    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        neibs = defaultdict(list)

        for a, b in adjacentPairs:
            neibs[a].append(b)
            neibs[b].append(a)

        LEFT = 0
        RIGHT = 1

        start_left, start_right = adjacentPairs[0]

        ans = [start_left, start_right]

        seen = {start_left, start_right}

        q = deque([(start_left, LEFT), (start_right, RIGHT)])

        while q:
            num, side = q.popleft()
            for neib in neibs[num]:
                if neib in seen:
                    continue
                if side == LEFT:
                    ans.insert(0, neib)
                    q.append((neib, LEFT))
                else:
                    ans.append(neib)
                    q.append((neib, RIGHT))
                seen.add(neib)

        return ans


class Solution1:
    """
    leetcode solution 1: DFS
    Time: O(n)
    Space: O(n)
    Runtime: 1098 ms, faster than 11.70% of Python3 online submissions for Restore the Array From Adjacent Pairs.
    Memory Usage: 168.1 MB, less than 28.03% of Python3 online submissions for Restore the Array From Adjacent Pairs.
    """

    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        graph = defaultdict(list)

        for x, y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)

        root = None

        for num in graph:
            if len(graph[num]) == 1:
                root = num
                break

        def dfs(node, prev, ans):
            ans.append(node)
            for neib in graph[node]:
                if neib != prev:
                    dfs(neib, node, ans)

        ans = []
        dfs(root, None, ans)
        return ans


class Solution2:
    """
    leetcode solution 2: Iterative, Follow the Path
    Time: O(n)
    Space: O(n)
    Runtime: 858 ms, faster than 97.18% of Python3 online submissions for Restore the Array From Adjacent Pairs.
    Memory Usage: 64.8 MB, less than 93.15% of Python3 online submissions for Restore the Array From Adjacent Pairs.
    """

    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        graph = defaultdict(list)

        for x, y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)

        root = None

        for num in graph:
            if len(graph[num]) == 1:
                root = num
                break

        curr = root
        ans = [root]
        prev = None

        while len(ans) < len(graph):
            for neib in graph[curr]:
                if neib != prev:
                    ans.append(neib)
                    prev = curr
                    curr = neib
                    break

        return ans
