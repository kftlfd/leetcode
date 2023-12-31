'''
Leetcode
799. Champagne Tower
2022-03-04

We stack glasses in a pyramid, where the first row has 1 glass, the second 
row has 2 glasses, and so on until the 100th row.  Each glass holds one 
cup of champagne.

Then, some champagne is poured into the first glass at the top.  When the 
topmost glass is full, any excess liquid poured will fall equally to the 
glass immediately to the left and right of it.  When those glasses become 
full, any excess champagne will fall equally to the left and right of those 
glasses, and so on.  (A glass at the bottom row has its excess champagne 
fall on the floor.)

For example, after one cup of champagne is poured, the top most glass is 
full.  After two cups of champagne are poured, the two glasses on the second 
row are half full.  After three cups of champagne are poured, those two cups 
become full - there are 3 full glasses total now.  After four cups of champagne 
are poured, the third row has the middle glass half full, and the two outside 
glasses are a quarter full, as pictured below.

https://leetcode.com/problems/champagne-tower/
'''



# leetcode solution
# https://leetcode.com/problems/champagne-tower/solution/
# Runtime: 108 ms, faster than 88.84% of Python3 online submissions for Champagne Tower.
# Memory Usage: 14 MB, less than 67.48% of Python3 online submissions for Champagne Tower.
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        A = [[0] * k for k in range(1, 102)]
        A[0][0] = poured
        for r in range(query_row + 1):
            for c in range(r+1):
                q = (A[r][c] - 1.0) / 2.0
                if q > 0:
                    A[r+1][c] += q
                    A[r+1][c+1] += q

        return min(1, A[query_row][query_glass])


res = Solution().champagneTower(50, 6, 3)
print(res)