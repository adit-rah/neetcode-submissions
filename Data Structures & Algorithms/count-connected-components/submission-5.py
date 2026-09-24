class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = list(range(n))

        def find(x):
            while x != res[x]:
                x = res[x]
            return x

        for a,b in edges:
            a = find(a)
            b = find(b)

            if a != b:
                res[b] = a

        return len({find(i) for i in range(n)})