class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns = set(nums)

        max_c = 0
        for n in ns:
            if n - 1 not in ns:
                length = 1
                curr = n

                while curr + 1 in ns:
                    length += 1
                    curr += 1
                
                if length > max_c:
                    max_c = length
        return max_c
