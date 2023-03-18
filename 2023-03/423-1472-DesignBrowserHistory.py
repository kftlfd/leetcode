"""
Leetcode
1472. Design Browser History (medium)
2023-03-18

You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

    BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
    void visit(string url) Visits url from the current page. It clears up all the forward history.
    string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
    string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.

Example:

Input:
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
Output:
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

Explanation:
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
"""


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)


class BrowserHistory:
    """
    Runtime: 206 ms, faster than 98.01% of Python3 online submissions for Design Browser History.
    Memory Usage: 16.7 MB, less than 70.44% of Python3 online submissions for Design Browser History.
    """

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0

    def visit(self, url: str) -> None:
        self.curr += 1
        self.history[self.curr:] = [url]

    def back(self, steps: int) -> str:
        self.curr -= min(steps, self.curr)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(len(self.history) - 1, self.curr + steps)
        return self.history[self.curr]


class HistoryNode:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None


class BrowserHistory2:
    """
    doubly linked list
    Runtime: 292 ms, faster than 37.81% of Python3 online submissions for Design Browser History.
    Memory Usage: 16.8 MB, less than 10.57% of Python3 online submissions for Design Browser History.
    """

    def __init__(self, homepage: str):
        self.curr = HistoryNode(homepage)

    def visit(self, url: str) -> None:
        new_node = HistoryNode(url)
        new_node.prev = self.curr
        self.curr.next = new_node
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        n = steps
        while self.curr.prev and n > 0:
            self.curr = self.curr.prev
            n -= 1
        return self.curr.url

    def forward(self, steps: int) -> str:
        n = steps
        while self.curr.next and n > 0:
            self.curr = self.curr.next
            n -= 1
        return self.curr.url
