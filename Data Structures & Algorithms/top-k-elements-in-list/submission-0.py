class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1
        
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        return [num for num, _ in sorted_items[:k]]

