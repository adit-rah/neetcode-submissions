class Solution:
    def countBits(self, n: int) -> List[int]:
        def count(n):
            res = 0
            while n:
                n &= n-1
                res +=1 
            return res

        return list(map(count, range(n+1)))