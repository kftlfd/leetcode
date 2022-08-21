"""
Leetcode
936. Stamping The Sequence (hard)
2022-08-22

You are given two strings stamp and target. Initially, there is a string s of length target.length with all s[i] == '?'.

In one turn, you can place stamp over s and replace every letter in the s with the corresponding letter from stamp.

    For example, if stamp = "abc" and target = "abcba", then s is "?????" initially. In one turn you can:
        place stamp at index 0 of s to obtain "abc??",
        place stamp at index 1 of s to obtain "?abc?", or
        place stamp at index 2 of s to obtain "??abc".
    Note that stamp must be fully contained in the boundaries of s in order to stamp (i.e., you cannot place stamp at index 3 of s).

We want to convert s to target using at most 10 * target.length turns.

Return an array of the index of the left-most letter being stamped at each turn. If we cannot obtain target from s within 10 * target.length turns, return an empty array.

Example 1:
Input: stamp = "abc", target = "ababc"
Output: [0,2]
Explanation: Initially s = "?????".
- Place stamp at index 0 to get "abc??".
- Place stamp at index 2 to get "ababc".
[1,0,2] would also be accepted as an answer, as well as some other answers.

Example 2:
Input: stamp = "abca", target = "aabcaca"
Output: [3,0,1]
Explanation: Initially s = "???????".
- Place stamp at index 3 to get "???abca".
- Place stamp at index 0 to get "abcabca".
- Place stamp at index 1 to get "aabcaca".
"""

from typing import List
import collections


# leetcode solution
# https://leetcode.com/problems/stamping-the-sequence/solution/
# Runtime: 182 ms, faster than 80.60% of Python3 online submissions for Stamping The Sequence.
# Memory Usage: 18.1 MB, less than 14.93% of Python3 online submissions for Stamping The Sequence.
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        M, N = len(stamp), len(target)

        queue = collections.deque()
        done = [False] * N
        ans = []
        A = []
        for i in range(N - M + 1):
            # For each window [i, i+M),
            # A[i] will contain info on what needs to change
            # before we can reverse stamp at i.

            made, todo = set(), set()
            for j, c in enumerate(stamp):
                a = target[i+j]
                if a == c:
                    made.add(i+j)
                else:
                    todo.add(i+j)
            A.append((made, todo))

            # If we can reverse stamp at i immediately,
            # enqueue letters from this window.
            if not todo:
                ans.append(i)
                for j in range(i, i + len(stamp)):
                    if not done[j]:
                        queue.append(j)
                        done[j] = True

        # For each enqueued letter,
        while queue:
            i = queue.popleft()

            # For each window that is potentially affected,
            # j: start of window
            for j in range(max(0, i-M+1), min(N-M, i)+1):
                if i in A[j][1]:  # This window is affected
                    # Remove it from todo list of this window
                    A[j][1].discard(i)
                    if not A[j][1]:  # Todo list of this window is empty
                        ans.append(j)
                        for m in A[j][0]:  # For each letter to potentially enqueue,
                            if not done[m]:
                                queue.append(m)
                                done[m] = True

        return ans[::-1] if all(done) else []


s = Solution()
tests = [
    ("abc", "ababc"),
    ("abca", "aabcaca"),
]
for stamp, target in tests:
    print(stamp, target)
    print(s.movesToStamp(stamp, target))
    print()
