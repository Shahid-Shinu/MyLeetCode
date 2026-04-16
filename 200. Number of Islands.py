class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0

        def check_island(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or  grid[i][j] == "0":
                return 
            
            grid[i][j] = "0"
            check_island(i-1, j)
            check_island(i+1, j)
            check_island(i, j-1)
            check_island(i, j+1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    check_island(i, j)
                    count += 1
        
        return count
