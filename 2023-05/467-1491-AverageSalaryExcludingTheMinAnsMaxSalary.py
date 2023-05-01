"""
Leetcode
1491. Average Salary Excluding the Minimum and Maximum Salary (easy)
2023-05-01

You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

Example 1:
Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500

Example 2:
Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000) / 1 = 2000
"""

from typing import List
from math import inf


class Solution1:
    """
    Runtime: 45 ms, faster than 5.49% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary.
    Memory Usage: 16.4 MB, less than 8.21% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary.
    """

    def average(self, salary: List[int]) -> float:
        min_salary = inf
        max_salary = 0
        total_sum = 0

        for num in salary:
            min_salary = min(min_salary, num)
            max_salary = max(max_salary, num)
            total_sum += num

        return (total_sum - min_salary - max_salary) / (len(salary) - 2)


class Solution2:
    """
    Runtime: 51 ms, faster than 5.49% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary.
    Memory Usage: 16.3 MB, less than 8.21% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary.
    """

    def average(self, salary: List[int]) -> float:
        return sum(sorted(salary)[1:-1]) / (len(salary) - 2)


s = Solution1()
tests = [
    ([4000, 3000, 1000, 2000],
     2500),

    ([1000, 2000, 3000],
     2000),
]
for inp, exp in tests:
    res = s.average(inp)
    if round(res) != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
