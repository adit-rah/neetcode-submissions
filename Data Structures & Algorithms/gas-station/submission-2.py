class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [gas[i]-cost[i] for i in range(len(gas))]
        print(diff)

        cand = {}
        for i in range(len(diff)):
            if diff[i] >= 0:
                if diff[i] not in cand:
                    cand[diff[i]] = [i]
                else:
                    cand[diff[i]].append(i)
        
        for c,im in cand.items():
            for i in im:
                c = 0
                for j in range(len(gas)):
                    c += diff[(i+j)%len(gas)]
                    if c < 0:
                        break
                print(c,i)
                if c >= 0:
                    return i

        return -1