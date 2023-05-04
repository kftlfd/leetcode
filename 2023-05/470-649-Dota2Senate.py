"""
Leetcode
649. Dota2 Senate (medium)
2023-05-04

In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

    Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
    Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.

Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. Then if there are n senators, the size of the given string will be n.

The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".

Example 1:
Input: senate = "RD"
Output: "Radiant"
Explanation: 
The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.

Example 2:
Input: senate = "RDD"
Output: "Dire"
Explanation: 
The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And the third senator comes from Dire and he can ban the first senator's right in round 1. 
And in round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.
"""

import bisect
from queue import deque


class Solution:
    """
    Runtime: 62 ms, faster than 62.39% of Python3 online submissions for Dota2 Senate.
    Memory Usage: 16.6 MB, less than 7.03% of Python3 online submissions for Dota2 Senate.
    """

    def predictPartyVictory(self, senate: str) -> str:

        q = [1 if senator == 'R' else -1 for senator in senate]
        balance = 0

        while q:
            next_q = []
            next_round = False

            for senator in q:
                if senator == 1:
                    if balance >= 0:
                        next_q.append(senator)
                    else:
                        next_round = True
                    balance += 1

                else:
                    if balance <= 0:
                        next_q.append(senator)
                    else:
                        next_round = True
                    balance -= 1

            if not next_round:
                return "Radiant" if balance > 0 else "Dire"

            q = next_q


class Solution2:
    """
    leetcode solution 2: Boolean Array
    Runtime: 6997 ms, faster than 5.20% of Python3 online submissions for Dota2 Senate.
    Memory Usage: 16.4 MB, less than 11.62% of Python3 online submissions for Dota2 Senate.
    """

    def predictPartyVictory(self, senate: str) -> str:

        # Number of Senators
        N = len(senate)

        # To mark Banned Senators
        banned = [False] * N

        # Count of Each Type of Senator who are not-banned
        r_count = senate.count('R')
        d_count = N - r_count

        # Ban the candidate "to_ban", immediate next to "start_at"
        def ban(to_ban, start_at):

            # Find the next eligible senator of "to_ban" type
            # On found, mark him as banned
            pointer = start_at
            while True:
                if senate[pointer] == to_ban and not banned[pointer]:
                    banned[pointer] = True
                    break
                pointer = (pointer + 1) % len(senate)

        # Turn of Senator at this Index
        turn = 0

        # While both parties have at least one senator
        while r_count > 0 and d_count > 0:

            if not banned[turn]:
                if senate[turn] == 'R':
                    ban('D', (turn + 1) % N)
                    d_count -= 1
                else:
                    ban('R', (turn + 1) % N)
                    r_count -= 1

            turn = (turn + 1) % N

        return 'Radiant' if d_count == 0 else 'Dire'


class Solution3:
    """
    leetcode solution 3: Binary Search
    Runtime: 113 ms, faster than 23.55% of Python3 online submissions for Dota2 Senate.
    Memory Usage: 16.9 MB, less than 5.50% of Python3 online submissions for Dota2 Senate.
    """

    def predictPartyVictory(self, senate: str) -> str:

        # Number of Senators
        N = len(senate)

        # To mark Banned Senators
        banned = [False] * N

        # List of indices of Eligible Radiant and Dire Senators
        r_indices = [i for i in range(N) if senate[i] == 'R']
        d_indices = [i for i in range(N) if senate[i] == 'D']

        # Ban the senator of "indices" array next to "start_at"
        def ban(indices_array, start_at):

            # Find the index of "index of senator to ban" using Binary Search
            temp = bisect.bisect_left(indices_array, start_at)

            # If start_at is more than the last index,
            # then start from the beginning. Ban the first senator
            if temp == len(indices_array):
                banned[indices_array.pop(0)] = True

            # Else, Ban the senator at the index
            else:
                banned[indices_array.pop(temp)] = True

        # Turn of Senator at this Index
        turn = 0

        # While both parties have at least one senator
        while r_indices and d_indices:

            if not banned[turn]:
                if senate[turn] == 'R':
                    ban(d_indices, turn)
                else:
                    ban(r_indices, turn)

            turn = (turn + 1) % N

        return 'Radiant' if d_indices == [] else 'Dire'


class Solution4:
    """
    leetcode solution 5: Single Queue
    Runtime: 61 ms, faster than 63.61% of Python3 online submissions for Dota2 Senate.
    Memory Usage: 16.4 MB, less than 15.60% of Python3 online submissions for Dota2 Senate.
    """

    def predictPartyVictory(self, senate: str) -> str:

        # Eligible Senators of each party
        r_count = senate.count('R')
        d_count = len(senate) - r_count

        # Floating Ban Count
        d_floating_ban = 0
        r_floating_ban = 0

        # Queue of Senators
        q = deque(senate)

        # While any party has eligible Senators
        while r_count and d_count:

            # Pop the senator with turn
            curr = q.popleft()

            # If eligible, float the ban on the other party, enqueue again.
            # If not, decrement the floating ban and count of the party.
            if curr == 'D':
                if d_floating_ban:
                    d_floating_ban -= 1
                    d_count -= 1
                else:
                    r_floating_ban += 1
                    q.append('D')
            else:
                if r_floating_ban:
                    r_floating_ban -= 1
                    r_count -= 1
                else:
                    d_floating_ban += 1
                    q.append('R')

        # Return the party with eligible Senators
        return 'Radiant' if r_count else 'Dire'


s = Solution()
tests = [
    ("RD",
     "Radiant"),

    ("RDD",
     "Dire"),

    ("RDDR",
     "Radiant"),

    ("RDDDR",
     "Dire"),

    ("RDDRD",
     "Dire"),
]
for inp, exp in tests:
    res = s.predictPartyVictory(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
