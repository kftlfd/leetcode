"""
Leetcode
682. Baseball Game (easy)
2022-04-10

You are keeping score for a baseball game with strange rules. The game 
consists of several rounds, where the scores of past rounds may affect 
future rounds' scores.

At the beginning of the game, you start with an empty record. You are 
given a list of strings ops, where ops[i] is the ith operation you 
must apply to the record and is one of the following:

 1. An integer x - Record a new score of x.
 2. "+" - Record a new score that is the sum of the previous two scores. 
    It is guaranteed there will always be two previous scores.
 3. "D" - Record a new score that is double the previous score. It is 
    guaranteed there will always be a previous score.
 4. "C" - Invalidate the previous score, removing it from the record. It 
    is guaranteed there will always be a previous score.

Return the sum of all the scores on the record.
"""

from typing import List


# try 1
# Runtime: 40 ms, faster than 93.04% of Python3 online submissions for Baseball Game.
# Memory Usage: 14.1 MB, less than 34.49% of Python3 online submissions for Baseball Game.
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        record = []        
        for op in ops:
            if op == "C": record.pop()
            elif op == "D": record.append(record[-1] * 2)
            elif op == "+": record.append(record[-1] + record[-2])
            else: record.append(int(op))
        return sum(record)



s = Solution()
tests = [
    ["5","2","C","D","+"],
    ["5","-2","4","C","D","9","+","+"],
    ["1"]
]
for t in tests:
    print(t)
    print(s.calPoints(t))
    print()
