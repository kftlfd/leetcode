"""
Leetcode
1578. Minimum Time to Make Rope Colorful (medium)
2022-10-03

Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

Return the minimum time Bob needs to make the rope colorful.

Example 1:
Input: colors = "abaac", neededTime = [1,2,3,4,5]
Output: 3
Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
Bob can remove the blue balloon at index 2. This takes 3 seconds.
There are no longer two consecutive balloons of the same color. Total time = 3.

Example 2:
Input: colors = "abc", neededTime = [1,2,3]
Output: 0
Explanation: The rope is already colorful. Bob does not need to remove any balloons from the rope.

Example 3:
Input: colors = "aabaa", neededTime = [1,2,3,4,1]
Output: 2
Explanation: Bob will remove the ballons at indices 0 and 4. Each ballon takes 1 second to remove.
There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.
"""

from typing import List


# leetcode solution 1
# Runtime: 2961 ms, faster than 15.54% of Python3 online submissions for Minimum Time to Make Rope Colorful.
# Memory Usage: 25 MB, less than 52.92% of Python3 online submissions for Minimum Time to Make Rope Colorful.
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        total_time = 0

        # two pointers
        i = 0
        j = 0

        while i < len(neededTime) and j < len(neededTime):
            curr_total = 0
            curr_max = 0

            # Find all the balloons having the same color as the
            # balloon indexed at i, record the total removal time
            # and the maximum removal time.
            while j < len(neededTime) and colors[i] == colors[j]:
                curr_total += neededTime[j]
                curr_max = max(curr_max, neededTime[j])
                j += 1

            # Once we reach the end of the current group, add the cost of
            # this group to total_time, and reset two pointers.
            total_time += curr_total - curr_max
            i = j

        return total_time


# leetcode solution 2
# Runtime: 1316 ms, faster than 83.60% of Python3 online submissions for Minimum Time to Make Rope Colorful.
# Memory Usage: 25 MB, less than 52.92% of Python3 online submissions for Minimum Time to Make Rope Colorful.
class Solution1:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        # totalTime: total time needed to make rope colorful;
        # currMaxTime: maximum time of a balloon needed in this group.
        total_time = 0
        curr_max_time = 0

        # For each balloon in the array:
        for i in range(len(colors)):
            # If this balloon is the first balloon of a new group
            # set the curr_max_time as 0.
            if i > 0 and colors[i] != colors[i - 1]:
                curr_max_time = 0

            # Increment total_time by the smaller one.
            # Update curr_max_time as the larger one.
            total_time += min(curr_max_time, neededTime[i])
            curr_max_time = max(curr_max_time, neededTime[i])

        # Return total_time as the minimum removal time.
        return total_time


s = Solution()
tests = [
    ("abaac", [1, 2, 3, 4, 5]),
    ("abc", [1, 2, 3]),
    ("aabaa", [1, 2, 3, 4, 1]),
]
for t in tests:
    print(t)
    colors, neededTime = t
    print(s.minCost(colors, neededTime))
    print()
