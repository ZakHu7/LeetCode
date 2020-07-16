class Solution:
    def setZeroes(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        rows = [False for _ in range(len(matrix))]
        cols = [False for _ in range(len(matrix[0]))]


        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] == 0:
                    rows[y] = True
                    cols[x] = True

        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if rows[y] or cols[x]:
                    matrix[y][x] = 0

s = Solution()
matrix = [
    [0,1,0],
    [1,1,1],
    [1,1,1]
]

s.setZeroes(matrix)

print(matrix)
        