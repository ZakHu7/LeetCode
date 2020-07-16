class Solution:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        h = len(matrix)
        w = len(matrix[0])
        maxSize = 0

        # dp = [[0 for _ in range(w)] for _ in range(h)]
        dpPre = [0 for _ in range(w)]
        dpCur = [0 for _ in range(w)]

        for y in range(h):
            for x in range(w):
                if not y or not x or matrix[y][x] == "0":
                    # dp[y][x] = ord(matrix[y][x]) - ord("0")
                    dpCur[x] = ord(matrix[y][x]) - ord("0")
                else:
                    # dp[y][x] = min(dp[y-1][x-1], dp[y-1][x], dp[y][x-1]) + 1
                    # maxSize = max(maxSize, dp[y][x])
                    dpCur[x] = min(dpPre[x-1], dpPre[x], dpCur[x-1]) + 1
                maxSize = max(maxSize, dpCur[x])
                    
            dpPre = dpCur.copy()


        return maxSize*maxSize


    # def maximalSquare(self, matrix):
    #     if not matrix:
    #         return 0
    #     h = len(matrix)
    #     w = len(matrix[0])
    #     allZeroes = True
    #     for y in range(h):
    #         for x in range(w):
    #             if matrix[y][x] == "1":
    #                 allZeroes = False
    #                 break
    #         if not allZeroes:
    #             break
    #     if allZeroes:
    #         return 0

    #     maxSize = 1

    #     while maxSize < min(h, w):
    #         maxSize += 1
    #         matrix = self.createHigherMatrix(matrix)
    #         if not matrix:
    #             maxSize -= 1
    #             break

    #     return maxSize*maxSize

    # def createHigherMatrix(self, matrix):
    #     h = len(matrix)
    #     w = len(matrix[0])
    #     newMatrix = [["0" for _ in range(w-1)] for _ in range(h-1)]
    #     foundHigher = False
    #     for y in range(h-1):
    #         for x in range(w-1):
    #             if matrix[y][x] == "1" and matrix[y+1][x] == "1" and matrix[y][x+1] == "1" and matrix[y+1][x+1] == "1":
    #                 newMatrix[y][x] = "1"
    #                 foundHigher = True
    #     if not foundHigher:
    #         return None
    #     return newMatrix

    # def maximalSquare(self, matrix):
    #     if not matrix:
    #         return 0
    #     h = len(matrix)
    #     w = len(matrix[0])
    #     maxSize = 0

    #     for y in range(h):
    #         for x in range(w):
    #             if matrix[y][x] == "1":
    #                 # Check for square size here
    #                 size = 1
    #                 isSquare = True

    #                 while size < min(h-y, w-x) and isSquare:
    #                     size += 1
    #                     isSquare = self.checkSquare(matrix, x, y, size)
    #                     if not isSquare:
    #                         size -= 1
                    
    #                 maxSize = max(maxSize, size)
    #     return maxSize*maxSize

    # def checkSquare(self, matrix, x, y, size):
    #     for sy in range(size):
    #         for sx in range(size):
    #             if matrix[y+sy][x+sx] == "0":
    #                 return False
    #     return True





s = Solution()
matrix = [
    ["1","1","1","1","0"],
    ["1","0","1","0","1"],
    ["1","1","0","1","1"],
    ["1","0","1","1","1"]
]

matrix2 = [
    ["0","0","0","0","0"],
    ["0","0","0","0","0"],
    ["0","0","0","0","0"],
    ["0","0","0","0","0"],
]


print(s.maximalSquare(matrix))


