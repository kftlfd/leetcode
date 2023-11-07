"""
Leetcode
1921. Eliminate Maximum Number of Monsters (medium)
2023-11-07

You are playing a video game where you are defending your city from a group of n monsters. You are given a 0-indexed integer array dist of size n, where dist[i] is the initial distance in kilometers of the ith monster from the city.

The monsters walk toward the city at a constant speed. The speed of each monster is given to you in an integer array speed of size n, where speed[i] is the speed of the ith monster in kilometers per minute.

You have a weapon that, once fully charged, can eliminate a single monster. However, the weapon takes one minute to charge. The weapon is fully charged at the very start.

You lose when any monster reaches your city. If a monster reaches the city at the exact moment the weapon is fully charged, it counts as a loss, and the game ends before you can use your weapon.

Return the maximum number of monsters that you can eliminate before you lose, or n if you can eliminate all the monsters before they reach the city.

 

Example 1:

Input: dist = [1,3,4], speed = [1,1,1]
Output: 3
Explanation:
In the beginning, the distances of the monsters are [1,3,4]. You eliminate the first monster.
After a minute, the distances of the monsters are [X,2,3]. You eliminate the second monster.
After a minute, the distances of the monsters are [X,X,2]. You eliminate the thrid monster.
All 3 monsters can be eliminated.

Example 2:

Input: dist = [1,1,2,3], speed = [1,1,1,1]
Output: 1
Explanation:
In the beginning, the distances of the monsters are [1,1,2,3]. You eliminate the first monster.
After a minute, the distances of the monsters are [X,0,1,2], so you lose.
You can only eliminate 1 monster.

Example 3:

Input: dist = [3,2,4], speed = [5,3,2]
Output: 1
Explanation:
In the beginning, the distances of the monsters are [3,2,4]. You eliminate the first monster.
After a minute, the distances of the monsters are [X,0,2], so you lose.
You can only eliminate 1 monster.

 

Constraints:

    n == dist.length == speed.length
    1 <= n <= 10^5
    1 <= dist[i], speed[i] <= 10^5
"""

from typing import List
import heapq


class Solution:
    """
    Runtime: 716 ms, faster than 34.62% of Python3 online submissions for Eliminate Maximum Number of Monsters.
    Memory Usage: 32.3 MB, less than 31.27% of Python3 online submissions for Eliminate Maximum Number of Monsters.
    """

    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = sorted([S / v for S, v in zip(dist, speed)])

        count = 0

        for i, t in enumerate(time):
            if i < t:
                count += 1
            else:
                break

        return count


class Solution1:
    """
    leetcode solution 2: heap
    Runtime: 757 ms, faster than 15.50% of Python3 online submissions for Eliminate Maximum Number of Monsters.
    Memory Usage: 32.3 MB, less than 44.96% of Python3 online submissions for Eliminate Maximum Number of Monsters.
    """

    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        heap = []
        for i in range(len(dist)):
            heap.append(dist[i] / speed[i])

        heapq.heapify(heap)
        ans = 0
        while heap:
            if heapq.heappop(heap) <= ans:
                break

            ans += 1

        return ans


s = Solution()
tests = [
    (([1, 3, 4], [1, 1, 1]),
     3),

    (([1, 1, 2, 3], [1, 1, 1, 1]),
     1),

    (([3, 2, 4], [5, 3, 2]),
     1),
]
for inp, exp in tests:
    res = s.eliminateMaximum(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
