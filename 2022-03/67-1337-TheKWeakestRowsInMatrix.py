"""
Leetcode
1337. The K Weakest Rows in a Matrix (easy)
2022-03-27

You are given an m x n binary matrix mat of 1's (representing soldiers) 
and 0's (representing civilians). The soldiers are positioned in front 
of the civilians. That is, all the 1's will appear to the left of all 
the 0's in each row.

A row i is weaker than a row j if one of the following is true:

 - The number of soldiers in row i is less than the number of soldiers 
   in row j.
 - Both rows have the same number of soldiers and i < j.

Return the indices of the k weakest rows in the matrix ordered from 
weakest to strongest.
"""

from typing import List



# try 1
# Runtime: 129 ms, faster than 72.58% of Python3 online submissions for The K Weakest Rows in a Matrix.
# Memory Usage: 14.1 MB, less than 90.64% of Python3 online submissions for The K Weakest Rows in a Matrix.
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        mat_sorted = [(v,i) for i,v in enumerate([sum(row) for row in mat])]
        mat_sorted.sort()
        out = []
        for i in range(k):
            out.append(mat_sorted[i][1])
        return out



s = Solution()
tests = [
    [[[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], 3],
    [[[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]], 2]
]
for t in tests:
    print(t)
    print(s.kWeakestRows(t[0], t[1]))
    print()
