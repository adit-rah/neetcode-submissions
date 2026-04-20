class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        u = []
        for n in nums:
            if n not in u:
                u.append(n)
            else:
                return True
        return False
        