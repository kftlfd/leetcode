"""
Leetcode
1823. Find the Winner of the Circular Game
Medium
2024-07-08

There are n friends that are playing a game. The friends are sitting in a circle and are numbered from 1 to n in clockwise order. More formally, moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i < n, and moving clockwise from the nth friend brings you to the 1st friend.

The rules of the game are as follows:

    Start at the 1st friend.
    Count the next k friends in the clockwise direction including the friend you started at. The counting wraps around the circle and may count some friends more than once.
    The last friend you counted leaves the circle and loses the game.
    If there is still more than one friend in the circle, go back to step 2 starting from the friend immediately clockwise of the friend who just lost and repeat.
    Else, the last friend in the circle wins the game.

Given the number of friends, n, and an integer k, return the winner of the game.

 

Example 1:

Input: n = 5, k = 2
Output: 3
Explanation: Here are the steps of the game:
1) Start at friend 1.
2) Count 2 friends clockwise, which are friends 1 and 2.
3) Friend 2 leaves the circle. Next start is friend 3.
4) Count 2 friends clockwise, which are friends 3 and 4.
5) Friend 4 leaves the circle. Next start is friend 5.
6) Count 2 friends clockwise, which are friends 5 and 1.
7) Friend 1 leaves the circle. Next start is friend 3.
8) Count 2 friends clockwise, which are friends 3 and 5.
9) Friend 5 leaves the circle. Only friend 3 is left, so they are the winner.

Example 2:

Input: n = 6, k = 5
Output: 1
Explanation: The friends leave in this order: 5, 4, 6, 2, 3. The winner is friend 1.

 

Constraints:

    1 <= k <= n <= 500

 

Follow up:

Could you solve this problem in linear time with constant space?
"""

from collections import deque


class Solution:
    """
    simple simulation
    Runtime: 217 ms, faster than 9.75% of Python3 online submissions for Find the Winner of the Circular Game.
    Memory Usage: 16.6 MB, less than 18.56% of Python3 online submissions for Find the Winner of the Circular Game.
    """

    def findTheWinner(self, n: int, k: int) -> int:
        q = deque(list(range(1, n + 1)))

        i = 1
        while len(q) > 1:
            player = q.popleft()
            if i < k:
                q.append(player)
                i += 1
            else:
                i = 1

        return q.popleft()


class Solution1:
    """
    sample 38 ms submission
    Runtime: 39 ms, faster than 60.58% of Python3 online submissions for Find the Winner of the Circular Game.
    Memory Usage: 16.6 MB, less than 49.47% of Python3 online submissions for Find the Winner of the Circular Game.
    """

    def findTheWinner(self, n: int, k: int) -> int:
        arr = list(range(1, n + 1))
        ptr = 0

        while len(arr) > 1:
            ptr = (ptr + k - 1) % len(arr)
            arr.pop(ptr)

        return arr[0]


class Solution2:
    """
    sample 29 ms submission
    Runtime: 32 ms, faster than 87.46% of Python3 online submissions for Find the Winner of the Circular Game.
    Memory Usage: 16.5 MB, less than 49.47% of Python3 online submissions for Find the Winner of the Circular Game.
    """

    def findTheWinner(self, n: int, k: int) -> int:
        def josephus(n):
            if n == 1:
                return 0
            return (josephus(n - 1) + k) % n

        return josephus(n) + 1


class Solution3:
    """
    leetcode solution 3: Recursion
    Runtime: 27 ms, faster than 97.02% of Python3 online submissions for Find the Winner of the Circular Game.
    Memory Usage: 16.4 MB, less than 84.30% of Python3 online submissions for Find the Winner of the Circular Game.
    """

    def findTheWinner(self, n: int, k: int) -> int:
        return self.winnerHelper(n, k) + 1

    def winnerHelper(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        return (self.winnerHelper(n - 1, k) + k) % n


class Solution4:
    """
    leetcode solution 4: Iterative
    Runtime: 37 ms, faster than 70.20% of Python3 online submissions for Find the Winner of the Circular Game.
    Memory Usage: 16.6 MB, less than 18.56% of Python3 online submissions for Find the Winner of the Circular Game.
    """

    def findTheWinner(self, n: int, k: int) -> int:
        ans = 0
        for i in range(2, n + 1):
            ans = (ans + k) % i
        # add 1 to convert back to 1 indexing
        return ans + 1
