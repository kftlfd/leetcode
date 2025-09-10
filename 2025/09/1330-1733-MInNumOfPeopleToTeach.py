"""
Leetcode
2025-09-10
1733. Minimum Number of People to Teach
Medium

On a social network consisting of m users and some friendships between users, two users can communicate with each other if they know a common language.

You are given an integer n, an array languages, and an array friendships where:

    There are n languages numbered 1 through n,
    languages[i] is the set of languages the ith user knows, and
    friendships[i] = [ui, vi] denotes a friendship between the users ui and vi.

You can choose one language and teach it to some users so that all friends can communicate with each other. Return the minimum number of users you need to teach.
Note that friendships are not transitive, meaning if x is a friend of y and y is a friend of z, this doesn't guarantee that x is a friend of z.

 

Example 1:

Input: n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]
Output: 1
Explanation: You can either teach user 1 the second language or user 2 the first language.

Example 2:

Input: n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]
Output: 2
Explanation: Teach the third language to users 1 and 3, yielding two users to teach.

 

Constraints:

    2 <= n <= 500
    languages.length == m
    1 <= m <= 500
    1 <= languages[i].length <= n
    1 <= languages[i][j] <= n
    1 <= ui < vi <= languages.length
    1 <= friendships.length <= 500
    All tuples (ui, vi) are unique
    languages[i] contains only unique values


Hint 1
You can just use brute force and find out for each language the number of users you need to teach
Hint 2
Note that a user can appear in multiple friendships but you need to teach that user only once
"""

from collections import defaultdict
from typing import List


class Solution01:
    """
    Runtime 649ms Beats 6.10%
    Memory 27.58MB Beats 78.05%
    """

    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        need_to_learn = defaultdict(set)

        for a, b in friendships:
            can_communicate = False

            for lang in languages[a - 1]:
                if lang in languages[b - 1]:
                    can_communicate = True
                    break

            if can_communicate:
                continue

            for lang in range(1, n + 1):
                if lang not in languages[a - 1]:
                    need_to_learn[lang].add(a)
                if lang not in languages[b - 1]:
                    need_to_learn[lang].add(b)

        return min(len(users) for users in need_to_learn.values()) if need_to_learn else 0


class Solution02:
    """
    Runtime 74ms Beats 35.37%
    Memory 29.70MB Beats 76.83%
    """

    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        m = len(languages)  # number of users
        need_to_learn = [[0] * (m + 1) for _ in range(n + 1)]
        knows = [[False] * (n + 1) for _ in range(m + 1)]

        for user, langs in enumerate(languages, start=1):
            for lang in langs:
                knows[user][lang] = True

        for a, b in friendships:
            can_communicate = False

            for lang in languages[a - 1]:
                if knows[b][lang]:
                    can_communicate = True
                    break

            if can_communicate:
                continue

            for lang in range(1, n + 1):
                if not knows[a][lang]:
                    need_to_learn[lang][a] = 1
                if not knows[b][lang]:
                    need_to_learn[lang][b] = 1

        return min(sum(need_to_learn[lang][1:]) for lang in range(1, n + 1))


class Solution1:
    """
    leetcode solution: Greedy
    Runtime 41ms Beats 95.12%
    Memory 27.18MB Beats 92.68%
    """

    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        cncon = set()
        for friendship in friendships:
            mp = {}
            conm = False
            for lan in languages[friendship[0] - 1]:
                mp[lan] = 1
            for lan in languages[friendship[1] - 1]:
                if lan in mp:
                    conm = True
                    break
            if not conm:
                cncon.add(friendship[0] - 1)
                cncon.add(friendship[1] - 1)

        max_cnt = 0
        cnt = [0] * (n + 1)
        for friendship in cncon:
            for lan in languages[friendship]:
                cnt[lan] += 1
                max_cnt = max(max_cnt, cnt[lan])

        return len(cncon) - max_cnt
