"""
Leetcode
881. Boats to Save People (medium)
2022-03-24

You are given an array people where people[i] is the weight of 
the ith person, and an infinite number of boats where each boat 
can carry a maximum weight of limit. Each boat carries at most 
two people at the same time, provided the sum of the weight of 
those people is at most limit.

Return the minimum number of boats to carry every given person.
"""

from typing import List



# try 1
# wrong
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        
        boats = 0
        i = 0
        while i < len(people) - 1:
            if people[i] + people[i + 1] <= limit: 
                i += 2
            else: 
                i += 1
            boats += 1
        if i == len(people) - 1: 
            boats += 1
        
        return boats



# try 2
# Runtime: 618 ms, faster than 48.06% of Python3 online submissions for Boats to Save People.
# Memory Usage: 21 MB, less than 34.38% of Python3 online submissions for Boats to Save People.
# turns out to be basically the same as the leetcode's solution
class Solution2:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()

        boats = 0
        start = 0
        end = len(people) - 1
        while start <= end:
            
            if people[start] + people[end] <= limit:
                boats += 1
                start += 1
                end -= 1
            
            else:
                boats += 1
                end -= 1

        return boats



# a bit optimized
# Runtime: 448 ms, faster than 97.32% of Python3 online submissions for Boats to Save People.
# Memory Usage: 20.8 MB, less than 96.21% of Python3 online submissions for Boats to Save People.
class Solution2:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()

        boats = 0
        start = 0
        end = len(people) - 1
        while start <= end:
            if people[start] + people[end] <= limit:
                start += 1
            boats += 1
            end -= 1

        return boats



s = Solution2()
tests = [
    [[5,1,4,2], 6],
    [[1,2], 3],
    [[3,2,2,1], 3],
    [[3,5,3,4], 5]
]
for t in tests:
    print(t)
    print(s.numRescueBoats(t[0], t[1]))
    print()
