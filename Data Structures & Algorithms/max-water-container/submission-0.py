class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        for i in range(len(heights) - 1):
            r = len(heights) - 1

            while i < r:
                dist = r - i
                lh, rh = heights[i], heights[r]
                height = min(lh,rh)
                area = height * dist
                res = max(res, area)
                r -= 1

        return res
        