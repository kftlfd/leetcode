"""
Leetcode
2025-12-26
2483. Minimum Penalty for a Shop
Medium

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

    1 <= customers.length <= 10^5
    customers consists only of characters 'Y' and 'N'.


Hint 1
At any index, the penalty is the sum of prefix count of "N" and suffix count of "Y".
Hint 2
Enumerate all indices and find the minimum such value.
"""


class Solution:
    """
    Runtime 55ms Beats 71.93%
    Memory 18.05MB Beats 77.33%
    """

    def bestClosingTime(self, customers: str) -> int:
        y_right = customers.count("Y")
        n_left = 0
        n = len(customers)
        min_penalty = n * 2
        min_penalty_time = -1

        for i in range(n + 1):
            cur_penalty = n_left + y_right
            if cur_penalty < min_penalty:
                min_penalty = cur_penalty
                min_penalty_time = i
            if i == n:
                break
            if customers[i] == "Y":
                y_right -= 1
            else:
                n_left += 1

        return min_penalty_time


class Solution1:
    """
    leetcode solution 1: Two Passes
    Runtime 72ms Beats 60.45%
    Memory 18.04MB Beats 77.33%
    """

    def bestClosingTime(self, customers: str) -> int:
        curPenalty = sum(c == "Y" for c in customers)

        # Start with closing at hour 0, the penalty equals all 'Y' in closed hours.
        minPenalty = curPenalty
        earliestHour = 0

        for i, ch in enumerate(customers):
            # If status in hour i is 'Y', moving it to open hours decrement
            # penalty by 1. Otherwise, moving 'N' to open hours increment
            # penalty by 1.
            if ch == "Y":
                curPenalty -= 1
            else:
                curPenalty += 1

            # Update earliestHour if a smaller penalty is encountered.
            if curPenalty < minPenalty:
                earliestHour = i + 1
                minPenalty = curPenalty

        return earliestHour


class Solution2:
    """
    leetcode solution 2: One Pass
    Runtime 49ms Beats 75.76%
    Memory 18.12MB Beats 66.34%
    """

    def bestClosingTime(self, customers: str) -> int:
        # Start with closing at hour 0 and assume the current penalty is 0.
        minPenalty = 0
        curPenalty = 0
        earliestHour = 0

        for i in range(len(customers)):
            ch = customers[i]

            # If status in hour i is 'Y', moving it to open hours decrement
            # penalty by 1. Otherwise, moving 'N' to open hours increment
            # penatly by 1.
            if ch == "Y":
                curPenalty -= 1
            else:
                curPenalty += 1

            # Update earliestHour if a smaller penatly is encountered.
            if curPenalty < minPenalty:
                earliestHour = i + 1
                minPenalty = curPenalty

        return earliestHour


class Solution3:
    """
    sample 38ms solution
    Runtime 42ms Beats 95.78%
    Memory 17.92MB Beats 92.15%
    """

    def bestClosingTime(self, customers: str) -> int:
        score = 0
        max_score = 0
        time = -1

        for j, cur in enumerate(customers):
            score += 1 if cur == 'Y' else -1
            if score > max_score:
                max_score = score
                time = j

        return time + 1
