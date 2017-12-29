'''
Ideas:
- BFS: each code can possibly generate next 8 codes. 
'''

class Solution:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        if '0000' in deadends:
            return -1
        if target == '0000':
            return 0

        def next_state(code):
            for i in range(4):
                c1 = (int(code[i]) + 1) % 10
                c2 = (int(code[i]) - 1) % 10
                yield code[:i] + str(c1) + code[i + 1:]
                yield code[:i] + str(c2) + code[i + 1:]

        visited = set(deadends)
        q = ['0000']
        res = 0
        while True:
            sz = len(q)
            if not sz:
                break
            res += 1
            for _ in range(sz):
                c = q.pop()
                for c1 in next_state(c):
                    if c1 in visited:
                        continue
                    if c1 == target:
                        return res
                    q.insert(0, c1)
                    visited.add(c1)
        return -1


sol = Solution()
deadends = ["0000"]
target = "8888"
res = sol.openLock(deadends, target)
print(res)
