'''
Leetcode
121. Best Time to Buy and Sell Stock (easy)
2022-02-01
'''

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a 
# different day in the future to sell that stock. (you must buy before you sell)

# Return the maximum profit you can achieve from this transaction. 
# If you cannot achieve any profit, return 0.

# DP? Kadane's algorithm?

from typing import List



# Try 1
# bruteforce O(n**2)
# Time Limit Exceeded
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []
        l = len(prices)
        for i in range(l):
            p = 0
            for j in range(i + 1, l):
                p = max(p, prices[j] - prices[i])
            profits.append(p)
        return max(profits)



# Try 2
# from:
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/1736054/All-Problems-of-Type-Best-Time-to-Buy-and-Sell-Stock-Solutions-or-Commented
# Runtime: 1730 ms, faster than 19.37% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 25.1 MB, less than 52.84% of Python3 online submissions for Best Time to Buy and Sell Stock.
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        mp = 0
        for i in range(len(prices)):
            mp = max(mp, prices[i] - buy) # sell now
            buy = min(buy, prices[i]) # buy now
            
            '''
            basically same as:

            if prices[i] < buy:
                buy = prices[i]

            profit = prices[i] - buy

            if profit > mp:
                mp = profit
            '''
        return mp



tests = [
    [7,1,5,3,6,4],
    [7,6,4,3,1],
    [4,7,3,8,2,1]
]

solution = Solution2()

for test in tests:
    print(f'test: {test}  -->  {solution.maxProfit(test)}')