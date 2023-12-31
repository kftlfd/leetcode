"""
Leetcode
1359. Count All Valid Pickup and Delivery Options (hard)
2023-09-10

Given n orders, each order consist in pickup and delivery services. 

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 

Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:

Input: n = 1
Output: 1
Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.

Example 2:

Input: n = 2
Output: 6
Explanation: All possible orders: 
(P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.

Example 3:

Input: n = 3
Output: 90

Constraints:

    1 <= n <= 500
"""


class Solution:
    """
    https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/discuss/516968/JavaC++Python-Easy-and-Concise
    Runtime: 33 ms, faster than 91.06% of Python3 online submissions for Count All Valid Pickup and Delivery Options.
    Memory Usage: 16.3 MB, less than 69.79% of Python3 online submissions for Count All Valid Pickup and Delivery Options.
    """

    def countOrders(self, n: int) -> int:
        res = 1
        mod = 10**9 + 7

        for i in range(2, n + 1):
            res = res * (i * 2 - 1) * (i * 2) / 2 % mod

        return res
