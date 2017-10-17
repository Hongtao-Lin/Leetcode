"""Idea

Two solutions provided: 
- Recursive post-order traversal 
- Iterative post-order traversal: 
    Note the order of popping into stack
    Also the depth should be changed to 'height'
"""
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        self.flag = True

        def preorder(node):
            if not self.flag:
                return -1
            ld = rd = 0
            if node.left:
                ld = preorder(node.left) + 1
            if node.right:
                rd = preorder(node.right) + 1

            # do something
            if abs(ld - rd) > 1:
                self.flag = False
                return -1
            return max(ld, rd)

        preorder(root)

        return self.flag

    def isBalanced2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        s = [(root, 0)]
        depth = {}
        while s:
            node, d = s.pop()
            if node in depth:
                # do something
                ld = depth[node.left] if node.left else d
                rd = depth[node.right] if node.right else d
                depth[node] = max(ld, rd)
                if abs(ld - rd) > 1:
                    return False
                continue
            depth[node] = d
            s.append((node, d))
            if node.right:
                s.append((node.right, d + 1))
            if node.left:
                s.append((node.left, d + 1))

        return True
