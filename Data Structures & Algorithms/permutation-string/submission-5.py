class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1,n2 = len(s1),len(s2)
        if n1 > n2:
            return False

        d1,d2 = {}, {}

        for c in s1:
            d1[c] = d1.get(c,0) + 1

        for i in range(n1):
            d2[s2[i]] = d2.get(s2[i],0) + 1

        for l in range(n1,n2):
            if d1 == d2:
                return True
            
            d2[s2[l-n1]] -= 1
            if d2[s2[l-n1]] == 0:
                d2.pop(s2[l-n1])

            d2[s2[l]] = d2.get(s2[l], 0) + 1

        return d1 == d2
