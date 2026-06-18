"""
Leetcode
2026-06-19
1344. Angle Between Hands of a Clock
Medium

Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.

Answers within 10-5 of the actual value will be accepted as correct.

 

Example 1:

Input: hour = 12, minutes = 30
Output: 165

Example 2:

Input: hour = 3, minutes = 30
Output: 75

Example 3:

Input: hour = 3, minutes = 15
Output: 7.5

 

Constraints:

    1 <= hour <= 12
    0 <= minutes <= 59


"""


class Solution01:
    """
    Runtime 0ms Beats 100.00%
    Memory 19.48MB Beats 45.34%
    """

    def angleClock(self, hour: int, minutes: int) -> float:
        hour_pos = ((hour % 12) + (minutes / 60)) * 5
        dist = abs(hour_pos - minutes)
        arc_len = min(dist, 60 - dist)  # if circumference = 60, r = ?
        # angle_deg = (l/r) * (180deg/Pi) -- where l is arc length
        # to make r = 1: (2 * Pi * r) : 60 = l : arc_len
        #   => l = (2 * Pi * arc_len) / 60
        # then: angle_deg = ((2 * Pi * arc_len) / 60) * (180deg / Pi)
        #                 = (2 * Pi * arc_len * 180) / (Pi * 60)
        #                 = arc_len * (2 * 180 / 60)
        return arc_len * 6


class Solution02:
    """
    Runtime 0ms Beats 100.00%
    Memory 19.56MB Beats 13.35%
    """

    def angleClock(self, hour: int, minutes: int) -> float:
        h = (hour * 30 % 360) + (minutes / 2)
        m = minutes * 6
        dist = abs(h - m)
        return min(dist, 360 - dist)


class Solution1:
    """
    sample 0ms solution
    """

    def angleClock(self, hour: int, minutes: int) -> float:
        ans = abs(30*hour - (11*minutes)/2)
        small = 360-ans
        if ans < small:
            return ans
        else:
            return small
