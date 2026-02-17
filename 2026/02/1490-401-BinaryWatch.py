"""
Leetcode
2026-02-17
401. Binary Watch
Easy

A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

    For example, the below binary watch reads "4:51".

Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), return all possible times the watch could represent. You may return the answer in any order.

The hour must not contain a leading zero.

    For example, "01:00" is not valid. It should be "1:00".

The minute must consist of two digits and may contain a leading zero.

    For example, "10:2" is not valid. It should be "10:02".

 

Example 1:

Input: turnedOn = 1
Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]

Example 2:

Input: turnedOn = 9
Output: []

 

Constraints:

    0 <= turnedOn <= 10


"""

from collections import defaultdict
from typing import List


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 19.38MB Beats 60.29%
    """

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn < 1:
            return ["0:00"]
        if turnedOn > 8:
            return []

        hours = defaultdict(list)
        for i in range(11 + 1):
            hours[i.bit_count()].append(i)

        minutes = defaultdict(list)
        for i in range(59 + 1):
            minutes[i.bit_count()].append(i)

        res = []
        for h in range(turnedOn + 1):
            m = turnedOn - h
            for hour in hours[h]:
                for minute in minutes[m]:
                    res.append(f"{hour}:{"0" if minute < 10 else ""}{minute}")

        return res


class Solution1:
    """
    leetcode solution 1: Enumerating Hours and Minutes
    Runtime 0ms Beats 100.00%
    Memory 19.19MB Beats 70.76%
    """

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        for h in range(12):
            for m in range(60):
                if h.bit_count() + m.bit_count() == turnedOn:
                    ans.append(f"{h}:{m:02d}")
        return ans


class Solution2:
    """
    leetcode solution 2: Binary Enumeration
    Runtime 2ms Beats 32.01%
    Memory 19.32MB Beats 60.29%
    """

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        for i in range(1024):
            h, m = (
                i >> 6,
                i & 0x3F,
            )  # Extract the high 4 bits and low 6 bits using bitwise operations
            if h < 12 and m < 60 and bin(i).count("1") == turnedOn:
                ans.append(f"{h}:{m:02d}")
        return ans
