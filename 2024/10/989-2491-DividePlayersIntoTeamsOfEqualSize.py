"""
Leetcode
2024-10-04
2491. Divide Players Into Teams of Equal Skill
Medium

You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.

The chemistry of a team is equal to the product of the skills of the players on that team.

Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams such that the total skill of each team is equal.

 

Example 1:

Input: skill = [3,2,5,1,3,4]
Output: 22
Explanation: 
Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.
The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.

Example 2:

Input: skill = [3,4]
Output: 12
Explanation: 
The two players form a team with a total skill of 7.
The chemistry of the team is 3 * 4 = 12.

Example 3:

Input: skill = [1,1,2,3]
Output: -1
Explanation: 
There is no way to divide the players into teams such that the total skill of each team is equal.

 

Constraints:

    2 <= skill.length <= 10^5
    skill.length is even.
    1 <= skill[i] <= 1000
"""

from typing import Counter, List


class Solution:
    """
    Runtime: 391 ms, faster than 80.53% of Python3 online submissions for Divide Players Into Teams of Equal Skill.
    Memory Usage: 29.5 MB, less than 68.50% of Python3 online submissions for Divide Players Into Teams of Equal Skill.
    """

    def dividePlayers(self, skill: List[int]) -> int:
        total_chemistry = 0
        skill = sorted(skill)
        goal_skill = skill[0] + skill[-1]

        l, r = 0, len(skill) - 1
        while l < r:
            if skill[l] + skill[r] != goal_skill:
                return -1
            total_chemistry += skill[l] * skill[r]
            l += 1
            r -= 1

        return total_chemistry


class Solution3:
    """
    leetcode solution 3: Map
    Runtime: 377 ms, faster than 94.87% of Python3 online submissions for Divide Players Into Teams of Equal Skill.
    Memory Usage: 29.5 MB, less than 31.15% of Python3 online submissions for Divide Players Into Teams of Equal Skill.
    """

    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        total_skill = sum(skill)

        # Check if total skill can be evenly distributed
        if total_skill % (n // 2) != 0:
            return -1

        target_skill = total_skill // (n // 2)
        skill_map = Counter(skill)
        total_chemistry = 0

        # Iterate through unique skill values
        for curr_skill, curr_freq in skill_map.items():
            partner_skill = target_skill - curr_skill

            # Check if valid partner skill exists with matching frequency
            if (
                partner_skill not in skill_map
                or curr_freq != skill_map[partner_skill]
            ):
                return -1

            # Calculate chemistry for all pairs with this skill
            total_chemistry += curr_skill * partner_skill * curr_freq

        # Return half of total chemistry (as each pair is counted twice)
        return total_chemistry // 2
