"""
Leetcode
1029. Two City Scheduling (medium)
2022-03-25

A company is planning to interview 2n people. Given the array costs 
where costs[i] = [aCosti, bCosti], the cost of flying the ith person 
to city a is aCosti, and the cost of flying the ith person to city b 
is bCosti.

Return the minimum cost to fly every person to a city such that 
exactly n people arrive in each city.
"""

from typing import List



# try 1
# wrong
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # return sum([min(x) for x in costs])

        l = len(costs)
        n = l // 2
        a, b = 0, 0
        cost = 0

        available = [1] * l

        qa = [(i,v[0]) for i,v in enumerate(costs)]
        qa.sort(key=lambda x: x[1])
        qb = [(i,v[1]) for i,v in enumerate(costs)]
        qb.sort(key=lambda x: x[1])
        
        while a < n and b < n:
            if not available[qb[0][0]]:
                qb.pop(0)
            elif not available[qa[0][0]]:
                qa.pop(0)
            elif qa[0][1] < qb[0][1]:
                a += 1
                tmp = qa.pop(0)
                cost += tmp[1]
                available[tmp[0]] = 0
            elif qa[0][1] > qb[0][1]:
                b += 1
                tmp = qb.pop(0)
                cost += tmp[1]
                available[tmp[0]] = 0

        if a < n:
            for x in qa:
                if available[x[0]]: cost += x[1]
        if b < n:
            for x in qb:
                if available[x[0]]: cost += x[1]

        return cost        



# try 2
# based on
# https://leetcode.com/problems/two-city-scheduling/discuss/1881058/0ms-or-Easy-or-sorting-+-just-1-loop-or-Elaborately-Explained
# Runtime: 52 ms, faster than 65.18% of Python3 online submissions for Two City Scheduling.
# Memory Usage: 14 MB, less than 45.30% of Python3 online submissions for Two City Scheduling.
class Solution1:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        cost = 0
        available = [1] * len(costs)
        priority = [0] * len(costs)
        
        for i,x in enumerate(costs):
            priority[i] = (x[0] - x[1], i)
        priority.sort(key=lambda x: x[0])
        
        # city A
        for i in range(len(costs) // 2):
            available[priority[i][1]] = 0
            cost += costs[priority[i][1]][0]

        # city B
        for i in range(len(costs)):
            if available[i]: cost += costs[i][1]

        return cost



# by @artod
# https://leetcode.com/problems/two-city-scheduling/discuss/1881054/Python3-2-LINERS-**-Explained
# Runtime: 54 ms, faster than 61.71% of Python3 online submissions for Two City Scheduling.
# Memory Usage: 13.9 MB, less than 45.30% of Python3 online submissions for Two City Scheduling.
class Solution2:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs, L = sorted(costs, key = lambda a: a[0] - a[1]), len(costs)//2
        return sum(c[0] for c in costs[:L]) + sum(c[1] for c in costs[L:])



s = Solution1()
tests = [
    [[10,20],[30,200],[400,50],[30,20]],
    [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]],
    [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
]
for t in tests:
    print(t)
    print(s.twoCitySchedCost(t))
    print()
