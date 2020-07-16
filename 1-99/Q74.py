class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        if not matrix:
            return False
        
        low = 0
        high = len(matrix) * len(matrix[0]) - 1

        rowLen = len(matrix[0])

        while low <= high:
            mid = low + (high - low) // 2

            if target < matrix[mid//rowLen][mid%rowLen]:
                high = mid - 1
            elif target > matrix[mid//rowLen][mid%rowLen]:
                low = mid + 1
            else:
                return True

        return False

s = Solution()
matrix = [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]

print(s.searchMatrix(matrix, 16))