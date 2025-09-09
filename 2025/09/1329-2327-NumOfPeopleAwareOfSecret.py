"""
Leetcode
2025-09-09
2327. Number of People Aware of a Secret
Medium

On day 1, one person discovers a secret.

You are given an integer delay, which means that each person will share the secret with a new person every day, starting from delay days after discovering the secret. You are also given an integer forget, which means that each person will forget the secret forget days after discovering it. A person cannot share the secret on the same day they forgot it, or on any day afterwards.

Given an integer n, return the number of people who know the secret at the end of day n. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: n = 6, delay = 2, forget = 4
Output: 5
Explanation:
Day 1: Suppose the first person is named A. (1 person)
Day 2: A is the only person who knows the secret. (1 person)
Day 3: A shares the secret with a new person, B. (2 people)
Day 4: A shares the secret with a new person, C. (3 people)
Day 5: A forgets the secret, and B shares the secret with a new person, D. (3 people)
Day 6: B shares the secret with E, and C shares the secret with F. (5 people)

Example 2:

Input: n = 4, delay = 1, forget = 3
Output: 6
Explanation:
Day 1: The first person is named A. (1 person)
Day 2: A shares the secret with B. (2 people)
Day 3: A and B share the secret with 2 new people, C and D. (4 people)
Day 4: A forgets the secret. B, C, and D share the secret with 3 new people. (6 people)

 

Constraints:

    2 <= n <= 1000
    1 <= delay < forget <= n


Hint 1
Let dp[i][j] be the number of people who have known the secret for exactly j + 1 days, at day i.
Hint 2
If j > 0, dp[i][j] = dp[i - 1][j - 1].
"""

from collections import deque
from functools import cache


class Solution01:
    """
    Runtime 102ms Beats 32.12%
    Memory 17.90MB Beats 71.53%
    """

    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        # on day 1 first person discovers the secret and is moved to delay_q
        delay_q = deque([0] * delay)
        delay_q[-1] = 1
        share_q = deque([0] * (forget - delay))
        ans = 1

        for _ in range(n - 1):  # start from day 2
            new_share = delay_q.popleft()  # waited delay, now start sharing

            share_q.popleft()  # forget at cur day
            share_q.append(new_share)  # start sharing after delay

            new_know = sum(share_q)  # all who share tell one new person
            delay_q.append(new_know)  # start waiting the delay

            ans = new_know + sum(delay_q)  # total know

        return ans % (10**9 + 7)


class Solution02:
    """
    Runtime 18ms Beats 36.50%
    Memory 18.24MB Beats 11.68%
    """

    class RingBuffer:
        def __init__(self, size: int):
            self._size = size
            self._arr = [0] * size
            self._start = 0
            self._end = size - 1
            self._sum = 0

        def __repr__(self):
            return str(self._arr)

        def popleft(self):
            val = self._arr[self._start]
            self._arr[self._start] = 0
            self._start += 1
            if self._start >= self._size:
                self._start = 0
            self._sum -= val
            return val

        def append(self, val: int):
            self._end += 1
            if self._end >= self._size:
                self._end = 0
            self._arr[self._end] = val
            self._sum += val

        def get_sum(self):
            return self._sum

    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        # on day 1 first person discovers the secret and is moved to delay_q
        delay_q = self.RingBuffer(delay)
        delay_q.popleft()
        delay_q.append(1)
        share_q = self.RingBuffer(forget - delay)
        ans = 1

        for _ in range(n - 1):  # start from day 2
            new_share = delay_q.popleft()  # waited delay, now start sharing

            share_q.popleft()  # forget at cur day
            share_q.append(new_share)  # start sharing after delay

            new_know = share_q.get_sum()  # all who share tell one new person
            delay_q.append(new_know)  # start waiting the delay

            ans = new_know + delay_q.get_sum()  # total know

        return ans % (10**9 + 7)


class Solution1:
    """
    leetcode solution: Simulation + Deque
    Runtime 7ms Beats 51.09%
    Memory 17.92MB Beats 50.36%
    """

    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        know, share = deque([(1, 1)]), deque([])
        know_cnt, share_cnt = 1, 0
        for i in range(2, n + 1):
            if know and know[0][0] == i - delay:
                know_cnt -= know[0][1]
                share_cnt += know[0][1]
                share.append(know[0])
                know.popleft()
            if share and share[0][0] == i - forget:
                share_cnt -= share[0][1]
                share.popleft()
            if share:
                know_cnt += share_cnt
                know.append((i, share_cnt))
        return (know_cnt + share_cnt) % (10**9 + 7)


class Solution2:
    """
    https://leetcode.com/problems/number-of-people-aware-of-a-secret/editorial/comments/3157150/
    DP top-down
    Runtime 278ms Beats 21.17%
    Memory 19.04MB Beats 5.11%
    """

    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        @cache
        def count_persons(limit):
            count = int(forget >= limit)
            for d in range(delay, min(forget, limit)):
                count = (count + count_persons(limit - d)) % 1000000007
            return count
        return count_persons(n)


class Solution3:
    """
    https://leetcode.com/problems/number-of-people-aware-of-a-secret/editorial/comments/3157150/
    DP bottom-up
    Runtime 257ms Beats 21.90%
    Memory 17.86MB Beats 71.53%
    """

    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [int(forget >= limit) for limit in range(n + 1)]
        for limit in range(len(dp)):
            for d in range(delay, min(forget, limit)):
                dp[limit] = (dp[limit] + dp[limit - d]) % 1000000007
        return dp[-1]


class Solution4:
    """
    sample 3ms solution
    Runtime 1ms Beats 95.62%
    Memory 17.98MB Beats 50.36%
    """

    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7

        # new[i] = number of people who first learn the secret on day i
        new = [0] * (n + 1)
        new[1] = 1

        sharing = 0  # how many can share on the current day

        # Fill day 2..n
        for day in range(2, n + 1):
            # People starting to share today
            if day - delay >= 1:
                sharing = (sharing + new[day - delay]) % MOD
            # People who forget today (stop sharing)
            if day - forget >= 1:
                sharing = (sharing - new[day - forget]) % MOD

            # each sharer shares to exactly one new person
            new[day] = sharing % MOD

        # Sum those who still remember on day n (haven't reached forget window)
        start = max(1, n - forget + 1)
        ans = sum(new[start: n + 1]) % MOD
        return ans


class Solution5:
    """
    https://leetcode.com/problems/number-of-people-aware-of-a-secret/editorial/comments/3157113/
    Runtime 1ms Beats 95.62%
    Memory 17.88MB Beats 71.53%
    """

    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        knows = [0] * n
        knows[0] = 1
        shared, total = 0, 1

        for day in range(delay, forget):
            shared += knows[day - delay]
            total += shared
            knows[day] = shared

        for day in range(forget, n):
            shared += knows[day - delay] - knows[day - forget]
            total += shared - knows[day - forget]
            knows[day] = shared

        return total % 1_000_000_007
