"""
Leetcode
904. Fruit Into Baskets (medium)
2023-02-07

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

    You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
    Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
    Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Given the integer array fruits, return the maximum number of fruits you can pick.

Example 1:
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Example 2:
Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].

Example 3:
Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
"""

from typing import List, Optional
from collections import defaultdict


class Solution:
    """
    Time Limit Exceeded. 84 / 91 test cases passed.
    """

    def totalFruit(self, fruits: List[int]) -> int:

        max_fruits = 1

        types = defaultdict(int)
        types[fruits[0]] = 1

        left = 0
        right = 1

        while right < len(fruits):
            types[fruits[right]] += 1
            if len([t for t in types.values() if t > 0]) <= 2:
                max_fruits = max(max_fruits, right - left + 1)
            else:
                types[fruits[left]] -= 1
                left += 1
            right += 1

        return max_fruits


class Solution1:
    """
    leetcode solution
    Runtime: 1045 ms, faster than 49.43% of Python3 online submissions for Fruit Into Baskets.
    Memory Usage: 20.1 MB, less than 80.52% of Python3 online submissions for Fruit Into Baskets.
    """

    def totalFruit(self, fruits: List[int]) -> int:

        max_fruits = 0
        basket = {}
        left = 0

        for right in range(len(fruits)):
            basket[fruits[right]] = basket.get(fruits[right], 0) + 1

            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits


s = Solution1()
tests = [
    ([1, 2, 1],
     3),

    ([0, 1, 2, 2],
     3),

    ([1, 2, 3, 2, 2],
     4)
]
for inp, exp in tests:
    res = s.totalFruit(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
