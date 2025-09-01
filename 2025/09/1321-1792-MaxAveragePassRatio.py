"""
Leetcode
2025-09-01
1792. Maximum Average Pass Ratio
Medium

There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes, where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.

You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.

The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.

Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:

Input: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
Output: 0.78333
Explanation: You can assign the two extra students to the first class. The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.

Example 2:

Input: classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
Output: 0.53485

 

Constraints:

    1 <= classes.length <= 10^5
    classes[i].length == 2
    1 <= passi <= totali <= 10^5
    1 <= extraStudents <= 10^5


Hint 1
Pay attention to how much the pass ratio changes when you add a student to the class. If you keep adding students, what happens to the change in pass ratio? The more students you add to a class, the smaller the change in pass ratio becomes.
Hint 2
Since the change in the pass ratio is always decreasing with the more students you add, then the very first student you add to each class is the one that makes the biggest change in the pass ratio.
Hint 3
Because each class's pass ratio is weighted equally, it's always optimal to put the student in the class that makes the biggest change among all the other classes.
Hint 4
Keep a max heap of the current class sizes and order them by the change in pass ratio. For each extra student, take the top of the heap, update the class size, and put it back in the heap.
"""

from heapq import heappop, heappush
import heapq
from typing import List


class Solution:
    """
    Runtime 1081ms Beats 84.35%
    Memory 55.12MB Beats 11.30%
    """

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        q = []

        for pas, total in classes:
            cur_ratio = pas / total
            nxt_ratio = (pas + 1) / (total + 1)
            heappush(q, (cur_ratio - nxt_ratio, total,
                     pas, nxt_ratio, cur_ratio))

        for _ in range(extraStudents):
            _, total, pas, nxt_ratio, _ = heappop(q)
            total += 1
            pas += 1
            cur_ratio = nxt_ratio
            nxt_ratio = (pas + 1) / (total + 1)
            heappush(q, (cur_ratio - nxt_ratio, total,
                     pas, nxt_ratio, cur_ratio))

        return sum(ratio for _, _, _, _, ratio in q) / len(q)


class Solution1:
    """
    leetcode solution
    Runtime 1117ms Beats 72.61%
    Memory 54.68MB Beats 97.39%
    """

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Lambda to calculate the gain of adding an extra student
        def _calculate_gain(passes, total_students):
            return (passes + 1) / (total_students + 1) - passes / total_students

        # Max heap to store (-gain, passes, total_students)
        max_heap = []
        for passes, total_students in classes:
            gain = _calculate_gain(passes, total_students)
            max_heap.append((-gain, passes, total_students))

        # Use heapify to transform the list into a valid heap in O(n)
        heapq.heapify(max_heap)

        # Distribute extra students
        for _ in range(extraStudents):
            _, passes, total_students = heapq.heappop(max_heap)
            heapq.heappush(
                max_heap,
                (
                    -_calculate_gain(passes + 1, total_students + 1),
                    passes + 1,
                    total_students + 1,
                ),
            )

        # Calculate the final average pass ratio
        total_pass_ratio = sum(
            passes / total_students for _, passes, total_students in max_heap
        )
        return total_pass_ratio / len(classes)
