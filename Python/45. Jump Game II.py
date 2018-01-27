'''Idea:
Record array of idxs such that idxs[i] = min idx to jump from idx[i] to i.
Then backtrack to the original starting point and count the step.
Advantage: can also output the exact path
'''

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        n = len(nums)
        r, idxs, d = 0, [-1], 0
        for i, num in enumerate(nums):
            if i + num > r:
                idxs += [i] * (min(i + num, n) - r)
                r = i + num
            if r >= n - 1:
                break
            if i == r:
                return -1
        i = n - 1
        while (i > 0):
            i = idxs[i]
            d += 1
        return d
