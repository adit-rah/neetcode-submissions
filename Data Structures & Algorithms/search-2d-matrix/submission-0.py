class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m = len(matrix), len(matrix[0])
        left, right = 0, n*m - 1

        while left <= right:
            mid = (left + right) // 2

            r,c = mid // m, mid % m

            val = matrix[r][c]

            if val > target:
                right = mid - 1 
            elif val < target:
                left = mid + 1
            else:
                return True

        return False