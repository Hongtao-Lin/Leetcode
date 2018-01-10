"""
Idea:

Recursive solution is naive, try the iterative solution instead

The idea is to go to the left-most node first (and use a stack 
to record that path), then backtrack through the path to see if 
we can find possible right child to explore.

"""

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        n = len(preorder)
        head = root = TreeNode(preorder[0])
        s, i, j = [head], 1, 0
        while True:
            # go for the left-most child
            while head.val != inorder[j]:
                head.left = TreeNode(preorder[i])
                head = head.left
                s.append(head)
                i += 1
            # backtrack the stack to jump into right child
            while s and s[-1].val == inorder[j]:
                head = s[-1]
                j += 1
                s.pop()
            if i == n:
                break
            head.right = TreeNode(preorder[i])
            i += 1
            head = head.right
            s.append(head)

        return root
