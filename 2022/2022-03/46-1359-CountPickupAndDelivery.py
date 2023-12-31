'''
Leetcode
1359. Count All Valid Pickup and Delivery Options (Hard)
2022-03-06

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

https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/
'''

import functools



# Leetcode solutions
# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/solution/



# Approach 1: Recursion with Memoization (Top-Down DP)
# Runtime: 1323 ms, faster than 11.36% of Python3 online submissions for Count All Valid Pickup and Delivery Options.
# Memory Usage: 194.8 MB, less than 8.52% of Python3 online submissions for Count All Valid Pickup and Delivery Options.
class Solution1:
    def countOrders(self, n: int) -> int:
        @functools.cache
        def totalWays(unpicked, undelivered):
            if not unpicked and not undelivered:
                # We have completed all orders.
                return 1

            if (unpicked < 0 or undelivered < 0 or undelivered < unpicked):
                # We can't pick or deliver more than N items
                # Number of deliveries can't exceed number of pickups 
                # as we can only deliver after a pickup.
                return 0

            # Count all choices of picking up an order.
            ans = unpicked * totalWays(unpicked - 1, undelivered)
            ans %= MOD

            # Count all choices of delivering a picked order.
            ans += (undelivered - unpicked) * totalWays(unpicked, undelivered - 1)
            ans %= MOD

            return ans
        
        MOD = 1_000_000_007
        return totalWays(n, n)



# Approach 2: Tabulation (Bottom-Up DP)
# Runtime: 740 ms, faster than 21.02% of Python3 online submissions for Count All Valid Pickup and Delivery Options.
# Memory Usage: 19.8 MB, less than 20.45% of Python3 online submissions for Count All Valid Pickup and Delivery Options.
class Solution2:
    def countOrders(self, n: int) -> int:
        MOD = 1_000_000_007
        dp = [[0] * (n + 1) for i in range(n + 1)]
        
        for unpicked in range(n + 1):
            for undelivered in range(unpicked, n + 1):
                # If all orders are picked and delivered then,
                # for remaining '0' orders we have only one way.
                if not unpicked and not undelivered:
                    dp[unpicked][undelivered] = 1
                    continue
                
                # There are some unpicked elements left. 
                # We have choice to pick any one of those orders.
                if unpicked > 0:
                    dp[unpicked][undelivered] += unpicked * dp[unpicked - 1][undelivered]
                dp[unpicked][undelivered] %= MOD
                
                # Number of deliveries done is less than picked orders.
                # We have choice to deliver any one of (undelivered - unpicked) orders. 
                if undelivered > unpicked:
                    dp[unpicked][undelivered] += (undelivered - unpicked) * dp[unpicked][undelivered - 1]
                dp[unpicked][undelivered] %= MOD
        
        return dp[n][n]



# Approach 3: Permutations (Math)
# Runtime: 41 ms, faster than 73.30% of Python3 online submissions for Count All Valid Pickup and Delivery Options.
# Memory Usage: 13.8 MB, less than 88.07% of Python3 online submissions for Count All Valid Pickup and Delivery Options.
class Solution3:
    def countOrders(self, n: int) -> int:
        MOD = 1_000_000_007
        ans = 1

        for i in range(1, n + 1):
            # Ways to arrange all pickups, 1*2*3*4*5*...*n
            ans = ans * i
            # Ways to arrange all deliveries, 1*3*5*...*(2n-1)
            ans = ans * (2 * i - 1)
            ans %= MOD
        
        return ans



# Approach 4: Probability (Math)
# Runtime: 66 ms, faster than 31.82% of Python3 online submissions for Count All Valid Pickup and Delivery Options.
# Memory Usage: 13.8 MB, less than 88.07% of Python3 online submissions for Count All Valid Pickup and Delivery Options.
class Solution4:
    def countOrders(self, n: int) -> int:
        MOD = 1_000_000_007
        ans = 1

        for i in range(1, 2 * n + 1):
            ans = ans * i
            
            # We only need to divide the result by 2 n-times.
            # To prevent decimal results we divide after multiplying an even number.
            if not i % 2:
                ans = ans // 2
            ans %= MOD
        
        return ans
