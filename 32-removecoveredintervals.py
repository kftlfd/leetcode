'''
Leetcode
1288. Remove Covered Intervals (medium)
2022-02-20

Given an array intervals where intervals[i] = [li, ri] represent 
the interval [li, ri), remove all intervals that are covered by 
another interval in the list.

The interval [a, b) is covered by the interval [c, d) if and only 
if c <= a and b <= d.

Return the number of remaining intervals.
'''

from typing import List



# brute force
# Runtime: 203 ms, faster than 12.21% of Python3 online submissions for Remove Covered Intervals.
# Memory Usage: 14.4 MB, less than 96.36% of Python3 online submissions for Remove Covered Intervals.
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        remains = len(intervals)
        
        # for every interval - intervals[i]
        for i in range(len(intervals)):
            
            # look at every other interval - interval[j]
            for j in range(len(intervals)):
                
                # if it (i) is covered by another (j), remove it
                if i != j and intervals[i][0] >= intervals[j][0] and intervals[i][1] <= intervals[j][1]:
                    remains -= 1
                    break
                    
        return remains



# try 2
# Runtime: 132 ms, faster than 52.47% of Python3 online submissions for Remove Covered Intervals.
# Memory Usage: 14.4 MB, less than 86.23% of Python3 online submissions for Remove Covered Intervals.
class Solution2:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        i = len(intervals) - 1
        
        # sort by 1) decreasing start index, 2) increasing end index
        intervals.sort(key=lambda i: (-i[0], i[1]))
        
        # go from end to start
        right = intervals[-1][0] - 1
        while i >= 0:
            
            # for every starting index leave only one with biggest end index
            if intervals[i][0] <= right:
                intervals.pop(i)
            else:
                right = intervals[i][0]
                
                # check if not covered by intervals with earlier starting indexes
                for j in range(i + 1, len(intervals)):
                    if intervals[j][0] <= intervals[i][0] and intervals[j][1] >= intervals[i][1]:
                        intervals.pop(i)
                        break
                
            i -= 1
                    
        return len(intervals)
