class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        maxa = 0 

        for i in range(len(heights)):
            lasti = i
            while s and heights[i] < s[-1][1]:
                e = s.pop()
                maxa = max(maxa, e[1] * (i - e[0]))
                lasti = e[0]
            
            s.append((lasti, heights[i]))
        
        while s:
            e = s.pop()
            maxa = max(maxa, e[1] * (len(heights) - e[0]))
        
        return maxa
