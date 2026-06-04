"""
Leetcode
2026-06-04
3751. Total Waviness of Numbers in Range I
Medium

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

    1 <= num1 <= num2 <= 10^5


"""

from functools import lru_cache


class Solution:
    """
    Runtime 627ms Beats 5.75%
    Memory 19.34MB Beats 32.95%
    """

    def totalWaviness(self, num1: int, num2: int) -> int:

        def get_wv(num: int) -> int:
            if num < 101:
                return 0
            d = list(map(int, str(num)))
            return sum(
                d[i-1] < d[i] > d[i+1]
                or d[i-1] > d[i] < d[i+1]
                for i in range(1, len(d) - 1)
            )

        return sum(map(get_wv, range(num1, num2 + 1)))


class Solution1:
    """
    leetcode solution 1: Enumeration
    Runtime 497ms Beats 8.43%
    Memory 19.37MB Beats 32.95%
    """

    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(n: int) -> int:
            s = str(n)
            return sum(
                (a < b > c) or (a > b < c) for a, b, c in zip(s, s[1:], s[2:])
            )

        return sum(waviness(n) for n in range(num1, num2 + 1))


class Solution2:
    """
    leetcode solution 2: Digit Dynamic Programming
    Runtime 380ms Beats 28.35%
    Memory 39.55MB Beats 5.36%
    """

    def totalWaviness(self, num1: int, num2: int) -> int:
        #  calculate the sum of the volatility values of all numbers in the range [0, num]
        def solve(num: int) -> int:
            # if the number is less than 3, the fluctuation value is 0
            if num < 100:
                return 0
            s = str(num)
            n = len(s)

            # memoized search uses two independent arrays
            # memo_cnt[pos][x][y]: the number of valid filling schemes where the current position is pos, and the previous two positions are x, y
            # memo_cnt = [[[-1] * 10 for _ in range(10)] for _ in range(16)]

            # memo_sum[pos][x][y]: the fluctuation value when the current position is pos and the two left digits are x and y
            # memo_sum = [[[-1] * 10 for _ in range(10)] for _ in range(16)]

            @lru_cache(None)
            def dfs(
                pos: int, prev: int, curr: int, isLimit: bool, isLeading: bool
            ):
                # end position
                if pos == n:
                    return 1, 0

                # calculate the number of filling schemes and the fluctuation value under current conditions
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
                    # only calculate the volatility value when there are no leading zeros
                    if not newLeading and prev >= 0 and curr >= 0:
                        # when the value is a peak or a trough, update the current fluctuation value
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


class Solution3:
    """
    sample 134ms solution
    Runtime 252ms Beats 78.54%
    Memory 19.37MB Beats 32.95%
    """

    def totalWaviness(self, num1: int, num2: int) -> int:
        count = 0
        for i in range(num1, num2 + 1):
            while i / 100 >= 1:
                digit_back = i % 10
                digit_front = i % 1000 // 100
                digit_middle = i % 100 // 10
                if (digit_front > digit_middle and digit_middle < digit_back) or (digit_front < digit_middle and digit_middle > digit_back):
                    count += 1
                i //= 10
        return count
