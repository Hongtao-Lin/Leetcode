'''Idea:
Calculate the max area the building i can span (with height as the current one)
Use stack to calculate the left and right span, by maintaining ascending order in stack
'''

class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights: return 0
        n = len(heights)
        ls, rs, res = [], [], heights[:]
        for i, h in enumerate(heights):
            while ls and h <= heights[ls[-1]]:
                ls.pop()
            res[i] += h * (i - (-1 if not ls else ls[-1]) - 1)
            ls.append(i)
        for i, h in enumerate(heights[::-1]):
            while rs and h <= heights[n-1-rs[-1]]:
                rs.pop()
            res[n-1-i] += h * (i - (-1 if not rs else rs[-1]) - 1)
            rs.append(i)
        
        return max(res)

s = Solution()
heights = [2,1,5,6,2,3]
print(s.largestRectangleArea(heights))