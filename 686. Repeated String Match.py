class RollingArray(object):
    def __init__(self, arr, idx=0):
        self.arr = arr
        self.n = len(arr)
        self.i = (idx - 1) % self.n

    def next(self):
        self.i += 1
        if self.i == self.n:
            self.i = 0
        return self.arr[self.i]

    def setIdx(self, idx):
        self.i = idx - 1

    def clear(self):
        self.i = -1

class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        m, n = len(A), len(B)
        # KMP method
        rA, next, k = RollingArray(A), [-1], -1
        maxLen = 2*m if m >= n else 2*m + n
        s = B + "#" + "".join([rA.next() for i in range(maxLen)])
        # rA.next()
        for i in range(1, len(s)):
            while k != -1 and s[k+1] != s[i]:
                k = next[k]
            if s[k+1] == s[i]:
                k += 1
            next.append(k)
            if k == n-1:
                return 1 + (i - n - 1) // m
        return -1
    # def repeatedStringMatch(self, A, B):
    #     """
    #     :type A: str
    #     :type B: str
    #     :rtype: int
    #     """
    #     m, n = len(A), len(B)

    #     # rolling hash method:
    #     p, M = 113, 10**9 + 7
    #     p_n = pow(p, n, M)

    #     def rollingHash(h, si, sj):
    #         h = (p * h + ord(sj)) - ord(si) * p_n
    #         return h % M if h >= M or h < 0 else h

    #     # check if B is equal to rolling array starting from A[i]
    #     def isSame(i):
    #         rA = RollingArray(A, i)
    #         return all(rA.next() == B[j] for j in range(n))

    #     # get hash of B
    #     b_hash = 0
    #     for ch in B:
    #         b_hash = p * b_hash + ord(ch)
    #         if b_hash >= M:
    #             b_hash %= M

    #     # get hash of rolling array A, starts from idx 0
    #     rA = RollingArray(A)
    #     a_hash = 0
    #     for i in range(n):
    #         a_hash = p * a_hash + ord(rA.next())
    #         if a_hash >= M:
    #             a_hash %= M

    #     # if they are equal, we can match them directly
    #     if a_hash == b_hash and isSame(0):
    #         return 1 + (n - 1) // m

    #     # compute rolling hash iteratively
    #     for i in range(1, m):
    #         si, sj = A[i - 1], rA.next()
    #         a_hash = rollingHash(a_hash, si, sj)
    #         if a_hash == b_hash and isSame(i):
    #             return 1 + (n + i - 1) // m

    #     return -1


s = Solution()
A, B = "abcd", "cdabcdabcdab"
print(s.repeatedStringMatch(A, B))
