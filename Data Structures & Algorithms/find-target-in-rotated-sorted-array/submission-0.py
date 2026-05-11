class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = 0, n-1

        off = 0

        while l < r:
            mid = (l+r)//2

            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        
        off = l
        l,r = 0, n-1

        while l <= r:
            mid = (l+r) // 2
            i = (mid + off) % n

            if nums[i] < target:
                l = mid + 1
            elif nums[i] > target:
                r = mid - 1
            else:
                return i

        return -1

