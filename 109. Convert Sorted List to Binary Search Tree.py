"""
Idea

Consider a one-pass O(n) time and O(1) space solution

Using the in-order framework, we can move the linked 
list forward and only consider the current node assignment

"""


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        self.head = head
        if not head:
            return None

        def count(head):
            p = head
            cnt = 0
            while p:
                cnt += 1
                p = p.next
            return cnt

        # wrap the construction into range (i, j)
        def inorder(i, j):
            if i > j:
                return None

            mid = (j + i) / 2
            left = inorder(i, mid - 1)
            node = TreeNode(self.head.val)
            # move linked list forward
            self.head = self.head.next
            node.left, node.right = left, inorder(mid + 1, j)
            return node

        return inorder(0, count(head) - 1)
