# Ideas:
# -1: DP: dp[i][j] means if s[i:j+1] is valid
#   Recurrence: if s[i] is '*' and dp[i+1][j] -> True
#               if s[i] can be made to be '(' and there exists a s[k] = ')' both segments are vailid

# -2: Greedy
#   Observation: we only need to maintain a lower & upper bound for open parathethis: it's continuous
#   Return False if in the process we have 'hi' reach 0


class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for k in range(n):
            for i in range(n - k):
                j = i + k
                if not k:
                    dp[i][j] = bool(s[i] == "*")
                    continue
                if dp[i + 1][j] and s[i] == "*":
                    dp[i][j] = True
                elif s[i] in "(*":
                    for l in range(k):
                        if s[i + 1 + l] in "*)" and (l == 0 or dp[i + 1][i + l]) and (l == k - 1 or dp[i + l + 2][j]):
                            dp[i][j] = True
                            break
        return dp[0][-1]

    def checkValidString2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lo, hi = 0, 0
        for ch in s:
            if ch == '(':
                lo += 1
                hi += 1
            elif ch == ')':
                lo = max(0, lo-1)
                if not hi:
                    return False
                hi -= 1
            else:
                hi += 1
                lo = max(0, lo-1)
        return lo == 0

sol = Solution()
s = "**(*())"
sol.checkValidString(s)