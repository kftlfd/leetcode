"""
Leetcode
2300. Successful Pairs of Spells and Potions (medium)
2023-04-02

You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

Example 1:
Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]
Explanation:
- 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
- 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
Thus, [4,0,3] is returned.

Example 2:
Input: spells = [3,1,2], potions = [8,5,8], success = 16
Output: [2,0,2]
Explanation:
- 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
- 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful. 
- 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful. 
Thus, [2,0,2] is returned.
"""

from typing import List


class Solution:
    """
    brute force
    """

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        pairs = [0] * len(spells)

        for i, spell in enumerate(spells):
            for potion in potions:
                if spell * potion >= success:
                    pairs[i] += 1

        return pairs


class Solution1:
    """
    brute force. List comprehention
    Time Limit Exceeded
    """

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        return [sum(1 if spell * potion >= success else 0 for potion in potions)
                for spell in spells]


class Solution2:
    """
    sort + binary search
    Runtime: 2029 ms, faster than 27.48% of Python3 online submissions for Successful Pairs of Spells and Potions.
    Memory Usage: 37.6 MB, less than 23.23% of Python3 online submissions for Successful Pairs of Spells and Potions.
    """

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        pairs = [0] * len(spells)

        potions = sorted(potions)

        for i, spell in enumerate(spells):
            l = 0
            r = len(potions) - 1
            while l <= r:
                m = (l + r) // 2
                if spell * potions[m] >= success:
                    r = m - 1
                else:
                    l = m + 1
            pairs[i] = len(potions) - l

        return pairs


class Solution3:
    """
    leetcode solution 2: Sorting + Two Pointers
    Runtime: 1281 ms, faster than 81.59% of Python3 online submissions for Successful Pairs of Spells and Potions.
    Memory Usage: 43.7 MB, less than 5.95% of Python3 online submissions for Successful Pairs of Spells and Potions.
    """

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        spells = sorted([(spell, idx) for idx, spell in enumerate(spells)])
        potions = sorted(potions)
        pairs = [0] * len(spells)
        m = len(potions)
        potion_idx = m - 1

        for spell, idx in spells:
            while potion_idx >= 0 and (spell * potions[potion_idx]) >= success:
                potion_idx -= 1
            pairs[idx] = m - (potion_idx + 1)

        return pairs


s = Solution3()
tests = [
    (([5, 1, 3], [1, 2, 3, 4, 5], 7),
     [4, 0, 3]),

    (([3, 1, 2], [8, 5, 8], 16),
     [2, 0, 2]),
]
for inp, exp in tests:
    res = s.successfulPairs(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
