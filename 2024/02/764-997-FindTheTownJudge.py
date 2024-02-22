"""
Leetcode
997. Find the Town Judge
Easy
2024-02-22

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

    The town judge trusts nobody.
    Everybody (except for the town judge) trusts the town judge.
    There is exactly one person that satisfies properties 1 and 2.

You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

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

 

Constraints:

    1 <= n <= 1000
    0 <= trust.length <= 104
    trust[i].length == 2
    All the pairs of trust are unique.
    ai != bi
    1 <= ai, bi <= n
"""

from typing import List


class Solution:
    """
    Runtime: 582 ms, faster than 96.73% of Python3 online submissions for Find the Town Judge.
    Memory Usage: 21.7 MB, less than 45.77% of Python3 online submissions for Find the Town Judge.
    """

    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ht = list(map(lambda x: [], [0] * n))

        for a, b in trust:
            ht[a - 1].append(b)

        for i in range(1, n + 1):
            if not ht[i - 1] and \
                    all(i in trusts for trusts in ht[:i-1]) and \
                    all(i in trusts for trusts in ht[i:]):
                return i

        return -1


class Solution1:
    """
    https://leetcode.com/problems/find-the-town-judge/discuss/242938/JavaC++Python-Directed-Graph
    Runtime: 578 ms, faster than 98.62% of Python3 online submissions for Find the Town Judge.
    Memory Usage: 21.6 MB, less than 86.28% of Python3 online submissions for Find the Town Judge.
    """

    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        points = [0] * (n + 1)

        for a, b in trust:
            points[a] -= 1
            points[b] += 1

        for i in range(1, n + 1):
            if points[i] == n - 1:
                return i

        return -1
