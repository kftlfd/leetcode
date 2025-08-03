"""
Leetcode
2025-08-03
2106. Maximum Fruits Harvested After at Most K Steps
Hard

Fruits are available at some positions on an infinite x-axis. You are given a 2D integer array fruits where fruits[i] = [positioni, amounti] depicts amounti fruits at the position positioni. fruits is already sorted by positioni in ascending order, and each positioni is unique.

You are also given an integer startPos and an integer k. Initially, you are at the position startPos. From any position, you can either walk to the left or right. It takes one step to move one unit on the x-axis, and you can walk at most k steps in total. For every position you reach, you harvest all the fruits at that position, and the fruits will disappear from that position.

Return the maximum total number of fruits you can harvest.

 

Example 1:

Input: fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4
Output: 9
Explanation: 
The optimal way is to:
- Move right to position 6 and harvest 3 fruits
- Move right to position 8 and harvest 6 fruits
You moved 3 steps and harvested 3 + 6 = 9 fruits in total.

Example 2:

Input: fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos = 5, k = 4
Output: 14
Explanation: 
You can move at most k = 4 steps, so you cannot reach position 0 nor 10.
The optimal way is to:
- Harvest the 7 fruits at the starting position 5
- Move left to position 4 and harvest 1 fruit
- Move right to position 6 and harvest 2 fruits
- Move right to position 7 and harvest 4 fruits
You moved 1 + 3 = 4 steps and harvested 7 + 1 + 2 + 4 = 14 fruits in total.

Example 3:

Input: fruits = [[0,3],[6,4],[8,5]], startPos = 3, k = 2
Output: 0
Explanation:
You can move at most k = 2 steps and cannot reach any position with fruits.

 

Constraints:

    1 <= fruits.length <= 10^5
    fruits[i].length == 2
    0 <= startPos, positioni <= 2 * 10^5
    positioni-1 < positioni for any i > 0 (0-indexed)
    1 <= amounti <= 10^4
    0 <= k <= 2 * 10^5


Hint 1
Does an optimal path have very few patterns? For example, could a path that goes left, turns and goes right, then turns again and goes left be any better than a path that simply goes left, turns, and goes right?
Hint 2
The optimal path turns at most once. That is, the optimal path is one of these: to go left only; to go right only; to go left, turn and go right; or to go right, turn and go left.
Hint 3
Moving x steps left then k-x steps right gives you a range of positions that you can reach.
Hint 4
Use prefix sums to get the sum of all fruits for each possible range.
Hint 5
Use a similar strategy for all the paths that go right, then turn and go left.
"""

from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    """
    Runtime 38ms Beats 99.17%
    Memory 52.25MB Beats 95.00%
    """

    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)

        w_sum = 0  # window sum
        min_left = max(startPos - k, 0)
        left_i = bisect_left(fruits, min_left, key=lambda x: x[0])

        i = left_i
        while i < n and fruits[i][0] <= startPos:
            w_sum += fruits[i][1]
            i += 1

        ans = w_sum

        for right_i in range(i, n):
            pos, count = fruits[right_i]
            if pos > startPos + k:
                break

            w_sum += count

            min_left = startPos - max(
                (k - (pos - startPos)) // 2,  # go left, then right
                k - (pos - startPos) * 2,  # go right, then left
            )

            while fruits[left_i][0] < min_left:
                w_sum -= fruits[left_i][1]
                left_i += 1

            ans = max(ans, w_sum)

        return ans


class Solution1:
    """
    leetcode solution 1: Binary Search
    Runtime 766ms Beats 25.83%
    Memory 52.42MB Beats 50.83%
    """

    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        sum_ = [0] * (n + 1)
        indices = [0] * n

        for i in range(n):
            sum_[i + 1] = sum_[i] + fruits[i][1]
            indices[i] = fruits[i][0]

        ans = 0
        for x in range(k // 2 + 1):
            # move left x steps, then right (k - 2x) steps
            y = k - 2 * x
            left = startPos - x
            right = startPos + y
            start = bisect_left(indices, left)
            end = bisect_right(indices, right)
            ans = max(ans, sum_[end] - sum_[start])

            # move right x steps, then left (k - 2x) steps
            y = k - 2 * x
            left = startPos - y
            right = startPos + x
            start = bisect_left(indices, left)
            end = bisect_right(indices, right)
            ans = max(ans, sum_[end] - sum_[start])

        return ans


class Solution2:
    """
    leetcode solution 2: Sliding Window
    Runtime 213ms Beats 45.00%
    Memory 52.44MB Beats 50.83%
    """

    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        left = 0
        right = 0
        n = len(fruits)
        w_sum = 0
        ans = 0

        def step(left: int, right: int) -> int:
            if fruits[right][0] <= startPos:
                return startPos - fruits[left][0]
            elif fruits[left][0] >= startPos:
                return fruits[right][0] - startPos
            else:
                return (
                    min(
                        abs(startPos - fruits[right][0]),
                        abs(startPos - fruits[left][0]),
                    )
                    + fruits[right][0]
                    - fruits[left][0]
                )

        # each time fix the right boundary of the window
        while right < n:
            w_sum += fruits[right][1]
            # move left boundary
            while left <= right and step(left, right) > k:
                w_sum -= fruits[left][1]
                left += 1

            ans = max(ans, w_sum)
            right += 1

        return ans
