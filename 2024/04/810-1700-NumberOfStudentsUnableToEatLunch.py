"""
Leetcode
1700. Number of Students Unable to Eat Lunch
Easy
2024-04-08

The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

    If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
    Otherwise, they will leave it and go to the queue's end.

This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the ith sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the jth student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.

 

Example 1:

Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
Output: 0 
Explanation:
- Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
- Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
- Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
- Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
- Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
Hence all students are able to eat.

Example 2:

Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
Output: 3

 

Constraints:

    1 <= students.length, sandwiches.length <= 100
    students.length == sandwiches.length
    sandwiches[i] is 0 or 1.
    students[i] is 0 or 1.
"""

from collections import deque
from typing import List


class Solution:
    """
    Runtime: 42 ms, faster than 45.25% of Python3 online submissions for Number of Students Unable to Eat Lunch.
    Memory Usage: 16.6 MB, less than 59.90% of Python3 online submissions for Number of Students Unable to Eat Lunch.
    """

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        total = len(students)
        ones = sum(students)
        zeroes = total - ones
        ate = 0

        for sw in sandwiches:
            if sw == 1 and ones > 0:
                ones -= 1
                ate += 1
            elif sw == 0 and zeroes > 0:
                zeroes -= 1
                ate += 1
            else:
                break

        return total - ate


class Solution1:
    """
    leetcode solution 1: Simulation Using Queue and Stack
    Runtime: 43 ms, faster than 35.74% of Python3 online submissions for Number of Students Unable to Eat Lunch.
    Memory Usage: 16.5 MB, less than 95.17% of Python3 online submissions for Number of Students Unable to Eat Lunch.
    """

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        # Add students and sandwiches to the queue and stack
        student_queue = deque(students)
        sandwich_stack = sandwiches[::-1]

        # Simulate the lunch process by serving sandwiches
        # or sending students to the back of the queue.
        last_served = 0
        while len(student_queue) > 0 and last_served < len(student_queue):
            if sandwich_stack[-1] == student_queue[0]:
                sandwich_stack.pop()  # Serve sandwich
                student_queue.popleft()  # Student leaves queue
                last_served = 0
            else:
                # Student moves to back of queue
                student_queue.append(student_queue.popleft())
                last_served += 1

        # Remaining students in queue are unserved students
        return len(student_queue)
