"""
Leetcode
712. Minimum ASCII Delete Sum for Two Strings (medium)
2023-07-31

Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:

Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

Example 2:

Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d] + 101[e] + 101[e] to the sum.
Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.

Constraints:

    1 <= s1.length, s2.length <= 1000
    s1 and s2 consist of lowercase English letters.
"""


class Solution:
    """
    leetcode solution 1: recursion
    Time: O(3^k * k) -- k = max(len(s1), len(s2))
    Space: O(k)
    TLE
    """

    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        # return minimum cost to make s1[0..i] and s2[0..j] equal
        def compute_cost(i, j):

            # if s1 is empty, then we need to delete all characters of s2
            if i < 0:
                delete_cost = 0
                for pointer in range(j + 1):
                    delete_cost += ord(s2[pointer])
                return delete_cost

            # if s2 is empty, delete all of s1
            if j < 0:
                delete_cost = 0
                for pointer in range(i + 1):
                    delete_cost += ord(s1[pointer])
                return delete_cost

            # check s1[i] and s2[j]
            if s1[i] == s2[j]:
                return compute_cost(i - 1, j - 1)

            return min(
                ord(s1[i]) + compute_cost(i - 1, j),
                ord(s2[j]) + compute_cost(i, j - 1),
                ord(s1[i]) + ord(s2[j]) + compute_cost(i - 1, j - 1)
            )

        return compute_cost(len(s1) - 1, len(s2) - 1)


class Solution1:
    """
    leetcode solution 2: top-down DP
    Time: O(m * n)
    Space: O(m * n)
    Runtime: 1037 ms, faster than 32.96% of Python3 online submissions for Minimum ASCII Delete Sum for Two Strings.
    Memory Usage: 221.6 MB, less than 8.52% of Python3 online submissions for Minimum ASCII Delete Sum for Two Strings.
    """

    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        dp = {}

        # return minimum cost to make s1[0..i] and s2[0..j] equal
        def compute_cost(i, j):

            if i < 0 and j < 0:
                return 0

            if (i, j) in dp:
                return dp[(i, j)]

            elif i < 0:
                dp[(i, j)] = ord(s2[j]) + compute_cost(i, j - 1)

            elif j < 0:
                dp[(i, j)] = ord(s1[i]) + compute_cost(i - 1, j)

            elif s1[i] == s2[j]:
                dp[(i, j)] = compute_cost(i - 1, j - 1)

            else:
                dp[(i, j)] = min(
                    ord(s1[i]) + compute_cost(i - 1, j),
                    ord(s2[j]) + compute_cost(i, j - 1),
                )

            return dp[(i, j)]

        return compute_cost(len(s1) - 1, len(s2) - 1)


class Solution2:
    """
    leetcode solution 3: bottom-up DP
    Time: O(m * n)
    Space: O(min(m, n))
    Runtime: 436 ms, faster than 95.80% of Python3 online submissions for Minimum ASCII Delete Sum for Two Strings.
    Memory Usage: 16.3 MB, less than 98.86% of Python3 online submissions for Minimum ASCII Delete Sum for Two Strings.
    """

    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        # Make sure s2 is smaller string
        if len(s1) < len(s2):
            return self.minimumDeleteSum(s1=s2, s2=s1)

        # Case for empty s1
        m, n = len(s1), len(s2)
        curr_row = [0] * (n + 1)
        for j in range(1, n + 1):
            curr_row[j] = curr_row[j - 1] + ord(s2[j - 1])

        # Compute answer row-by-row
        for i in range(1, m + 1):

            diag = curr_row[0]
            curr_row[0] += ord(s1[i - 1])

            for j in range(1, n + 1):

                # If characters are the same, the answer is top-left-diagonal value
                if s1[i - 1] == s2[j - 1]:
                    answer = diag

                # Otherwise, the answer is minimum of top and left values with
                # deleted character's ASCII value
                else:
                    answer = min(
                        ord(s1[i - 1]) + curr_row[j],
                        ord(s2[j - 1]) + curr_row[j - 1]
                    )

                # Before overwriting curr_row[j] with the answer, save it in diag
                # for the next column
                diag = curr_row[j]
                curr_row[j] = answer

        # Return answer
        return curr_row[-1]


s = Solution2()
tests = [
    (("sea", "eat"),
     231),

    (("delete", "leet"),
     403),
]
for inp, exp in tests:
    res = s.minimumDeleteSum(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
