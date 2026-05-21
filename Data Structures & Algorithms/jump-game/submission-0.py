class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return True

        start = len(nums) - 1

        dist = 1
        for i in range(start-1, -1, -1):
            if nums[i] >= dist:
                dist = 0
            dist += 1

        print(dist)
        return dist == 1 