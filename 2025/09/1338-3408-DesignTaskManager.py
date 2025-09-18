"""
Leetcode
2025-09-18
3408. Design Task Manager
Medium
Topics
premium lock iconCompanies

There is a task management system that allows users to manage their tasks, each associated with a priority. The system should efficiently handle adding, modifying, executing, and removing tasks.

Implement the TaskManager class:

    TaskManager(vector<vector<int>>& tasks) initializes the task manager with a list of user-task-priority triples. Each element in the input list is of the form [userId, taskId, priority], which adds a task to the specified user with the given priority.

    void add(int userId, int taskId, int priority) adds a task with the specified taskId and priority to the user with userId. It is guaranteed that taskId does not exist in the system.

    void edit(int taskId, int newPriority) updates the priority of the existing taskId to newPriority. It is guaranteed that taskId exists in the system.

    void rmv(int taskId) removes the task identified by taskId from the system. It is guaranteed that taskId exists in the system.

    int execTop() executes the task with the highest priority across all users. If there are multiple tasks with the same highest priority, execute the one with the highest taskId. After executing, the taskId is removed from the system. Return the userId associated with the executed task. If no tasks are available, return -1.

Note that a user may be assigned multiple tasks.

 

Example 1:

Input:
["TaskManager", "add", "edit", "execTop", "rmv", "add", "execTop"]
[[[[1, 101, 10], [2, 102, 20], [3, 103, 15]]], [4, 104, 5], [102, 8], [], [101], [5, 105, 15], []]

Output:
[null, null, null, 3, null, null, 5]

Explanation
TaskManager taskManager = new TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]]); // Initializes with three tasks for Users 1, 2, and 3.
taskManager.add(4, 104, 5); // Adds task 104 with priority 5 for User 4.
taskManager.edit(102, 8); // Updates priority of task 102 to 8.
taskManager.execTop(); // return 3. Executes task 103 for User 3.
taskManager.rmv(101); // Removes task 101 from the system.
taskManager.add(5, 105, 15); // Adds task 105 with priority 15 for User 5.
taskManager.execTop(); // return 5. Executes task 105 for User 5.

 

Constraints:

    1 <= tasks.length <= 10^5
    0 <= userId <= 10^5
    0 <= taskId <= 10^5
    0 <= priority <= 10^9
    0 <= newPriority <= 10^9
    At most 2 * 10^5 calls will be made in total to add, edit, rmv, and execTop methods.
    The input is generated such that taskId will be valid.


"""

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()

import heapq
from typing import List
from sortedcontainers import SortedSet


class TaskManager0:
    """
    Runtime 1061ms Beats 9.05%
    Memory 104.76MB Beats 48.30%
    """

    def __init__(self, tasks: List[List[int]]):
        self.tasks = SortedSet()
        self.task_priority = {}
        self.task_user = {}
        for user, task, priority in tasks:
            self.task_user[task] = user
            self.task_priority[task] = priority
            self.tasks.add((-priority, -task))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasks.add((-priority, -taskId))
        self.task_priority[taskId] = priority
        self.task_user[taskId] = userId

    def edit(self, taskId: int, newPriority: int) -> None:
        self.tasks.remove((-self.task_priority[taskId], -taskId))
        self.tasks.add((-newPriority, -taskId))
        self.task_priority[taskId] = newPriority

    def rmv(self, taskId: int) -> None:
        self.tasks.remove((-self.task_priority[taskId], -taskId))
        del self.task_priority[taskId]
        del self.task_user[taskId]

    def execTop(self) -> int:
        if not self.tasks:
            return -1

        _, taskId = self.tasks.pop(0)
        user = self.task_user[-taskId]
        del self.task_priority[-taskId]
        del self.task_user[-taskId]
        return user


class TaskManager1:
    """
    https://leetcode.com/problems/design-task-manager/solutions/7200885/clean-explanation-code-c-python-java
    Runtime 517ms Beats 60.38%
    Memory 110.28MB Beats 11.32%
    """

    def __init__(self, tasks: List[List[int]]):
        self.heap = []
        self.taskPriority = {}
        self.taskOwner = {}
        for t in tasks:
            self.add(t[0], t[1], t[2])

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.heap, (-priority, -taskId))
        self.taskPriority[taskId] = priority
        self.taskOwner[taskId] = userId

    def edit(self, taskId: int, newPriority: int) -> None:
        heapq.heappush(self.heap, (-newPriority, -taskId))
        self.taskPriority[taskId] = newPriority

    def rmv(self, taskId: int) -> None:
        self.taskPriority[taskId] = -1

    def execTop(self) -> int:
        while self.heap:
            negp, negid = heapq.heappop(self.heap)
            p = -negp
            tid = -negid
            if self.taskPriority.get(tid, -2) == p:
                self.taskPriority[tid] = -1
                return self.taskOwner.get(tid, -1)
        return -1
