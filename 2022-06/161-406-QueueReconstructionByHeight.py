"""
Leetcode
406. Queue Reconstruction by Height (medium)
2022-06-29

You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order). Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people in front who have a height greater than or equal to hi.

Reconstruct and return the queue that is represented by the input array people. The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] is the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).

Example 1:
Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

Example 2:
Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]


Hints
1. What can you say about the position of the shortest person? If the position of the shortest person is i, how many people would be in front of the shortest person?
2. Once you fix the position of the shortest person, what can you say about the position of the second shortest person?
"""

from typing import List


# Runtime: 647 ms, faster than 14.61% of Python3 online submissions for Queue Reconstruction by Height.
# Memory Usage: 14.5 MB, less than 64.95% of Python3 online submissions for Queue Reconstruction by Height.
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        ans = [None] * n
        sorted_people = sorted(
            sorted(people, key=lambda x: x[1], reverse=True), key=lambda x: x[0])

        for p in sorted_people:
            i = p[1]

            for j in range(n):
                if ans[j] == None:
                    if i == 0:
                        ans[j] = p
                        break
                    else:
                        i -= 1

        return ans


# Runtime: 610 ms, faster than 15.57% of Python3 online submissions for Queue Reconstruction by Height.
# Memory Usage: 14.4 MB, less than 93.98% of Python3 online submissions for Queue Reconstruction by Height.
class Solution2:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        ans = [None] * n
        sorted_people = sorted(
            sorted(people, key=lambda x: x[1], reverse=True), key=lambda x: x[0])

        for p in sorted_people:
            none_indexes = [i for i, n in enumerate(ans) if n == None]
            ans[none_indexes[p[1]]] = p

        return ans


# https://leetcode.com/problems/queue-reconstruction-by-height/discuss/89359/Explanation-of-the-neat-Sort+Insert-solution
# https://leetcode.com/problems/queue-reconstruction-by-height/discuss/167308/Python-solution
# Runtime: 90 ms, faster than 99.52% of Python3 online submissions for Queue Reconstruction by Height.
# Memory Usage: 14.5 MB, less than 31.23% of Python3 online submissions for Queue Reconstruction by Height.
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        queue = []
        for p in people:
            queue.insert(p[1], p)
        return queue


s = Solution2()
tests = [
    [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]],
    [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]],
]
for t in tests:
    print(t)
    print(s.reconstructQueue(t))
    print()
