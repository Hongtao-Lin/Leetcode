"""
Idea:

Basic BFS
Alternate the order of exapnding children for different layer
Avoid the operation for reverse array

"""
from collections import *
import string



class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q, q_next, res = [root], [], []
        layer = 0
        while q:
            _res = []
            for i in reversed(xrange(len(q))):
                node = q[i]
                _res.append(node.val)
                children = []
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
                if layer % 2:
                    children = reversed(children)
                q_next += children
            layer += 1
            res.append(_res)
            q, q_next = q_next, []
        return res


s = Solution()
# nums = [6, 5, 3, 3, 3, 2, 2, 2, 2, 2]
# k = 3
# print(s.zigzagLevelOrder(nums, k))
