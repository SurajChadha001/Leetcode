class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        land = 0
        neighbor = 0
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    land += 1

                    if  i < rows - 1 and grid[i+1][j] == 1:
                        neighbor += 1
                    if j < cols - 1  and grid[i][j+1] == 1:
                        neighbor += 1
        return 4 * land - 2 * neighbor