class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S: return ""
        cnt, l, r = [0]*26, S[0], S[0]
        for ch in S:
            cnt[ord(ch) - ord('a')] += 1
            l = min(l, ch)
            r = max(r, ch)
        l, r = ord(l) - ord('a'), ord(r) - ord('a')
        res = ""
        for i in range(l, r + 1):
            # print(cnt[i], cnt[i+1])
            if not cnt[i] or cnt[i] > cnt[i+1] + 1:
                return res if len(res) == len(S) else ""
            else:
                res += (chr(i + ord('a')) + chr(i+1+ord('a'))) * (cnt[i] - 1) + chr(i + ord('a'))
                cnt[i+1] -= cnt[i] - 1
        return res

s = Solution()
print(s.reorganizeString("aabbbc"))