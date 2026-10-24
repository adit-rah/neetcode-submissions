class Solution:
    def reverseBits(self, n: int) -> int:
        off = 1<<31
        res = 0

        while n:
            res += off if n % 2 == 1 else 0
            n = n >> 1
            off = off >> 1

        return res