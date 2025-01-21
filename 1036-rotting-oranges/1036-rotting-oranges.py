class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mins_elapsed = 0
        while any(1 in row for row in grid):
            grid_copy = copy.deepcopy(grid)
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 2:
                        if j > 0 and grid[i][j-1] == 1:
                            grid_copy[i][j-1] = 2
                        if j+1 < n and grid[i][j+1] == 1:
                            grid_copy[i][j+1] = 2
                        if i > 0 and grid[i-1][j] == 1:
                            grid_copy[i-1][j] = 2
                        if i+1<m and grid[i+1][j] == 1:
                            grid_copy[i+1][j] = 2
            if grid == grid_copy:
                return -1
            mins_elapsed += 1
            grid = grid_copy
        return mins_elapsed