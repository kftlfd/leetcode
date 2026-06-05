"""
Leetcode
2026-06-05
3753. Total Waviness of Numbers in Range II
Hard

You are given two integers num1 and num2 representing an inclusive range [num1, num2].

The waviness of a number is defined as the total count of its peaks and valleys:

    A digit is a peak if it is strictly greater than both of its immediate neighbors.
    A digit is a valley if it is strictly less than both of its immediate neighbors.
    The first and last digits of a number cannot be peaks or valleys.
    Any number with fewer than 3 digits has a waviness of 0.

Return the total sum of waviness for all numbers in the range [num1, num2].

 

Example 1:

Input: num1 = 120, num2 = 130

Output: 3

Explanation:

In the range [120, 130]:

    120: middle digit 2 is a peak, waviness = 1.
    121: middle digit 2 is a peak, waviness = 1.
    130: middle digit 3 is a peak, waviness = 1.
    All other numbers in the range have a waviness of 0.

Thus, total waviness is 1 + 1 + 1 = 3.

Example 2:

Input: num1 = 198, num2 = 202

Output: 3

Explanation:

In the range [198, 202]:

    198: middle digit 9 is a peak, waviness = 1.
    201: middle digit 0 is a valley, waviness = 1.
    202: middle digit 0 is a valley, waviness = 1.
    All other numbers in the range have a waviness of 0.

Thus, total waviness is 1 + 1 + 1 = 3.

Example 3:

Input: num1 = 4848, num2 = 4848

Output: 2

Explanation:

Number 4848: the second digit 8 is a peak, and the third digit 4 is a valley, giving a waviness of 2.

 

Constraints:

    1 <= num1 <= num2 <= 10^15


Hint 1
Use digit dynamic programming
Hint 2
Build a digit-DP state (position, tight, lastDigit, secondLastDigit)
"""


class Solution1:
    """
    leetcode solution 1: Digit Dynamic Programming
    Runtime 809ms Beats 22.50%
    Memory 56.46MB Beats 65.00%
    """

    def totalWaviness(self, num1: int, num2: int) -> int:
        #  calculate the sum of fluctuation values of all numbers in the range [0, num]
        def solve(num: int) -> int:
            # if the fluctuation value of numbers less than 3 is 0
            if num < 100:
                return 0
            s = str(num)
            n = len(s)

            # memoized search uses two independent arrays
            # memo_cnt[pos][x][y]: the number of valid filling schemes where the current digit is at position pos, and the previous two digits are x and y
            # memo_cnt = [[[-1] * 10 for _ in range(10)] for _ in range(16)]

            # memo_sum[pos][x][y]: the fluctuation value when the current position is pos, and the two left digits are x and y
            # memo_sum = [[[-1] * 10 for _ in range(10)] for _ in range(16)]

            from functools import lru_cache

            @lru_cache(None)
            def dfs(
                pos: int, prev: int, curr: int, isLimit: bool, isLeading: bool
            ):
                # end position
                if pos == n:
                    return 1, 0

                # calculate the number of filling schemes and fluctuation value under current conditions
                cnt = 0
                waviness = 0
                up = int(s[pos]) if isLimit else 9
                for digit in range(up + 1):
                    newLeading = isLeading and (digit == 0)
                    # the previous number is updated to curr
                    newPrev = curr
                    # the current number is updated to digit
                    newCurr = -1 if newLeading else digit
                    subCnt, subSum = dfs(
                        pos + 1,
                        newPrev,
                        newCurr,
                        isLimit and (digit == up),
                        newLeading,
                    )
                    # only calculate the fluctuation value when there are no leading zeros
                    if not newLeading and prev >= 0 and curr >= 0:
                        # when the digit is a peak or a valley, update the current fluctuation value
                        if (prev < curr and curr > digit) or (
                            prev > curr and curr < digit
                        ):
                            waviness += subCnt

                    cnt += subCnt
                    waviness += subSum

                return cnt, waviness

            _, totalSum = dfs(0, -1, -1, True, True)
            return totalSum

        return solve(num2) - solve(num1 - 1)


class Solution2:
    """
    leetcode solution 2: Bottom-Up Dynamic Programming
    Runtime 774ms Beats 45.00%
    Memory 19.52MB Beats 87.50%
    """

    def totalWaviness(self, num1: int, num2: int) -> int:
        return self.solve(num2) - self.solve(num1 - 1)

    def solve(self, num: int) -> int:
        # if the number has fewer than 3 digits, the fluctuation value is 0
        if num < 100:
            return 0
        s = str(num)
        n = len(s)

        # digit 10 represents the invalid state when there is a leading zero
        curr_states = [
            (10, 10, 1, 1, 1, 0)
        ]  # (prev, curr, tight, lead, cnt, sum)

        for pos in range(n):
            limit = int(s[pos])
            cnt = [
                [[[0] * 11 for _ in range(11)] for _ in range(2)]
                for _ in range(2)
            ]
            sum_arr = [
                [[[0] * 11 for _ in range(11)] for _ in range(2)]
                for _ in range(2)
            ]

            for prev, curr, tight, lead, c, s_val in curr_states:
                max_digit = limit if tight else 9
                for digit in range(max_digit + 1):
                    new_lead = 1 if (lead and digit == 0) else 0
                    new_prev = curr
                    new_curr = 10 if new_lead else digit
                    new_tight = 1 if (tight and digit == max_digit) else 0

                    add = 0
                    # calculate fluctuation only when there are three significant digits (both prev and curr are valid and not leading zeros)
                    if not new_lead and prev != 10 and curr != 10:
                        if (prev < curr and curr > digit) or (
                            prev > curr and curr < digit
                        ):
                            add = c

                    cnt[new_tight][new_lead][new_prev][new_curr] += c
                    sum_arr[new_tight][new_lead][new_prev][new_curr] += (
                        s_val + add
                    )

            # collect legal states
            next_states = []
            for tight in range(2):
                for lead in range(2):
                    for prev in range(11):
                        for cur in range(11):
                            c = cnt[tight][lead][prev][cur]
                            if c != 0:
                                next_states.append(
                                    (
                                        prev,
                                        cur,
                                        tight,
                                        lead,
                                        c,
                                        sum_arr[tight][lead][prev][cur],
                                    )
                                )
            curr_states = next_states

        # sum of fluctuation values of all valid states
        ans = 0
        for _, _, _, _, _, s_val in curr_states:
            ans += s_val
        return ans
