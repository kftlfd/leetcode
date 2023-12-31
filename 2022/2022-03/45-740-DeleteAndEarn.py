'''
Leetcode
740. Delete and Earn
2022-03-05

You are given an integer array nums. You want to maximize the number 
of points you get by performing the following operation any number 
of times:

 - Pick any nums[i] and delete it to earn nums[i] points. Afterwards, 
   you must delete every element equal to nums[i] - 1 and every element 
   equal to nums[i] + 1.

Return the maximum number of points you can earn by applying the above 
operation some number of times.

https://leetcode.com/problems/delete-and-earn/
'''

from collections import defaultdict
from functools import cache
from typing import List



# leetcode solution 1
# https://leetcode.com/problems/delete-and-earn/solution/
# Runtime: 82 ms, faster than 56.73% of Python3 online submissions for Delete and Earn.
# Memory Usage: 28 MB, less than 5.02% of Python3 online submissions for Delete and Earn.
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        points = defaultdict(int)
        max_number = 0
        # Precompute how many points we gain from taking an element
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)

        @cache
        def max_points(num):
            # Check for base cases
            if num == 0:
                return 0
            if num == 1:
                return points[1]
            
            # Apply recurrence relation
            return max(max_points(num - 1), max_points(num - 2) + points[num])
        
        return max_points(max_number)



s = Solution()
tests = [
    [3,4,2],
    [2,2,3,3,3,4]
]
for t in tests:
    print(t, "\n ->", s.deleteAndEarn(t), "\n")
