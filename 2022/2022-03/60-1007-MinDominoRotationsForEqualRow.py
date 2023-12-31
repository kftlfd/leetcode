"""
Leetcode
1007. Minimum Domino Rotations For Equal Row (medium)
2022-03-20

In a row of dominoes, tops[i] and bottoms[i] represent the top and 
bottom halves of the ith domino. (A domino is a tile with two numbers 
from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops 
are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.
"""

from typing import List



# try 1
# wrong: trying to make equal only the top row
from collections import Counter
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        n = len(tops)
        
        counter_t = Counter()
        counter_b = Counter()
        for i in range(n):
            counter_t[tops[i]] += 1
            if tops[i] != bottoms[i]:
                counter_b[bottoms[i]] += 1
        
        candidates = []
        for x in counter_t.keys():
            if counter_t[x] == n:
                candidates.append((x,counter_t[x]))
                continue
            if x in counter_b.keys() and counter_t[x] + counter_b[x] == n:
                candidates.append((x,counter_t[x]))
        if not candidates: return -1

        candidates.sort(key=lambda x: x[1])

        return n - candidates[0][1]



# try 2
# Runtime: 1387 ms, faster than 58.73% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
# Memory Usage: 15.2 MB, less than 44.98% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
class Solution1:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        n = len(tops)

        count_t = {}
        count_b = {}
        for i in range(1,7):
            count_t[i] = [0,0]
            count_b[i] = [0,0]

        for i in range(n):
            count_t[tops[i]][0] += 1
            count_b[bottoms[i]][0] += 1
            if tops[i] != bottoms[i]:
                count_t[bottoms[i]][1] += 1
                count_b[tops[i]][1] += 1

        out = n + 1
        for x in count_t.values():
            if x[0] + x[1] == n:
                out = min(out, min(x[0],x[1]))
        for x in count_b.values():
            if x[0] + x[1] == n:
                if out > min(x[0], x[1]): out = min(x[0], x[1])

        return -1 if out >= n else out



# Runtime: 2371 ms, faster than 5.02% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
# Memory Usage: 15 MB, less than 77.02% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
class Solution2:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        n = len(tops)

        count_t = [ [0,0] for i in range(6) ]
        count_b = [ [0,0] for i in range(6) ]
        for i in range(n):

            count_t[tops[i]-1][0] += 1
            count_b[bottoms[i]-1][0] += 1

            if tops[i] != bottoms[i]:
                count_t[bottoms[i]-1][1] += 1
                count_b[tops[i]-1][1] += 1

        out = n + 1
        for x in count_t + count_b:
            if x[0] + x[1] == n:
                out = min(out, min(x[0],x[1]))

        return -1 if out >= n else out



# inspired by
# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/discuss/252242/JavaC++Python-Different-Ideas
# Runtime: 1296 ms, faster than 71.17% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
# Memory Usage: 15.1 MB, less than 77.02% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
class Solution3:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        n = len(tops)

        count_t = Counter(tops)
        count_b = Counter(bottoms)
        same = Counter([y for y in map(lambda x: x[0] if x[0] == x[1] else None, zip(tops, bottoms)) ])

        out = n + 1
        for i in range(1,7):
            if i in count_t and i in count_b and count_t[i] + count_b[i] - same[i] == n:
                out = min(out, min(n - count_t[i], n - count_b[i]))

        return -1 if out >= n else out



# by @artod
# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/discuss/1865333/Python3-UNPRECENDENT-NUMBER-OF-COUNTERS-o()o-Explained
# Runtime: 2227 ms, faster than 7.00% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
# Memory Usage: 15.1 MB, less than 77.02% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
class Solution4:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        total = len(tops)
        top_fr, bot_fr, val_total = [0]*7, [0]*7, [total]*7
        for top, bot in zip(tops, bottoms):
            if top == bot:
                val_total[top] -= 1
            else:
                top_fr[top] += 1
                bot_fr[bot] += 1
                
        for val in range(1, 7):
            if (val_total[val] - top_fr[val]) == bot_fr[val]:
                return min(top_fr[val], bot_fr[val])
            
        return -1



s = Solution4()
tests = [
    [ [1,2,1,1,1,2,2,2], [2,1,2,2,2,2,2,2] ],
    [ [1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1] ],
    [ [2,1,2,4,2,2], [5,2,6,2,3,2] ],
    [ [3,5,1,2,3], [3,6,3,3,4] ]
]
for t in tests:
    print(*t)
    print(s.minDominoRotations(t[0], t[1]))
    print()
