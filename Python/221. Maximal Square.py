'''Idea
Use dp[i][j] to record the max sqaure given that matrix[i][j] is the right-bottom corner
dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1, if matrix[i][j] == '1'

We can perform dp compression. But note that we have to explicitly assign 0 if the above equation fails
'''

class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]: return 0
        m, n = len(matrix), len(matrix[0])
        dp = [0] * n
        
        res, prev = 0, 0
        for i in range(m):
            for j in range(n):
                tmp = dp[j]
                if not i or not j:
                    dp[j] = int(matrix[i][j])
                elif matrix[i][j] == '1':
                    dp[j] = min(dp[j-1], dp[j], prev) + 1
                else:
                    dp[j] = 0
                res, prev = max(dp[j], res), tmp
        return res * res

s = Solution()
matrix = [["1","0","1","1","1"],["0","1","0","1","0"],["1","1","0","1","1"],["1","1","0","1","1"],["0","1","1","1","1"]]
s.maximalSquare(matrix)