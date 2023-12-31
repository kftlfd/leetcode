"""
Leetcode
458. Poor Pigs (hard)
2022-08-06

There are buckets buckets of liquid, where exactly one of the buckets is poisonous. To figure out which one is poisonous, you feed some number of (poor) pigs the liquid to see whether they will die or not. Unfortunately, you only have minutesToTest minutes to determine which bucket is poisonous.

You can feed the pigs according to these steps:

 1. Choose some live pigs to feed.
 1. For each pig, choose which buckets to feed it. The pig will consume all the chosen buckets simultaneously and will take no time.
 3. Wait for minutesToDie minutes. You may not feed any other pigs during this time.
 4. After minutesToDie minutes have passed, any pigs that have been fed the poisonous bucket will die, and all others will survive.
 5. Repeat this process until you run out of time.

Given buckets, minutesToDie, and minutesToTest, return the minimum number of pigs needed to figure out which bucket is poisonous within the allotted time.

Example 1:
Input: buckets = 1000, minutesToDie = 15, minutesToTest = 60
Output: 5

Example 2:
Input: buckets = 4, minutesToDie = 15, minutesToTest = 15
Output: 2

Example 3:
Input: buckets = 4, minutesToDie = 15, minutesToTest = 30
Output: 2
"""

import math


# https://leetcode.com/problems/poor-pigs/discuss/2385451/C++-oror-Detail-Explanation-oror-1-Line-Codeoror-100-Fast
# Runtime: 33 ms, faster than 90.51% of Python3 online submissions for Poor Pigs.
# Memory Usage: 14 MB, less than 20.44% of Python3 online submissions for Poor Pigs.
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return math.ceil(math.log(buckets) / math.log(minutesToTest / minutesToDie + 1))


s = Solution()
tests = [
    (1000, 15, 60),
    (4, 15, 15),
    (4, 15, 30),
]
for t in tests:
    print(t)
    print(s.poorPigs(*t))
    print()
