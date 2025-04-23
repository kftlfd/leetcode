"""
Leetcode
2025-04-24
1399. Count Largest Group
Easy

You are given an integer n.

Each number from 1 to n is grouped according to the sum of its digits.

Return the number of groups that have the largest size.



Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
There are 4 groups with largest size.

Example 2:

Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.



Constraints:

    1 <= n <= 10^4


"""

from collections import Counter


class Solution:
    """
    Runtime 27ms Beats 71.29%
    Memory 17.82MB Beats 53.28%
    """

    def countLargestGroup(self, n: int) -> int:
        sums = Counter(self.digits_sum(i) for i in range(1, n + 1))
        groups = Counter(sums.values())
        return groups[max(sums.values())]

    def digits_sum(self, n: int) -> int:
        res = 0
        while n > 0:
            res += n % 10
            n //= 10
        return res


class Solution1:
    """
    leetcode solution
    Runtime 72ms Beats 9.98%
    Memory 17.79MB Beats 72.02%
    """

    def countLargestGroup(self, n: int) -> int:
        hashMap = Counter()
        for i in range(1, n + 1):
            key = sum([int(x) for x in str(i)])
            hashMap[key] += 1
        maxValue = max(hashMap.values())
        count = sum(1 for v in hashMap.values() if v == maxValue)
        return count
