"""
Leetcode
846. Hand of Straights
Medium
2024-06-06

Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

 

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

Example 2:

Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.

 

Constraints:

    1 <= hand.length <= 104
    0 <= hand[i] <= 109
    1 <= groupSize <= hand.length

 

Note: This question is the same as 1296: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
"""

from collections import Counter
import heapq
from typing import List


class Solution:
    """
    Time Limit Exceeded
    """

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True
        if len(hand) % groupSize != 0:
            return False

        hand = sorted(hand)
        sets = [[hand[0]]]
        set_start = 0

        for n in hand[1:]:
            cur_set = set_start
            while True:
                if len(sets) == cur_set:
                    sets.append([n])
                    break
                if len(sets[cur_set]) < groupSize and sets[cur_set][-1] == n - 1:
                    sets[cur_set].append(n)
                    if len(sets[cur_set]) == groupSize:
                        set_start += cur_set == set_start
                    break
                cur_set += 1

        return all(len(num_set) >= groupSize and len(num_set) % groupSize == 0 for num_set in sets)


class Solution1:
    """
    leetcode solution 1: Using Map
    Runtime: 163 ms, faster than 56.75% of Python3 online submissions for Hand of Straights.
    Memory Usage: 18.4 MB, less than 63.87% of Python3 online submissions for Hand of Straights.
    """

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True

        hand_size = len(hand)

        if hand_size % groupSize != 0:
            return False

        # Counter to store the count of each card value
        card_count = Counter(hand)

        # Min-heap to process the cards in sorted order
        min_heap = list(card_count.keys())
        heapq.heapify(min_heap)

        # Process the cards until the heap is empty
        while min_heap:
            current_card = min_heap[0]  # Get the smallest card value
            # Check each consecutive sequence of groupSize cards
            for i in range(groupSize):
                if card_count[current_card + i] == 0:
                    return False
                card_count[current_card + i] -= 1
                if card_count[current_card + i] == 0:
                    if current_card + i != heapq.heappop(min_heap):
                        return False

        return True


class Solution2:
    """
    leetcode solution 2: Rerverse Decrement
    Runtime: 158 ms, faster than 74.68% of Python3 online submissions for Hand of Straights.
    Memory Usage: 18.5 MB, less than 50.76% of Python3 online submissions for Hand of Straights.
    """

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True

        if len(hand) % groupSize != 0:
            return False

        # Counter to store the count of each card value
        card_count = Counter(hand)

        for card in hand:
            start_card = card
            # Find the start of the potential straight sequence
            while card_count[start_card - 1]:
                start_card -= 1

            # Process the sequence starting from start_card
            while start_card <= card:
                while card_count[start_card]:
                    # Check if we can form a consecutive sequence
                    # of groupSize cards
                    for next_card in range(start_card, start_card + groupSize):
                        if not card_count[next_card]:
                            return False
                        card_count[next_card] -= 1
                start_card += 1

        return True


s = Solution()
tests = [
    (([1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 6, 7], 3),
     False),

    (([1, 2, 3, 6, 2, 3, 4, 7, 8], 3),
     True),

    (([1, 2, 3, 4, 5], 4),
     False),

]
for inp, exp in tests:
    res = s.isNStraightHand(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
