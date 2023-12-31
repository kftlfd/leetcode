'''
Leetcode
1672. Richest Customer Wealth (easy)
2022-01-31
'''

# You are given an m x n integer grid accounts where accounts[i][j] 
# is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. 
# Return the wealth that the richest customer has.

# A customer's wealth is the amount of money they have in all their bank 
# accounts. The richest customer is the customer that has the maximum wealth.

from typing import List



# Try 1
# pythonic one-liner
# Runtime: 130 ms, faster than 5.10% of Python3 online submissions for Richest Customer Wealth.
# Memory Usage: 13.8 MB, less than 99.25% of Python3 online submissions for Richest Customer Wealth.
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max( [sum(customer) for customer in accounts] )

        # alternative using map:
        # https://leetcode.com/problems/richest-customer-wealth/solution/1244045
        # return max(map(sum, accounts))



# Try 2
# Runtime: 48 ms, faster than 95.35% of Python3 online submissions for Richest Customer Wealth.
# Memory Usage: 14 MB, less than 96.85% of Python3 online submissions for Richest Customer Wealth.
class Solution2:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        maxw = 0
        
        for customer in accounts:
            cw = sum(customer)
            maxw = max(maxw, cw)
        
        return maxw