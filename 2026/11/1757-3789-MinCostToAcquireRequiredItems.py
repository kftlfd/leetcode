"""
Leetcode
2026-11-11
3789. Minimum Cost to Acquire Required Items
Medium

You are given five integers cost1, cost2, costBoth, need1, and need2.

There are three types of items available:

    An item of type 1 costs cost1 and contributes 1 unit to the type 1 requirement only.
    An item of type 2 costs cost2 and contributes 1 unit to the type 2 requirement only.
    An item of type 3 costs costBoth and contributes 1 unit to both type 1 and type 2 requirements.

You must collect enough items so that the total contribution toward type 1 is at least need1 and the total contribution toward type 2 is at least need2.

Return an integer representing the minimum possible total cost to achieve these requirements.

 

Example 1:

Input: cost1 = 3, cost2 = 2, costBoth = 1, need1 = 3, need2 = 2

Output: 3

Explanation:

After buying three type 3 items, which cost 3 * 1 = 3, the total contribution to type 1 is 3 (>= need1 = 3) and to type 2 is 3 (>= need2 = 2).
Any other valid combination would cost more, so the minimum total cost is 3.

Example 2:

Input: cost1 = 5, cost2 = 4, costBoth = 15, need1 = 2, need2 = 3

Output: 22

Explanation:

We buy need1 = 2 items of type 1 and need2 = 3 items of type 2: 2 * 5 + 3 * 4 = 10 + 12 = 22.
Any other valid combination would cost more, so the minimum total cost is 22.

Example 3:

Input: cost1 = 5, cost2 = 4, costBoth = 15, need1 = 0, need2 = 0

Output: 0

Explanation:

Since no items are required (need1 = need2 = 0), we buy nothing and pay 0.

 

Constraints:

    1 <= cost1, cost2, costBoth <= 10^6
    0 <= need1, need2 <= 10^9


"""


class Solution01:
    """
    Runtime 0ms Beats 100.00%
    Memory 19.22MB Beats 71.58%
    """

    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        total = 0

        if costBoth <= cost1 + cost2:
            needBoth = min(need1, need2)
            total += costBoth * needBoth
            need1 -= needBoth
            need2 -= needBoth

        if costBoth <= cost1 and costBoth <= cost2:
            return total + costBoth * max(need1, need2)

        if costBoth <= cost1:
            # costBoth > cost2
            return total + costBoth * need1 + cost2 * max(0, need2 - need1)

        if costBoth <= cost2:
            # costBoth > cost1
            return total + costBoth * need2 + cost1 * max(0, need1 - need2)

        return total + cost1 * need1 + cost2 * need2


class Solution02:
    """
    Runtime 1ms Beats 35.79%
    Memory 19.17MB Beats 88.42%
    """

    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        total = 0

        if costBoth <= cost1 + cost2:
            needBoth = min(need1, need2)
            total += costBoth * needBoth
            need1 -= needBoth
            need2 -= needBoth

        total += min(cost1, costBoth) * need1
        total += min(cost2, costBoth) * need2

        return total


class Solution1:
    """
    leetcode solution: Greedy
    Runtime 0ms Beats 100.00%
    Memory 19.29MB Beats 71.58%
    """

    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # Buying separately is cheaper; item 3 is unnecessary
        if cost1 + cost2 <= costBoth:
            totalCost = cost1 * need1 + cost2 * need2
        else:
            # Buy item 3 first until one requirement is fulfilled
            cnt_3 = min(need1, need2)
            totalCost = cnt_3 * costBoth

            need1 -= cnt_3
            need2 -= cnt_3

            # Type 1 is still needed; choose the cheaper of items 1 and 3
            if need1 > 0:
                totalCost += need1 * min(cost1, costBoth)

            # Type 2 is still needed; choose the cheaper of items 2 and 3
            elif need2 > 0:
                totalCost += need2 * min(cost2, costBoth)

        return totalCost
