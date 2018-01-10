# Ideas:
# Simulation-based method, iterate over K and simulate the prob of being at each location
# Complexity: N^2*K

import collections

class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        def onBoard(x, y):
            return x >= 0 and y >= 0 and x < N and y < N

        dirs = [(1, 2), (1, -2), (-1, -2), (-1, 2), (2, 1), (2, -1), (-2, -1), (-2, 1)]
        q = {(r, c): 1.}
        for _ in range(K):
            q_next = collections.defaultdict(float)
            for (x, y), p in q.iteritems():
                for dx, dy in dirs:
                    if onBoard(x + dx, y + dy):
                        q_next[(x + dx, y + dy)] += p / 8
            q = q_next
        return sum(q[l] for l in q)


s = Solution()
res = s.knightProbability(25, 25, 12, 12)
