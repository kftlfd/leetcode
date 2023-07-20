"""
Leetcode
735. Asteroid Collision (medium)
2023-07-20

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

Constraints:

    2 <= asteroids.length <= 10^4
    -1000 <= asteroids[i] <= 1000
    asteroids[i] != 0
"""

from typing import List


class Solution:
    """
    Runtime: 104 ms, faster than 87.94% of Python3 online submissions for Asteroid Collision.
    Memory Usage: 17.5 MB, less than 84.31% of Python3 online submissions for Asteroid Collision.
    """

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        i = 0

        while i < len(asteroids):
            cur = asteroids[i]

            # moves to right
            if cur > 0:
                ans.append(cur)
                i += 1
                continue

            # moves to left
            while True:
                if not ans or ans[-1] < 0:
                    ans.append(cur)
                    break

                if -cur == ans[-1]:
                    ans.pop()
                    break

                if -cur < ans[-1]:
                    break

                if -cur > ans[-1]:
                    ans.pop()

            i += 1

        return ans


class Solution1:
    """
    Runtime: 109 ms, faster than 71.15% of Python3 online submissions for Asteroid Collision.
    Memory Usage: 17.4 MB, less than 84.31% of Python3 online submissions for Asteroid Collision.
    """

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []

        for cur in asteroids:
            # moves to right
            if cur > 0:
                ans.append(cur)
                continue

            # moves to left
            while True:
                if not ans or ans[-1] < 0:
                    ans.append(cur)
                    break

                if -cur == ans[-1]:
                    ans.pop()
                    break

                if -cur < ans[-1]:
                    break

                if -cur > ans[-1]:
                    ans.pop()

        return ans


s = Solution1()
tests = [
    ([5, 10, -5],
     [5, 10]),

    ([8, -8],
     []),

    ([10, 2, -5],
     [10]),

    ([1, 2],
     [1, 2]),

    ([-1, -2],
     [-1, -2]),
]
for inp, exp in tests:
    res = s.asteroidCollision(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
