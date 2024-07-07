"""
Leetcode
1518. Water Bottles
Easy
2024-07-07

There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water bottles from the market with one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.

 

Example 1:

Input: numBottles = 9, numExchange = 3
Output: 13
Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
Number of water bottles you can drink: 9 + 3 + 1 = 13.

Example 2:

Input: numBottles = 15, numExchange = 4
Output: 19
Explanation: You can exchange 4 empty bottles to get 1 full water bottle. 
Number of water bottles you can drink: 15 + 3 + 1 = 19.

 

Constraints:

    1 <= numBottles <= 100
    2 <= numExchange <= 100
"""


class Solution:
    """
    Runtime: 32 ms, faster than 71.11% of Python3 online submissions for Water Bottles.
    Memory Usage: 16.6 MB, less than 5.42% of Python3 online submissions for Water Bottles.
    """

    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink = numBottles
        empty = drink

        while empty >= numExchange:
            bottles, left = divmod(empty, numExchange)
            drink += bottles
            empty = bottles + left

        return drink


class Solution2:
    """
    leetcode solution 2: Optimized Simulation
    Runtime: 42 ms, faster than 9.31% of Python3 online submissions for Water Bottles.
    Memory Usage: 16.5 MB, less than 79.17% of Python3 online submissions for Water Bottles.
    """

    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        consumed_bottles = 0

        while numBottles >= numExchange:
            # Maximum number of times we can consume numExchange
            # number of bottles using numBottles.
            K = numBottles // numExchange

            consumed_bottles += numExchange * K
            numBottles -= numExchange * K

            numBottles += K

        return consumed_bottles + numBottles


class Solution3:
    """
    https://leetcode.com/problems/water-bottles/solution/2498134
    Runtime: 29 ms, faster than 84.86% of Python3 online submissions for Water Bottles.
    Memory Usage: 16.4 MB, less than 97.50% of Python3 online submissions for Water Bottles.
    """

    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles-1)//(numExchange-1)
