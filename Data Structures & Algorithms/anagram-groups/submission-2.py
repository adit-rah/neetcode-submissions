class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        ds = {}

        for s in strs:
            w = str(sorted(s))

            if w not in ds:
                ds[w] = [s]
            else:
                ds[w].append(s)
        
        for s in ds.values():
            res.append(s)
        
        return res