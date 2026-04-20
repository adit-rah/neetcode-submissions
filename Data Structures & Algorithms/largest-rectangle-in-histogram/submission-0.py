class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        hs = len(heights)
        max_a = 0

        for i in range(hs + 1):
            h = heights[i] if i < hs else 0
            while stack and h < heights[stack[-1]]:
                ht = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_a = max(max_a, ht * w)
            stack.append(i)
        
        return max_a
