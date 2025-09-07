"""
Leetcode
2025-09-07
1304. Find N Unique Integers Sum up to Zero
Easy

Given an integer n, return any array containing n unique integers such that they add up to 0.

 

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

Example 2:

Input: n = 3
Output: [-1,0,1]

Example 3:

Input: n = 1
Output: [0]

 

Constraints:

    1 <= n <= 1000


Hint 1
Return an array where the values are symmetric. (+x , -x).
Hint 2
If n is odd, append value 0 in your returned array.
"""

from typing import List


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.93MB Beats 36.29%
    """

    def sumZero(self, n: int) -> List[int]:
        ans = [0] * n
        start = 1 if n & 1 == 1 else 0
        num = 1
        for i in range(start, n, 2):
            ans[i] = num
            ans[i+1] = -num
            num += 1
        return ans


class Solution1:
    """
    leetcode solution
    Runtime 0ms Beats 100.00%
    Memory 18.07MB Beats 13.47%
    """

    def sumZero(self, n: int) -> List[int]:
        ans = []
        for i in range(1, n // 2 + 1):
            ans.append(i)
            ans.append(-i)
        if n % 2 == 1:
            ans.append(0)
        return ans
