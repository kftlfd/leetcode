"""
Leetcode
2251. Number of Flowers in Full Bloom (hard)
2023-10-11

You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi] means the ith flower will be in full bloom from starti to endi (inclusive). You are also given a 0-indexed integer array people of size n, where people[i] is the time that the ith person will arrive to see the flowers.

Return an integer array answer of size n, where answer[i] is the number of flowers that are in full bloom when the ith person arrives.

 

Example 1:

Input: flowers = [[1,6],[3,7],[9,12],[4,13]], poeple = [2,3,7,11]
Output: [1,2,2,2]
Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
For each person, we return the number of flowers in full bloom during their arrival.

Example 2:

Input: flowers = [[1,10],[3,3]], poeple = [3,3,2]
Output: [2,2,1]
Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
For each person, we return the number of flowers in full bloom during their arrival.

 

Constraints:

    1 <= flowers.length <= 5 * 10^4
    flowers[i].length == 2
    1 <= starti <= endi <= 10^9
    1 <= people.length <= 5 * 10^4
    1 <= people[i] <= 10^9

Hint: Notice that for any given time t, the number of flowers blooming at time t is equal to the number of flowers that have started blooming minus the number of flowers that have already stopped blooming.
"""

from typing import List
from bisect import bisect_right, bisect_left
import heapq
from sortedcontainers import SortedDict


class Solution:
    """
    Runtime: 904 ms, faster than 71.52% of Python3 online submissions for Number of Flowers in Full Bloom.
    Memory Usage: 44.7 MB, less than 50.61% of Python3 online submissions for Number of Flowers in Full Bloom.
    """

    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start_times = sorted(s for s, e in flowers)
        end_times = sorted(e for s, e in flowers)

        def get_flowers_num(time):
            started = bisect_right(start_times, time)
            ended = bisect_left(end_times, time)
            return started - ended

        return list(map(get_flowers_num, people))


class Solution1:
    """
    leetcode solution 1: Heap/Priority Queue
    Time: O(n * log(n) + m * (log(n) + log(m)))
    Space: O(n + m)
    Runtime: 881 ms, faster than 86.97% of Python3 online submissions for Number of Flowers in Full Bloom.
    Memory Usage: 44 MB, less than 69.39% of Python3 online submissions for Number of Flowers in Full Bloom.
    """

    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowers = sorted(flowers)
        sorted_people = sorted(people)
        dic = {}
        heap = []

        i = 0
        for person in sorted_people:
            while i < len(flowers) and flowers[i][0] <= person:
                heapq.heappush(heap, flowers[i][1])
                i += 1

            while heap and heap[0] < person:
                heapq.heappop(heap)

            dic[person] = len(heap)

        return [dic[x] for x in people]


class Solution2:
    """
    leetcode solution 2: Difference Array + Binary Search
    Time: O((n + m) * log(n))
    Space: O(n)
    Runtime: 1033 ms, faster than 33.03% of Python3 online submissions for Number of Flowers in Full Bloom.
    Memory Usage: 44 MB, less than 67.88% of Python3 online submissions for Number of Flowers in Full Bloom.
    """

    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        difference = SortedDict({0: 0})
        for start, end in flowers:
            difference[start] = difference.get(start, 0) + 1
            difference[end + 1] = difference.get(end + 1, 0) - 1

        positions = []
        prefix = []
        curr = 0
        for key, val in difference.items():
            positions.append(key)
            curr += val
            prefix.append(curr)

        ans = []
        for person in people:
            i = bisect_right(positions, person) - 1
            ans.append(prefix[i])

        return ans


class Solution3:
    """
    leetcode solution 3: Simpler Binary Search
    Time: O((n + m) * log(n))
    Space: O(n)
    Runtime: 881 ms, faster than 86.97% of Python3 online submissions for Number of Flowers in Full Bloom.
    Memory Usage: 45.1 MB, less than 26.06% of Python3 online submissions for Number of Flowers in Full Bloom.
    """

    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = []
        ends = []

        for start, end in flowers:
            starts.append(start)
            ends.append(end + 1)

        starts.sort()
        ends.sort()
        ans = []

        for person in people:
            i = bisect_right(starts, person)
            j = bisect_right(ends, person)
            ans.append(i - j)

        return ans


s = Solution()
tests = [
    (([[1, 6], [3, 7], [9, 12], [4, 13]], [2, 3, 7, 11]),
     [1, 2, 2, 2]),

    (([[1, 10], [3, 3]], [3, 3, 2]),
     [2, 2, 1]),
]
for inp, exp in tests:
    res = s.fullBloomFlowers(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
