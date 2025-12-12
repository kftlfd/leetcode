"""
Leetcode
2025-12-12
3433. Count Mentions Per User
Medium

You are given an integer numberOfUsers representing the total number of users and an array events of size n x 3.

Each events[i] can be either of the following two types:

    Message Event: ["MESSAGE", "timestampi", "mentions_stringi"]
        This event indicates that a set of users was mentioned in a message at timestampi.
        The mentions_stringi string can contain one of the following tokens:
            id<number>: where <number> is an integer in range [0,numberOfUsers - 1]. There can be multiple ids separated by a single whitespace and may contain duplicates. This can mention even the offline users.
            ALL: mentions all users.
            HERE: mentions all online users.
    Offline Event: ["OFFLINE", "timestampi", "idi"]
        This event indicates that the user idi had become offline at timestampi for 60 time units. The user will automatically be online again at time timestampi + 60.

Return an array mentions where mentions[i] represents the number of mentions the user with id i has across all MESSAGE events.

All users are initially online, and if a user goes offline or comes back online, their status change is processed before handling any message event that occurs at the same timestamp.

Note that a user can be mentioned multiple times in a single message event, and each mention should be counted separately.

 

Example 1:

Input: numberOfUsers = 2, events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]]

Output: [2,2]

Explanation:

Initially, all users are online.

At timestamp 10, id1 and id0 are mentioned. mentions = [1,1]

At timestamp 11, id0 goes offline.

At timestamp 71, id0 comes back online and "HERE" is mentioned. mentions = [2,2]

Example 2:

Input: numberOfUsers = 2, events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","12","ALL"]]

Output: [2,2]

Explanation:

Initially, all users are online.

At timestamp 10, id1 and id0 are mentioned. mentions = [1,1]

At timestamp 11, id0 goes offline.

At timestamp 12, "ALL" is mentioned. This includes offline users, so both id0 and id1 are mentioned. mentions = [2,2]

Example 3:

Input: numberOfUsers = 2, events = [["OFFLINE","10","0"],["MESSAGE","12","HERE"]]

Output: [0,1]

Explanation:

Initially, all users are online.

At timestamp 10, id0 goes offline.

At timestamp 12, "HERE" is mentioned. Because id0 is still offline, they will not be mentioned. mentions = [0,1]

 

Constraints:

    1 <= numberOfUsers <= 100
    1 <= events.length <= 100
    events[i].length == 3
    events[i][0] will be one of MESSAGE or OFFLINE.
    1 <= int(events[i][1]) <= 10^5
    The number of id<number> mentions in any "MESSAGE" event is between 1 and 100.
    0 <= <number> <= numberOfUsers - 1
    It is guaranteed that the user id referenced in the OFFLINE event is online at the time the event occurs.


Hint 1
Sort events by timestamp and then process each event.
Hint 2
Maintain two sets for offline and online user IDs.
"""

from collections import defaultdict
from typing import List


class Solution01:
    """
    Runtime 86ms Beats 14.34%
    Memory 18.06MB Beats 59.62%
    """

    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        mentions = defaultdict(int)
        offlineUntil = defaultdict(int)

        events = sorted(events, key=lambda x: [
                        int(x[1]), 0 if x[0] == "OFFLINE" else 1])

        for evType, timestamp, data in events:
            ts = int(timestamp)

            if evType == "OFFLINE":
                uid = f"id{data}"
                offlineUntil[uid] = ts + 60
                continue

            if data == "ALL":
                for i in range(numberOfUsers):
                    uid = f"id{i}"
                    mentions[uid] += 1
                continue

            if data == "HERE":
                for i in range(numberOfUsers):
                    uid = f"id{i}"
                    if offlineUntil[uid] > ts:
                        continue
                    mentions[uid] += 1
                continue

            for uid in data.split(" "):
                mentions[uid] += 1

        ans = [0] * numberOfUsers
        for i in range(numberOfUsers):
            uid = f"id{i}"
            ans[i] = mentions[uid]

        return ans


class Solution02:
    """
    Runtime 40ms Beats 86.04%
    Memory 18.22MB Beats 13.58%
    """

    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        mentions = [0] * numberOfUsers
        offlineUntil = [0] * numberOfUsers

        evs = sorted(
            [(t, int(ts), d) for t, ts, d in events],
            key=lambda x: [x[1], 0 if x[0] == "OFFLINE" else 1],
        )

        for evType, ts, data in evs:
            if evType == "OFFLINE":
                uid = int(data)
                offlineUntil[uid] = ts + 60
                continue

            if data == "ALL":
                for uid in range(numberOfUsers):
                    mentions[uid] += 1
                continue

            if data == "HERE":
                for uid in range(numberOfUsers):
                    if offlineUntil[uid] > ts:
                        continue
                    mentions[uid] += 1
                continue

            for idstr in data.split(" "):
                uid = int(idstr[2:])
                mentions[uid] += 1

        return mentions


class Solution1:
    """
    leetcode solution: Playback After Sorting
    Runtime 40ms Beats 86.04%
    Memory 17.99MB Beats 79.25%
    """

    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda e: (int(e[1]), e[0] == "MESSAGE"))
        count = [0] * numberOfUsers
        next_online_time = [0] * numberOfUsers
        for event in events:
            cur_time = int(event[1])
            if event[0] == "MESSAGE":
                if event[2] == "ALL":
                    for i in range(numberOfUsers):
                        count[i] += 1
                elif event[2] == "HERE":
                    for i, t in enumerate(next_online_time):
                        if t <= cur_time:
                            count[i] += 1
                else:
                    for idx in event[2].split():
                        count[int(idx[2:])] += 1
            else:
                next_online_time[int(event[2])] = cur_time + 60
        return count
