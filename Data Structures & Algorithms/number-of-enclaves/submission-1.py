class Solution:

    def dfs(self, x, y, visited, grid):
        visited[x][y] = True
        grid[x][y] = 0
        neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for x_n, y_n in neighbors:
            new_x = x_n + x
            new_y = y_n + y
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and not visited[new_x][new_y] and grid[new_x][new_y]:
                self.dfs(new_x, new_y, visited, grid)

    def numEnclaves(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0]) 
        visited = [[False for _ in range(col)] for _ in range(row)]
        for _row in [0, row - 1]:
            for _col in range(col):
                if not visited[_row][_col] and grid[_row][_col]:
                    self.dfs(_row, _col, visited, grid)

        for _row in range(row):
            for _col in [0, col - 1]:
                if not visited[_row][_col] and grid[_row][_col]:
                    self.dfs(_row, _col, visited, grid)

        _sum = 0
        for lst in grid:
            _sum += sum(lst)
        return _sum
        
        