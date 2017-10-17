"""Idea

A naive solution is to use DFS / stack to record all paths till now
    Note that we cannot wait till leaf node to operate, which is both
    inefficient and incorrect (duplicate path counted)
    Time complexity n^2, if balanced BT: nlogn

Use hashtable to cache the cnt of sum_so_far:
    cnt += cache[sum_so_far - taget]
    When exiting the subtree, the current sum should be substracted
    Linear time!

"""
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0

        def extractPath(path):
            cumSum, res = 0, 0
            for v in reversed(path):
                cumSum += v
                if cumSum == sum:
                    res += 1
            return res

        s, res = [(root, [])], 0
        while s:
            node, path = s.pop()
            # sum -= node.val
            tmppath = path + [node.val]
            res += extractPath(tmppath)
            if not node.left and not node.right:  # leaf
                continue
            if node.left:
                s.append((node.left, tmppath))
            if node.right:
                s.append((node.right, tmppath))

        return res

    def pathSum2(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: int
        """
        self.count = 0
        preDict = {0: 1}

        def dfs(p, target, pathSum, preDict):
            if p:
                pathSum += p.val
                self.count += preDict.get(pathSum - target, 0)
                preDict[pathSum] = preDict.get(pathSum, 0) + 1
                dfs(p.left, target, pathSum, preDict)
                dfs(p.right, target, pathSum, preDict)
                preDict[pathSum] -= 1
        dfs(root, target, 0, preDict)
        return self.count