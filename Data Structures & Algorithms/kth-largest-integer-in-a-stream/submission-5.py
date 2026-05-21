class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = []
    
        for n in nums:
            self.nums.append(n)
            self.insert(len(self.nums)-1)

    def insert(self, i):
        while i != 0 and self.nums[i] < self.nums[(i - 1) // 2]:
            parent = (i - 1) // 2

            self.nums[i], self.nums[parent] = self.nums[parent], self.nums[i]

            i = parent

        while len(self.nums) > self.k:
            self.pop()

    def pop(self):
        if not self.nums:
            return None

        self.nums[0], self.nums[-1] = self.nums[-1], self.nums[0]
        minimum = self.nums.pop()

        i = 0

        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i

            if left < len(self.nums) and self.nums[left] < self.nums[smallest]:
                smallest = left

            if right < len(self.nums) and self.nums[right] < self.nums[smallest]:
                smallest = right

            if smallest == i:
                break

            self.nums[i], self.nums[smallest] = self.nums[smallest], self.nums[i]
            i = smallest



    def add(self, val: int) -> int:
        self.nums.append(val)
        self.insert(len(self.nums)-1)

        return self.nums[0]
