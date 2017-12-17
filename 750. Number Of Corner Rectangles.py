# Ideas:
# Count the pair (i, j) that are both 1s, then we can construct a rectangle using them
import collections

class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        edge = collections.defaultdict(int)
        cnt = 0
        for row in grid:
            valid = []
            for i in range(len(row)):
                if row[i]:
                    for j in valid:
                        cnt += edge[(i, j)]
                        edge[(i, j)] += 1
                    valid.append(i)
        return cnt

