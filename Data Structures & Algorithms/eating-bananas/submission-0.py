class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = max(piles)
        l,r = 1, m

        ans = m 
        while l <= r:
            mid = (l + r) // 2

            c = 0
            for b in piles:
                c += math.ceil(b/mid)
            
            if c <= h:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans