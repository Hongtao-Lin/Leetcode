from random import randint

# Sort algorithm medley, including selection, insert, swap sorts. 

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# two selection sort

def select_sort(a):
    n = len(a)
    for i in range(n):
        idx = i
        for j in range(i + 1, n):
            if a[j] < a[idx]:
                idx = j
        a[idx], a[i] = a[i], a[idx]

def heap_sort(a):
    def heapify(a, n, i):
        p, l, r = i, 2 * i + 1, 2 * i + 2
        if l < n and a[l] > a[p]:
            p = l
        if r < n and a[r] > a[p]:
            p = r
        if p != i:
            a[i], a[p] = a[p], a[i]
            heapify(a, n, p)
    n = len(a)
    for i in range(n // 2, -1, -1):
        heapify(a, n, i)
    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0)

# two swap sort

def bubble_sort(a):
    for j in reversed(range(len(a))):
        for i in range(j):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]

def quick_sort(a):
    def partition(a, lo, hi, mode=1):
        if mode == 1:
            pi = randint(lo, hi)
            a[hi], a[pi] = a[pi], a[hi]
        p = a[hi]
        i, j = lo, hi - 1
        for j in range(lo, hi):
            if a[j] < p:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[hi] = a[hi], a[i]
        return i

    def _quick_sort(a, lo, hi):
        if lo >= hi:
            return
        pi = partition(a, lo, hi)
        _quick_sort(a, lo, pi - 1)
        _quick_sort(a, pi + 1, hi)

    _quick_sort(a, 0, len(a) - 1)

# two insertion sort

def insert_sort(a):
    def get_insert_pos(a, num, binary=True):
        if binary:
            lo, hi = 0, len(a)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if a[mid] < num:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        else:
            i = 0
            while i < len(a) and a[i] < num:
                i += 1
            return i

    for i in range(1, len(a)):
        idx = get_insert_pos(a[:i], a[i])
        tmp = a[i]
        for j in range(i, idx, -1):
            a[j] = a[j - 1]
        a[idx] = tmp


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def get_array(node):
            a = []
            while node:
                a.append(node.val)
                node = node.next
            return a

        def get_list(a):
            l = ListNode(-1)
            p = l
            for num in a:
                l.next = ListNode(num)
                l = l.next
            return p.next

        a = get_array(head)
        n = len(a)

        quick_sort(a)

        return get_list(a)
