"""
Leetcode
2483. Minimum Penalty for a Shop (medium)
2023-08-29

You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':

    if the ith character is 'Y', it means that customers come at the ith hour
    whereas 'N' indicates that no customers come at the ith hour.

If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:

    For every hour when the shop is open and no customers come, the penalty increases by 1.
    For every hour when the shop is closed and customers come, the penalty increases by 1.

Return the earliest hour at which the shop must be closed to incur a minimum penalty.

Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.

Example 1:

Input: customers = "YYNY"
Output: 2
Explanation: 
- Closing the shop at the 0th hour incurs in 1+1+0+1 = 3 penalty.
- Closing the shop at the 1st hour incurs in 0+1+0+1 = 2 penalty.
- Closing the shop at the 2nd hour incurs in 0+0+0+1 = 1 penalty.
- Closing the shop at the 3rd hour incurs in 0+0+1+1 = 2 penalty.
- Closing the shop at the 4th hour incurs in 0+0+1+0 = 1 penalty.
Closing the shop at 2nd or 4th hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.

Example 2:

Input: customers = "NNNNN"
Output: 0
Explanation: It is best to close the shop at the 0th hour as no customers arrive.

Example 3:

Input: customers = "YYYY"
Output: 4
Explanation: It is best to close the shop at the 4th hour as customers arrive at each hour.

Constraints:

    1 <= customers.length <= 105
    customers consists only of characters 'Y' and 'N'.
"""


class Solution:
    """
    Runtime: 270 ms, faster than 21.39% of Python3 online submissions for Minimum Penalty for a Shop.
    Memory Usage: 25.2 MB, less than 9.64% of Python3 online submissions for Minimum Penalty for a Shop.
    """

    def bestClosingTime(self, customers: str) -> int:
        n_penalty = [0] * (len(customers) + 1)
        y_penalty = [0] * (len(customers) + 1)

        for i in range(1, len(n_penalty)):
            n_penalty[i] = n_penalty[i-1] + (1 if customers[i-1] == 'N' else 0)

        for j in range(len(y_penalty)-2, -1, -1):
            y_penalty[j] = y_penalty[j+1] + (1 if customers[j] == 'Y' else 0)

        min_penalty = float('inf')
        min_index = 0
        for i, (pn, py) in enumerate(zip(n_penalty, y_penalty)):
            cur = pn + py
            if cur < min_penalty:
                min_penalty = cur
                min_index = i

        return min_index


class Solution1:
    """
    leetcode solution 1: two passes
    Runtime: 99 ms, faster than 93.67% of Python3 online submissions for Minimum Penalty for a Shop.
    Memory Usage: 17.3 MB, less than 73.49% of Python3 online submissions for Minimum Penalty for a Shop.
    """

    def bestClosingTime(self, customers: str) -> int:
        # Start with closing at hour 0, the penalty equals all 'Y' in closed hours.
        cur_penalty = min_penalty = customers.count('Y')
        earliest_hour = 0

        for i, ch in enumerate(customers):
            # If status in hour i is 'Y', moving it to open hours decrement
            # penalty by 1. Otherwise, moving 'N' to open hours increment
            # penatly by 1.
            if ch == 'Y':
                cur_penalty -= 1
            else:
                cur_penalty += 1

            # Update earliest_hour if a smaller penatly is encountered
            if cur_penalty < min_penalty:
                earliest_hour = i + 1
                min_penalty = cur_penalty

        return earliest_hour


class Solution2:
    """
    leetcode solution 2: one pass
    Runtime: 96 ms, faster than 95.48% of Python3 online submissions for Minimum Penalty for a Shop.
    Memory Usage: 17.4 MB, less than 73.49% of Python3 online submissions for Minimum Penalty for a Shop.
    """

    def bestClosingTime(self, customers: str) -> int:
        # Start with closing at hour 0 and assume the current penalty is 0.
        cur_penalty = min_penalty = 0
        earliest_hour = 0

        for i, ch in enumerate(customers):
            # If status in hour i is 'Y', moving it to open hours decrement
            # penalty by 1. Otherwise, moving 'N' to open hours increment
            # penatly by 1.
            if ch == 'Y':
                cur_penalty -= 1
            else:
                cur_penalty += 1

            # Update earliest_hour if a smaller penatly is encountered
            if cur_penalty < min_penalty:
                earliest_hour = i + 1
                min_penalty = cur_penalty

        return earliest_hour


s = Solution()
tests = [
    ('YYNY',
     2),

    ('NNNN',
     0),

    ('YYYY',
     4),
]
for inp, exp in tests:
    res = s.bestClosingTime(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
