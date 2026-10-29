"""
Leetcode
2026-10-29
3841. Palindromic Path Queries in a Tree
Hard

You are given an undirected tree with n nodes labeled 0 to n - 1. This is represented by a 2D array edges of length n - 1, where edges[i] = [ui, vi] indicates an undirected edge between nodes ui and vi.

You are also given a string s of length n consisting of lowercase English letters, where s[i] represents the character assigned to node i.

You are also given a string array queries, where each queries[i] is either:

    "update ui c": Change the character at node ui to c. Formally, update s[ui] = c.
    "query ui vi": Determine whether the string formed by the characters on the unique path from ui to vi (inclusive) can be rearranged into a palindrome.

Return a boolean array answer, where answer[j] is true if the jth query of type "query ui vi" can be rearranged into a palindrome, and false otherwise.

 

Example 1:

Input: n = 3, edges = [[0,1],[1,2]], s = "aac", queries = ["query 0 2","update 1 b","query 0 2"]

Output: [true,false]

Explanation:

    "query 0 2": Path 0 → 1 → 2 gives "aac", which can be rearranged to form "aca", a palindrome. Thus, answer[0] = true.
    "update 1 b": Update node 1 to 'b', now s = "abc".
    "query 0 2": Path characters are "abc", which cannot be rearranged to form a palindrome. Thus, answer[1] = false.

Thus, answer = [true, false].

Example 2:

Input: n = 4, edges = [[0,1],[0,2],[0,3]], s = "abca", queries = ["query 1 2","update 0 b","query 2 3","update 3 a","query 1 3"]

Output: [false,false,true]

Explanation:

    "query 1 2": Path 1 → 0 → 2 gives "bac", which cannot be rearranged to form a palindrome. Thus, answer[0] = false.
    "update 0 b": Update node 0 to 'b', now s = "bbca".
    "query 2 3": Path 2 → 0 → 3 gives "cba", which cannot be rearranged to form a palindrome. Thus, answer[1] = false.
    "update 3 a": Update node 3 to 'a', s = "bbca".
    "query 1 3": Path 1 → 0 → 3 gives "bba", which can be rearranged to form "bab", a palindrome. Thus, answer[2] = true.

Thus, answer = [false, false, true].

 

Constraints:

    1 <= n == s.length <= 5 * 10^4
    edges.length == n - 1
    edges[i] = [ui, vi]
    0 <= ui, vi <= n - 1
    s consists of lowercase English letters.
    The input is generated such that edges represents a valid tree.
    1 <= queries.length <= 5 * 10^4
        queries[i] = "update ui c" or
        queries[i] = "query ui vi"
        0 <= ui, vi <= n - 1
        c is a lowercase English letter.


Hint 1
Use heavy light decomposition to break each path query into O(log n) segments.
Hint 2
Represent characters as a 26-bit mask and maintain segment data with XOR. A path can form a palindrome if the resulting mask has at most one bit set.
"""


class Solution:
    """
    leetcode solution: Binary Indexed Tree + Lowest Common Ancestor
    Runtime 2099ms Beats 16.33%
    Memory 107.19MB Beats 30.61%
    """

    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        LOG = n.bit_length()
        fa = [[0] * LOG for _ in range(n)]
        dep = [0] * n
        l = [0] * n
        r = [0] * n
        timer = 0

        def dfs(u: int, p: int) -> None:
            nonlocal timer
            timer += 1
            l[u] = timer
            fa[u][0] = p
            for v in g[u]:
                if v == p:
                    continue
                dep[v] = dep[u] + 1
                dfs(v, u)
            r[u] = timer

        dfs(0, 0)

        for j in range(1, LOG):
            for i in range(n):
                fa[i][j] = fa[fa[i][j - 1]][j - 1]

        def lca(u: int, v: int) -> int:
            if dep[u] < dep[v]:
                u, v = v, u
            diff = dep[u] - dep[v]
            for i in range(LOG):
                if (diff >> i) & 1:
                    u = fa[u][i]
            if u == v:
                return u
            for i in range(LOG - 1, -1, -1):
                if fa[u][i] != fa[v][i]:
                    u = fa[u][i]
                    v = fa[v][i]
            return fa[u][0]

        bit = self.BIT(n + 1)
        sl = list(s)
        for i in range(n):
            bit.updateRange(l[i], r[i], 1 << (ord(sl[i]) - ord("a")))

        ans = []
        for q in queries:
            op, *rest = q.split()
            if op == "update":
                u, c = int(rest[0]), rest[1]
                bit.updateRange(
                    l[u],
                    r[u],
                    (1 << (ord(sl[u]) - ord("a"))
                     ) ^ (1 << (ord(c) - ord("a"))),
                )
                sl[u] = c
            else:
                u, v = int(rest[0]), int(rest[1])
                w = lca(u, v)
                mask = (
                    bit.query(l[u])
                    ^ bit.query(l[v])
                    ^ (1 << (ord(sl[w]) - ord("a")))
                )
                ans.append(mask.bit_count() <= 1)
        return ans

    class BIT:
        def __init__(self, n: int):
            self.n = n
            self.tree = [0] * (n + 1)

        @staticmethod
        def lowbit(x: int) -> int:
            return x & -x

        def update(self, x: int, v: int) -> None:
            while x <= self.n:
                self.tree[x] ^= v
                x += self.lowbit(x)

        def query(self, x: int) -> int:
            ret = 0
            while x:
                ret ^= self.tree[x]
                x -= self.lowbit(x)
            return ret

        def updateRange(self, l: int, r: int, v: int) -> None:
            self.update(l, v)
            self.update(r + 1, v)
