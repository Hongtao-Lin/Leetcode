import collections, re, string

class TreeNode(object):
    def __init__(self, x = 0):
        self.val = x
        self.left = None
        self.right = None

class ListNode(object):
    def __init__(self, x = 0):
        self.val = x
        self.prev = None
        self.next = None


# convert a binary tree to in-order-based doubly linked list

def concate(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1

    l1_left, l1_right = l1, l1.left
    l2_left, l2_right = l2, l2.left

    l1_right.right = l2_left
    l2_left.left = l1_right
    l1_left.left = l2_right
    l2_right.right = l1_left
    return l1

def Tree2List(root):
    if not root:
        return None
    head = ListNode(root.val)
    head.prev = head.next = head
    if not root.left and not root.right:
        return head

    left = Tree2List(root.left)
    right = Tree2List(root.right)
    if left:
        head = concate(left, head)
    if right:
        head = concate(head, right)
    return head


# convert a sequence of T/F logic expression to a value
# e.g. "(True or False) and True" = 1
# follow-up: add 'not'

def logic2val(s):
    ops, n = [], len(s)

    def dfs(i):
        while i < n:
            while len(ops) >= 2 and len(ops[-1]) == 2 and ops[-1][1] <= ops[-2][1]:
                op2, v2 = ops.pop()
                op1, v1 = ops.pop()
                v = v1 and v2 if op1 else v1 or v2
                ops.append([int(v), op2])

            if s[i] == " ":
                i += 1
                continue
            if s[i:].startswith("True"):
                i += 4
                if ops and ops[-1][-1] == -1:
                    ops[-1] = [0]
                else:
                    ops.append([1])
            elif s[i:].startswith("False"):
                i += 5
                if ops and ops[-1][-1] == -1:
                    ops[-1] = [1]
                else:
                    ops.append([0])
            elif s[i:].startswith("and"):
                i += 3
                ops[-1].append(1)
            elif s[i:].startswith("or"):
                i += 2
                ops[-1].append(0)
            elif s[i:].startswith("not"):
                i += 3
                ops.append([0, -1])
                continue
            elif s[i] == "(":
                v, i = dfs(i + 1)
                ops.append([v])
            else:
                i += 1
                break
        ops[-1].append(0)
        while len(ops) >= 2 and len(ops[-1]) == 2 and ops[-1][1] <= ops[-2][1]:
            v2, op2 = ops.pop()
            v1, op1 = ops.pop()
            v = v1 and v2 if op1 else v1 or v2
            # print(v1, v2)
            ops.append([v, op2])
        return ops[0][0], i

    return dfs(0)[0]

import operator, functools