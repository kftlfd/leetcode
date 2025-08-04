"""
Leetcode
2025-08-04
904. Fruit Into Baskets\
Medium

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

 

Constraints:

    1 <= fruits.length <= 10^5
    0 <= fruits[i] < fruits.length


"""

from typing import Counter, List


class Solution00:
    """
    Time Limit Exceeded
    """

    def totalFruit(self, fruits: List[int]) -> int:
        basket = Counter()
        ans = 0

        left = 0
        for right, fruit in enumerate(fruits):
            basket[fruit] += 1
            while sum(c > 0 for c in basket.values()) > 2:
                basket[fruits[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans


class Solution01:
    """
    Runtime 713ms Beats 5.03%
    Memory 23.61MB Beats 42.94%
    """

    def totalFruit(self, fruits: List[int]) -> int:
        basket = Counter()
        ans = 0

        left = 0
        for right, fruit in enumerate(fruits):
            basket[fruit] += 1
            while sum(c > 0 for c in basket.values()) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] < 1:
                    del basket[fruits[left]]
                left += 1
            ans = max(ans, right - left + 1)

        return ans


class Solution02:
    """
    Runtime 163ms Beats 81.57%
    Memory 23.56MB Beats 77.01%
    """

    def totalFruit(self, fruits: List[int]) -> int:
        a, a_c = -1, 0
        b, b_c = -1, 0
        ans = 0

        left = 0
        for fruit in fruits:
            if a not in [fruit, -1] and b not in [fruit, -1]:
                while a_c and b_c:
                    left_f = fruits[left]
                    if left_f == a:
                        a_c -= 1
                    else:
                        b_c -= 1
                    left += 1
                if a_c < 1:
                    a = -1
                else:
                    b = -1

            if a in [fruit, -1]:
                a = fruit
                a_c += 1
            else:
                b = fruit
                b_c += 1

            ans = max(ans, a_c + b_c)

        return ans


class Solution03:
    """
    Runtime 271ms Beats 7.30%
    Memory 23.62MB Beats 42.94%
    """

    def totalFruit(self, fruits: List[int]) -> int:
        basket = Counter()
        basket_len = 0
        ans = 0

        left = 0
        for right, fruit in enumerate(fruits):
            if basket[fruit] == 0:
                basket_len += 1
            basket[fruit] += 1

            while basket_len > 2:
                left_f = fruits[left]
                if basket[left_f] == 1:
                    basket_len -= 1
                basket[left_f] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
