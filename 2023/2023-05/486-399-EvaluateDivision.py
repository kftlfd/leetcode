"""
Leetcode
399. Evaluate Division (medium)
2023-05-20

You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Example 1:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

Example 2:
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:
Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
"""

from typing import List
from collections import defaultdict


class Solution:
    """
    Runtime: 39 ms, faster than 47.80% of Python3 online submissions for Evaluate Division.
Memory Usage: 16.4 MB, less than 27.06% of Python3 online submissions for Evaluate Division.
    """

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        variables = set()

        divisions = defaultdict(dict)

        for pair, val in zip(equations, values):
            a, b = pair
            variables.add(a)
            variables.add(b)
            divisions[a][b] = val
            divisions[b][a] = 1 / val

        def eval_query(query: List[str]) -> float:
            a, b = query

            if a not in variables or b not in variables:
                return -1.0

            if a == b:
                return 1.0

            if b in divisions[a]:
                return divisions[a][b]

            visited = set()
            q = list(divisions[a].items())
            while q:
                val, multiplier = q.pop(0)
                visited.add(val)
                if b in divisions[val]:
                    return divisions[val][b] * multiplier
                for nxt_val in divisions[val]:
                    if nxt_val not in visited:
                        q.append(
                            (nxt_val, divisions[val][nxt_val] * multiplier))

            return -1

        return [eval_query(query) for query in queries]


s = Solution()
tests = [
    (([["a", "b"], ["b", "c"]], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]),
     [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]),

    (([["a", "b"], ["b", "c"], ["bc", "cd"]], [1.5, 2.5, 5.0], [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]),
     [3.75000, 0.40000, 5.00000, 0.20000]),

    (([["a", "b"]], [0.5], [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]),
     [0.50000, 2.00000, -1.00000, -1.00000]),
]
for inp, exp in tests:
    res = s.calcEquation(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
