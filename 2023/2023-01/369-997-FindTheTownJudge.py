"""
Leetcode
997. Find the Town Judge (easy)
2023-01-23

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

    The town judge trusts nobody.
    Everybody (except for the town judge) trusts the town judge.
    There is exactly one person that satisfies properties 1 and 2.

You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

Example 1:
Input: n = 2, trust = [[1,2]]
Output: 2

Example 2:
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
"""

from typing import List, Optional
from collections import defaultdict


# Runtime: 1817 ms, faster than 25.04% of Python3 online submissions for Find the Town Judge.
# Memory Usage: 19.1 MB, less than 25.51% of Python3 online submissions for Find the Town Judge.
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        if not trust:
            return 1 if n == 1 else -1

        trusts_to = defaultdict(list)
        trust_from = defaultdict(list)

        for a, b in trust:
            trusts_to[a].append(b)
            trust_from[b].append(a)

        judge = -1

        for suspect, people in trust_from.items():
            if len(people) == n-1 and len(trusts_to[suspect]) == 0:
                if judge > 0:  # check that only one judge is present
                    return -1
                judge = suspect

        return judge


# https://leetcode.com/problems/find-the-town-judge/discuss/242938/JavaC++Python-Directed-Graph
# Runtime: 985 ms, faster than 39.21% of Python3 online submissions for Find the Town Judge.
# Memory Usage: 19 MB, less than 25.51% of Python3 online submissions for Find the Town Judge.
class Solution1:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count = [0] * (n + 1)
        for i, j in trust:
            count[i] -= 1
            count[j] += 1
        for i in range(1, n + 1):
            if count[i] == n - 1:
                return i
        return -1


s = Solution1()
tests = [
    ((2, [[1, 2]]),
     2),

    ((3, [[1, 3], [2, 3]]),
     3),

    ((3, [[1, 3], [2, 3], [3, 1]]),
     -1),

    ((1, []),
     1),
]
for inp, exp in tests:
    n, trust = inp
    res = s.findJudge(n, trust)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
