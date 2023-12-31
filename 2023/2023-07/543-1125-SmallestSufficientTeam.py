"""
Leetcode
1125. Smallest Sufficient Team (hard)
2023-07-16

In a project, you have a list of required skills req_skills, and a list of people. The ith person people[i] contains a list of skills that the person has.

Consider a sufficient team: a set of people such that for every required skill in req_skills, there is at least one person in the team who has that skill. We can represent these teams by the index of each person.

    For example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].

Return any sufficient team of the smallest possible size, represented by the index of each person. You may return the answer in any order.

It is guaranteed an answer exists.

Example 1:

Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
Output: [0,2]

Example 2:

Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
Output: [1,2]

Constraints:

    1 <= req_skills.length <= 16
    1 <= req_skills[i].length <= 16
    req_skills[i] consists of lowercase English letters.
    All the strings of req_skills are unique.
    1 <= people.length <= 60
    0 <= people[i].length <= 16
    1 <= people[i][j].length <= 16
    people[i][j] consists of lowercase English letters.
    All the strings of people[i] are unique.
    Every skill in people[i] is a skill in req_skills.
    It is guaranteed a sufficient team exists.
"""

from typing import List


class Solution:
    """
    leetcode solution 1: Bottom-Up Dynamic Programming with Bitmasks
    Time: O(2^m * n)
    Space: O(2^m)
    Runtime: 1472 ms, faster than 15.19% of Python3 online submissions for Smallest Sufficient Team.
    Memory Usage: 18.9 MB, less than 60.13% of Python3 online submissions for Smallest Sufficient Team.
    """

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(people)
        m = len(req_skills)

        skill_id = dict()
        for i, skill in enumerate(req_skills):
            skill_id[skill] = i
        skills_mask_of_person = [0] * n

        for i in range(n):
            for skill in people[i]:
                skills_mask_of_person[i] |= 1 << skill_id[skill]

        dp = [(1 << n) - 1] * (1 << m)
        dp[0] = 0

        for skills_mask in range(1, 1 << m):
            for i in range(n):
                smaller_skills_mask = skills_mask & ~skills_mask_of_person[i]
                if smaller_skills_mask != skills_mask:
                    people_mask = dp[smaller_skills_mask] | (1 << i)
                    if people_mask.bit_count() < dp[skills_mask].bit_count():
                        dp[skills_mask] = people_mask

        answer_mask = dp[(1 << m) - 1]
        ans = []
        for i in range(n):
            if (answer_mask >> i) & 1:
                ans.append(i)
        return ans


class Solution1:
    """
    leetcode solution 2: Top-Down Dynamic Programming (Memoization)
    Time: O(2^m * n)
    Space: O(2^m)
    Runtime: 641 ms, faster than 34.18% of Python3 online submissions for Smallest Sufficient Team.
    Memory Usage: 19.1 MB, less than 56.33% of Python3 online submissions for Smallest Sufficient Team.
    """

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(people)
        m = len(req_skills)

        skill_id = dict()
        for i, skill in enumerate(req_skills):
            skill_id[skill] = i

        skills_mask_of_person = [0] * n
        for i in range(n):
            for skill in people[i]:
                skills_mask_of_person[i] |= 1 << skill_id[skill]

        dp = [-1] * (1 << m)
        dp[0] = 0

        def f(skills_mask):
            if dp[skills_mask] != -1:
                return dp[skills_mask]
            for i in range(n):
                new_skills_mask = skills_mask & ~skills_mask_of_person[i]
                if new_skills_mask != skills_mask:
                    people_mask = f(new_skills_mask) | (1 << i)
                    if (dp[skills_mask] == -1 or
                        people_mask.bit_count()
                       < dp[skills_mask].bit_count()):
                        dp[skills_mask] = people_mask
            return dp[skills_mask]

        answer_mask = f((1 << m) - 1)
        ans = []
        for i in range(n):
            if (answer_mask >> i) & 1:
                ans.append(i)
        return ans


s = Solution()
tests = [
    ((
        ["java", "nodejs", "reactjs"],
        [
            ["java"],
            ["nodejs"],
            ["nodejs", "reactjs"]
        ]
    ),
        [0, 2]),

    ((
        ["algorithms", "math", "java", "reactjs", "csharp", "aws"],
        [
            ["algorithms", "math", "java"],
            ["algorithms", "math", "reactjs"],
            ["java", "csharp", "aws"],
            ["reactjs", "csharp"],
            ["csharp", "math"],
            ["aws", "java"]
        ]
    ),
        [1, 2])
]
for inp, exp in tests:
    res = s.smallestSufficientTeam(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
