class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ds = []
        res = []

        for s in strs:
            dic = {}
            for c in s:
                dic[c] = dic.get(c,0) + 1
            
            if dic not in ds:
                ds.append(dic)
                res.append([s])
            else:
                i = ds.index(dic)
                res[i].append(s)
        
        return res