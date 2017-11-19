class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n, next, k = len(s), [-1] * len(s), -1
        for i in range(1, n):
            while k != -1 and s[k + 1] != s[i]:
                k = next[k]
            if s[k + 1] == s[i]:
                k += 1
            next[i] = k
        if next[-1] == -1:
            return False
        m, k = n - 1 - next[-1], n - 1
        return n % m == 0

sol = Solution()
s = "aba"
print(sol.repeatedSubstringPattern(s))