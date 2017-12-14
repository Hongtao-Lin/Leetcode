import collections, re
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        def neighbors(i, j):
            res = []
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                i1, j1 = i + di, j + dj
                if i1 >= 0 and j1 >= 0 and i1 < m and j1 < n:
                    res.append((i1, j1))
            return res

        m, n = len(matrix), len(matrix[0])

        links, degree = collections.defaultdict(list), collections.defaultdict(int)
        for i in range(m):
            for j in range(n):
                for i1, j1 in neighbors(i, j):
                    if matrix[i1][j1] > matrix[i][j]:
                        links[(i, j)].append((i1, j1))
                        degree[(i1, j1)] += 1
        q, res = [(i, j) for i in range(m) for j in range(n) if (i, j) not in degree], 0
        while q:
            sz = len(q)
            res += 1
            for _ in range(sz):
                i, j = q.pop()
                for i1, j1 in links[(i, j)]:
                    degree[(i1, j1)] -= 1
                    if not degree[(i1, j1)]:
                        q.insert(0, (i1, j1))
        return res


sol = Solution()
mat = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
print(sol.longestIncreasingPath(mat))

res = re.findall(r'ab|bc', 'abcababc')
print(res)