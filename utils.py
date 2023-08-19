class ListNode:
    """Singly Linked list class"""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if not self.next:
            return f"{self.val}."
        return f"{self.val} -> {self.next}"

    @classmethod
    def fromString(cls, s):
        vals = s[1:-1].split(",")
        vals = list(map(int, vals))
        return cls.build(vals)

    @classmethod
    def build(cls, vals):
        if not vals:
            return None
        start = cls()
        curr = start
        for val in vals:
            curr.next = cls(val)
            curr = curr.next
        return start.next


class TreeNode:
    """Binary Tree class"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def fromString(cls, string):
        vals = string[1:-1].split(",")
        vals = map(lambda x: None if x == "null" else int(x), vals)
        return cls.build(list(vals))

    @classmethod
    def build(cls, values):
        if not values:
            return None

        vals = values[:]
        root = cls(vals.pop(0))
        nodes = [root]

        while vals:
            node = nodes.pop(0)

            nextval = vals.pop(0)
            if nextval is not None:
                node.left = cls(nextval)
                nodes.append(node.left)

            if not vals:
                break

            nextval = vals.pop(0)
            if nextval is not None:
                node.right = cls(nextval)
                nodes.append(node.right)

        return root

    def toString(self):
        vals = []
        q = [self]
        while q:
            node = q.pop(0)
            if not node:
                vals.append('null')
                continue
            vals.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        while q[-1] == 'null':
            q.pop()
        return f"[{','.join(vals)}]"
