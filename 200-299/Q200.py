# Number of Islands
class Solution:
    def numIslands(self, grid):
        ans = 0

        myGrid = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1" and not myGrid[y][x]:
                    self.numIslandsR(grid, myGrid, x, y)
                    ans += 1
        # for y in range(len(grid)):
        #     for x in range(len(grid[0])):
        #         if grid[y][x] == "2":
        #             grid[y][x] = "1"

        return ans

    def numIslandsR(self, grid, myGrid, x, y):
        if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid) or grid[y][x] == "0" or myGrid[y][x]:
            return

        myGrid[y][x] = True

        self.numIslandsR(grid, myGrid, x + 1, y)
        self.numIslandsR(grid, myGrid, x - 1, y)
        self.numIslandsR(grid, myGrid, x, y + 1)
        self.numIslandsR(grid, myGrid, x, y - 1)



s = Solution()

grid = [
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,1]
]

grid2 = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]

print(s.numIslands(grid2))

print(grid2)