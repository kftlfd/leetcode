"""
Leetcode
2024-12-22
2940. Find Building Where Alice and Bob Can Meet
Hard

You are given a 0-indexed array heights of positive integers, where heights[i] represents the height of the ith building.

If a person is in building i, they can move to any other building j if and only if i < j and heights[i] < heights[j].

You are also given another array queries where queries[i] = [ai, bi]. On the ith query, Alice is in building ai while Bob is in building bi.

Return an array ans where ans[i] is the index of the leftmost building where Alice and Bob can meet on the ith query. If Alice and Bob cannot move to a common building on query i, set ans[i] to -1.

 

Example 1:

Input: heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]
Output: [2,5,-1,5,2]
Explanation: In the first query, Alice and Bob can move to building 2 since heights[0] < heights[2] and heights[1] < heights[2]. 
In the second query, Alice and Bob can move to building 5 since heights[0] < heights[5] and heights[3] < heights[5]. 
In the third query, Alice cannot meet Bob since Alice cannot move to any other building.
In the fourth query, Alice and Bob can move to building 5 since heights[3] < heights[5] and heights[4] < heights[5].
In the fifth query, Alice and Bob are already in the same building.  
For ans[i] != -1, It can be shown that ans[i] is the leftmost building where Alice and Bob can meet.
For ans[i] == -1, It can be shown that there is no building where Alice and Bob can meet.

Example 2:

Input: heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]
Output: [7,6,-1,4,6]
Explanation: In the first query, Alice can directly move to Bob's building since heights[0] < heights[7].
In the second query, Alice and Bob can move to building 6 since heights[3] < heights[6] and heights[5] < heights[6].
In the third query, Alice cannot meet Bob since Bob cannot move to any other building.
In the fourth query, Alice and Bob can move to building 4 since heights[3] < heights[4] and heights[0] < heights[4].
In the fifth query, Alice can directly move to Bob's building since heights[1] < heights[6].
For ans[i] != -1, It can be shown that ans[i] is the leftmost building where Alice and Bob can meet.
For ans[i] == -1, It can be shown that there is no building where Alice and Bob can meet.

 

Constraints:

    1 <= heights.length <= 5 * 10^4
    1 <= heights[i] <= 10^9
    1 <= queries.length <= 5 * 10^4
    queries[i] = [ai, bi]
    0 <= ai, bi <= heights.length - 1

Hints:
- For each query [x, y], if x > y, swap x and y. Now, we can assume that x <= y.
- For each query [x, y], if x == y or heights[x] < heights[y], then the answer is y since x ≤ y.
- Otherwise, we need to find the smallest index t such that y < t and heights[x] < heights[t]. Note that heights[y] <= heights[x], so heights[x] < heights[t] is a sufficient condition.
- To find index t for each query, sort the queries in descending order of y. Iterate over the queries while maintaining a monotonic stack which we can binary search over to find index t.
"""

from collections import deque
import heapq
from typing import List


class Solution:
    """
    Time Limit Exceeded
    """

    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        next_bigger_i = {}

        stack = deque()
        for i, h in enumerate(heights):
            while stack and stack[-1][1] < h:
                next_bigger_i[stack[-1][0]] = i
                stack.pop()
            stack.append((i, h))

        ans = [-1] * len(queries)

        for i, (a, b) in enumerate(queries):
            if b < a:
                a, b = b, a

            if a == b or heights[a] < heights[b]:
                ans[i] = b
                continue

            while b in next_bigger_i:
                b = next_bigger_i[b]
                if heights[a] < heights[b]:
                    ans[i] = b
                    break

        return ans


class Solution1:
    """
    leetcode solution 1: monotonic stack
    Runtime: 475 ms, faster than 72.17% of Python3 online submissions for Find Building Where Alice and Bob Can Meet.
    Memory Usage: 46.9 MB, less than 7.22% of Python3 online submissions for Find Building Where Alice and Bob Can Meet.
    """

    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        mono_stack = []
        result = [-1 for _ in range(len(queries))]
        new_queries = [[] for _ in range(len(heights))]
        for i in range(len(queries)):
            a = queries[i][0]
            b = queries[i][1]
            if a > b:
                a, b = b, a
            if heights[b] > heights[a] or a == b:
                result[i] = b
            else:
                new_queries[b].append((heights[a], i))

        for i in range(len(heights) - 1, -1, -1):
            mono_stack_size = len(mono_stack)
            for a, b in new_queries[i]:
                position = self.search(a, mono_stack)
                if position < mono_stack_size and position >= 0:
                    result[b] = mono_stack[position][1]
            while mono_stack and mono_stack[-1][0] <= heights[i]:
                mono_stack.pop()
            mono_stack.append((heights[i], i))
        return result

    def search(self, height, mono_stack):
        left = 0
        right = len(mono_stack) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if mono_stack[mid][0] > height:
                ans = max(ans, mid)
                left = mid + 1
            else:
                right = mid - 1
        return ans


class Solution2:
    """
    leetcode solution 2: Priority Queue
    Runtime: 279 ms, faster than 95.88% of Python3 online submissions for Find Building Where Alice and Bob Can Meet.
    Memory Usage: 41.2 MB, less than 52.58% of Python3 online submissions for Find Building Where Alice and Bob Can Meet.
    """

    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        max_idx = []  # Min-heap to simulate priority queue
        results = [-1] * len(queries)
        store_queries = [[] for _ in heights]

        # Store the mappings for all queries in store_queries.
        for idx, query in enumerate(queries):
            a, b = query
            if a < b and heights[a] < heights[b]:
                results[idx] = b
            elif a > b and heights[a] > heights[b]:
                results[idx] = a
            elif a == b:
                results[idx] = a
            else:
                store_queries[max(a, b)].append(
                    (max(heights[a], heights[b]), idx)
                )

        for idx, height in enumerate(heights):
            # If the heap's smallest value is less than the current height, it is an answer to the query.
            while max_idx and max_idx[0][0] < height:
                _, q_idx = heapq.heappop(max_idx)
                results[q_idx] = idx
            # Push the queries with their maximum index as the current index into the heap.
            for element in store_queries[idx]:
                heapq.heappush(max_idx, element)

        return results


s = Solution()
tests = [
    (([6, 4, 8, 5, 2, 7], [[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]]),
        [2, 5, -1, 5, 2]),

    (([5, 3, 8, 2, 6, 1, 4, 6], [[0, 7], [3, 5], [5, 2], [3, 0], [1, 6]]),
        [7, 6, -1, 4, 6]),
]
for inp, exp in tests:
    res = s.leftmostBuildingQueries(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
