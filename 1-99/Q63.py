class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return 0

        l = len(obstacleGrid)
        w = len(obstacleGrid[0])

        dp = [[0 for _ in range(w)] for _ in range(l)]

        for y in range(l):
            for x in range(w):
                if obstacleGrid[y][x] == 1:
                    dp[y][x] == 0
                elif y == 0 and x == 0:
                    dp[y][x] = 1
                elif y == 0:
                    dp[y][x] = dp[y][x-1]
                elif x == 0:
                    dp[y][x] = dp[y-1][x]
                else:
                    dp[y][x] = dp[y-1][x] + dp[y][x-1]



        return dp[l-1][w-1]


s = Solution()

grid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

print(s.uniquePathsWithObstacles(grid))