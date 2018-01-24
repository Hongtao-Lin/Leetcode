class Solution(object):
    def isMatch(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[0][0] = True
        for i in range(1, len(pattern), 2):
            dp[0][i+1] = (pattern[i] == '*') and dp[0][i-1]
        for j in range(1, len(pattern) + 1):
            for i in range(1, len(text) + 1):
                if pattern[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or  pattern[j-2] in {text[i-1], '.'} and dp[i-1][j]
                else:
                    dp[i][j] = pattern[j-1] in {text[i-1], '.'} and dp[i-1][j-1]

        return dp[-1][-1]

s = Solution()
text, pattern = "aab", ".*"
print(s.isMatch(text, pattern))