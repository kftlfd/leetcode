"""
Leetcode
2024. Maximize the Confusion of an Exam (medium)
2023-07-07

A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).

You are given a string answerKey, where answerKey[i] is the original answer to the ith question. In addition, you are given an integer k, the maximum number of times you may perform the following operation:

    Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').

Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.

Example 1:

Input: answerKey = "TTFF", k = 2
Output: 4
Explanation: We can replace both the 'F's with 'T's to make answerKey = "TTTT".
There are four consecutive 'T's.

Example 2:

Input: answerKey = "TFFT", k = 1
Output: 3
Explanation: We can replace the first 'T' with an 'F' to make answerKey = "FFFT".
Alternatively, we can replace the second 'T' with an 'F' to make answerKey = "TFFF".
In both cases, there are three consecutive 'F's.

Example 3:

Input: answerKey = "TTFTTFTT", k = 1
Output: 5
Explanation: We can replace the first 'F' to make answerKey = "TTTTTFTT"
Alternatively, we can replace the second 'F' to make answerKey = "TTFTTTTT". 
In both cases, there are five consecutive 'T's.

Constraints:

    n == answerKey.length
    1 <= n <= 5 * 10^4
    answerKey[i] is either 'T' or 'F'
    1 <= k <= n
"""

from collections import defaultdict, Counter


class Solution:
    """
    Sliding windows
    Runtime: 621 ms, faster than 12.80% of Python3 online submissions for Maximize the Confusion of an Exam.
    Memory Usage: 16.7 MB, less than 55.49% of Python3 online submissions for Maximize the Confusion of an Exam.
    """

    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans = 0

        # cosecutive 'T's
        left = 0
        count = defaultdict(int)
        for right, c in enumerate(answerKey):
            count[c] += 1
            while left < right and count['F'] > k:
                count[answerKey[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)

        # cosecutive 'F's
        left = 0
        count = defaultdict(int)
        for right, c in enumerate(answerKey):
            count[c] += 1
            while left < right and count['T'] > k:
                count[answerKey[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans


class Solution1:
    """
    leetcode solution 1: Binary search + fixed sliding window
    Time: O(n * log(n))
    Space: O(1)
    Runtime: 1962 ms, faster than 5.18% of Python3 online submissions for Maximize the Confusion of an Exam.
    Memory Usage: 16.8 MB, less than 55.49% of Python3 online submissions for Maximize the Confusion of an Exam.
    """

    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        left = k
        right = n

        def isValid(size):
            counter = Counter(answerKey[:size])
            if min(counter['T'], counter['F']) <= k:
                return True
            for i in range(size, n):
                counter[answerKey[i]] += 1
                counter[answerKey[i - size]] -= 1
                if min(counter['T'], counter['F']) <= k:
                    return True
            return False

        while left < right:
            mid = (left + right + 1) // 2
            if isValid(mid):
                left = mid
            else:
                right = mid - 1

        return left


class Solution2:
    """
    leetcode solution 2: Sliding window
    Time: O(n)
    Space: O(1)
    Runtime: 429 ms, faster than 62.19% of Python3 online submissions for Maximize the Confusion of an Exam.
    Memory Usage: 16.6 MB, less than 99.09% of Python3 online submissions for Maximize the Confusion of an Exam.
    """

    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_size = k
        count = Counter(answerKey[:k])
        left = 0
        for right in range(k, len(answerKey)):
            count[answerKey[right]] += 1
            while min(count['T'], count['F']) > k:
                count[answerKey[left]] -= 1
                left += 1
            max_size = max(max_size, right - left + 1)
        return max_size


class Solution3:
    """
    leetcode solution : Advanced sliding window
    Time: O(n)
    Space: O(1)
    Runtime: 373 ms, faster than 76.83% of Python3 online submissions for Maximize the Confusion of an Exam.
    Memory Usage: 16.7 MB, less than 85.98% of Python3 online submissions for Maximize the Confusion of an Exam.
    """

    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_size = 0
        count = Counter()
        for right in range(len(answerKey)):
            count[answerKey[right]] += 1
            minor = min(count['T'], count['F'])
            if minor <= k:
                max_size += 1
            else:
                count[answerKey[right - max_size]] -= 1
        return max_size


s = Solution()
tests = [
    (("TTFF", 2),
     4),

    (("TFFT", 1),
     3),

    (("TTFTTFTT", 1),
     5),
]
for inp, exp in tests:
    res = s.maxConsecutiveAnswers(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
