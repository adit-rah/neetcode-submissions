class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}

        for s in strs:
            res = str(sorted(s))
            if res not in ana:
                ana[res] = [s]
            else:
                ana[res].append(s)
        
        return list(ana.values())