class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        dp, directions = [[0] * n for _ in range(m)], [(0, -1), (-1, 0), (0, 1), (1, 0)]

        def dfs(i, j, val):
            dp[i][j] |= val
            for di, dj in directions:
                i1, j1 = i + di, j + dj
                if (not (i1 >= 0 and j1 >= 0 and i1 < m and j1 < n)) or (matrix[i][j] > matrix[i1][j1]) or (dp[i1][j1] & val == val):
                    continue
                dfs(i1, j1, val)

        for i in range(m):
            dfs(i, 0, 1)
            dfs(i, n - 1, 2)

        for i in range(n):
            dfs(0, i, 1)
            dfs(m - 1, i, 2)

        return [[i, j] for i in range(m) for j in range(n) if dp[i][j] == 3]
